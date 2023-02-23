from discord.ext import commands
import discord

class Spotify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #TODO: Alex you can work on your discord bot here
    #make sure every function has self as a parameter

async def setup(bot):
    await bot.add_bot(Spotify(bot))
