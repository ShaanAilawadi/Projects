import discord

client = discord.Client()


@client.event
async def on_message(message):
    # users message
    msg = message.content

    if msg.startswith('https://'):
        msg.delete()
