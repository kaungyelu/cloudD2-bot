# src/bot.py
from telegram.ext import ApplicationBuilder
from js import Response, env
import logging
from .handlers import register_handlers

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Cloudflare Workers entry point
async def on_fetch(request, env):
    """Main handler for Cloudflare Workers"""
    try:
        # Initialize bot with token from wrangler.toml
        app = ApplicationBuilder().token(env.BOT_TOKEN).build()
        
        # Register all handlers
        register_handlers(app)
        
        await app.initialize()
        
        # Process Telegram webhook update
        if request.method == "POST":
            data = await request.json()
            update = Update.de_json(data, app.bot)
            await app.process_update(update)
            
        return Response.new("OK")
        
    except Exception as e:
        logger.error(f"Error in on_fetch: {str(e)}")
        return Response.new("Server Error", status=500)
