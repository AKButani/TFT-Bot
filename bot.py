# This example requires the 'message_content' intent.
import config

#from riotwatcher import TftWatcher

#watcher = TftWatcher(api_key=)

import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix="/",intents=intents)

@bot.event
async def on_ready():
    await bot.load_extension("cogs.Basic")
    await bot.load_extension("cogs.Tft")
    print(f'We have logged in as {bot.user}')


bot.run(config.TOKEN)

"""
@bot.command(name='hello')
async def on_message(ctx):
    await ctx.send('Hello!')

 #this is a nicer way to write the commented block above
 #command name is the same as function name.
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")


@bot.command()
async def bye(ctx):
    await ctx.send("Bye! :(")
    emoji = "👋🏼"
    await ctx.message.add_reaction(emoji)


@bot.command(name="bye")
async def on_message(ctx):
    await ctx.send("Bye! :(")
    emoji = "👋🏼"
    await ctx.message.add_reaction(emoji)



@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1073167438042120204)
    await channel.send("Welcome " + member.name)
"""





