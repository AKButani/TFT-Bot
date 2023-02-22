# This example requires the 'message_content' intent.
import config

import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix="/",intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(name='hello')
async def on_message(ctx):
    await ctx.send('Hello!')

@bot.command(name="bye")
async def on_message(ctx):
    await ctx.send("Bye! :(")
    emoji = "👋🏼"
    await ctx.message.add_reaction(emoji)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1073167438042120204)
    await channel.send("Welcome " + member.name)

bot.run(config.TOKEN)
