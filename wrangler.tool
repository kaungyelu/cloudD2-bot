name = "my-telegram-bot"
type = "python"
account_id = "your-cloudflare-account-id"
workers_dev = true
compatibility_date = "2023-05-18"

[vars]
BOT_TOKEN = "your-telegram-bot-token"

[build]
command = "pip install -r requirements.txt"

[[rules]]
type = "json"
globs = ["**/*.json"]
