name = "D2_kk_bot"
type = "python"
account_id = "e21c6c77f209505158e4169f172541e4"
workers_dev = true
compatibility_date = "2023-05-18"

[vars]
BOT_TOKEN = "8058979076:AAE9v6HTt8kXIvde5EoiG02wBnbZ3PBO0cs"

[build]
command = "pip install -r requirements.txt"

[[rules]]
type = "json"
globs = ["**/*.json"]
