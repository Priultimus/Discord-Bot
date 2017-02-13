import discord
import asyncio
from chatterbotapi import ChatterBotFactory, ChatterBotType

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith("!messages"):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    elif message.content.startswith('!help'):
        await client.send_message(message.channel, "To be implemented")

    elif message.content.startswith("!random"):
        if message.contains("Hello"):
            await client.send_message(message.channel, "Not working yet")

    elif client.user.mentioned_in(message):
        try:
            if str(message.author) == "Yakitrak#2464":
                factory = ChatterBotFactory()
                bot1 = factory.create(ChatterBotType.PANDORABOTS, "b0dafd24ee35a477")
                bot1session = bot1.create_session()
                msg = message.split()
                for word in msg:
                    if word == 
                await client.send_message(message.channel, bot1session.think(message))
        except:
          await client.send_message(message.channel, "pandorabot api is down so you're seeing this message!")




client.run("Mjc2MTM4NDk5NTU0NjcyNjUx.C3ZRBw.AkKdtU5dE1yXzd5dilX_OVvmNSU")
