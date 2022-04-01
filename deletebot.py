import discord
import os
import requests
import json

# makes discord usable
client = discord.Client()

@client.event
async def on_message(message):

    # members message
    msg = message.content

    # establishes channel and deletes link
    if str(message.channel) == 'general' and msg.startswith("https://"):
        await message.channel.purge(limit=1)

    # establishes channel and deletes link
    if str(message.channel) == 'general' and message.content.startswith("http"):
        await message.channel.purge(limit=1)


if __name__ == '__main__':
    # runs the bot
    client.run("OTU5Mjk2ODQzNTAwNjM4MjA4.YkZ0zg.A7H_wlId1u9IR3NMG3mO4c5EZi0")
