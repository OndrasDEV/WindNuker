from discord_webhook import DiscordWebhook
def spam(looplen,webhooklink,msg):
    for i in range(looplen):
        webhook = DiscordWebhook(url=webhooklink,rate_limit_retry=True, username="Wind Nuker V1",content=msg)
        response = webhook.execute()

