from discord.ext import commands
import discord
import requests
import random
 #TODO: Alex you can work on your discord bot here
    #make sure every function has self as a parameter
class Spotify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def newsBitcoin(self, ctx):
        URL = "https://newsapi.org/v2/everything"
        PARAMS = {'q':"bitcoin", 'ApiKey':"1ec10d5995c444e89086aa2afbebea6b"}
        r = requests.get(url = URL, params = PARAMS)
        data = r.json()
        randArticleDescription = data['articles'][random.randint(0, 99)]['description']
        await ctx.send(randArticleDescription)

async def setup(bot):
    await bot.add_bot(News(bot))

