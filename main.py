import discord
import asyncio
import logging
from discord.ext import commands
from chatterbotapi import ChatterBotFactory, ChatterBotType

logging.basicConfig(level=logging.INFO)
bot = commands.Bot(command_prefix="!")

@bot.command()
async def messages(ctx): # this is the same as what you did before
    """Counts all the messages you have sent."""
    counter = 0
    tmp = await ctx.send("Calcuating messages...")
    async with ctx.channel.typing(): # this makes the bot start typing.
        async for log in ctx.channel.history(limit=100):
            if log.author == ctx.author:
                counter += 1
        await tmp.delete()
        await ctx.send("Done! You have {} messages.".format(counter))
        # sending a message stops bot typing.

@bot.command()
async def sleep(ctx, time: int=5):
    """Makes the bot sleep for 5 seconds, or the seconds you provide."""
    await asyncio.sleep(time)
    await ctx.send("Done sleeping!")

@bot.command()
async def random(ctx, message: str=None):
    """I don't know what you want to do here"""
    await ctx.send("Not working yet.")


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if bot.user.mentioned_in(message):
        try:
            if str(message.author) == "Yakitrak#2464":
                factory = ChatterBotFactory()
                bot1 = factory.create(ChatterBotType.PANDORABOTS,
                                      "b0dafd24ee35a477")
                bot1session = bot1.create_session()
                # msg = message.content.split()
                # for word in msg:
                #    if word ==
                # Didn't know what you wanted up there, so I commented it out.
                await message.channel.send(bot1session.think(message.content))
        except:
          await message.channel.send("The Pandorabot api is down "
                                     "so you're seeing this message!")


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user)
    print("User ID:")
    print(bot.user.id)
    print("Number of servers/guilds:")
    print(len(bot.guilds))
    print('------')


bot.run("MzE4MDcxOTU0ODk0NDg3NTY0.DqVENg.4e3DhtRmzYNl9EoqH53YldpLG8Q") # this is what a token looks like, replace it with a real one
