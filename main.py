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



def startChatter():
    factory = ChatterBotFactory()

    bot1 = factory.create(ChatterBotType.CLEVERBOT)
    bot1session = bot1.create_session()

    s = 'Hi'
    while (1):
        print('bot1> ' + s)

        s = bot1session.think(s)
        print('bot2> ' + s)

        s = bot1session.think(s)



startChatter()


#removed token
client.run("Mjc2MTM4NDk5NTU0NjcyNjUx.C3ZRBw.AkKdtU5dE1yXzd5dilX_OVvmNSU")

