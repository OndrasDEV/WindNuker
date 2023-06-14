from discord_webhook import DiscordWebhook
import json
config = json.load(open("config.json",encoding="utf-8"))
def spam(looplen,webhooklink,msg):
    for i in range(looplen):
        webhook = DiscordWebhook(url=webhooklink,rate_limit_retry=True, username=config["username"],content=msg)
        response = webhook.execute()

