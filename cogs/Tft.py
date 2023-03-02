from discord.ext import commands
import discord
import config
from riotwatcher import TftWatcher, ApiError
from helpers import tfthelper

watcher = TftWatcher(api_key=config.tft_key)


class Tft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def player(self, ctx, *, player_name):
        #todo: add message with buttons for region
        """/player <playername> finds the stats of the player in a given region and will give you some information."""
        region = await tfthelper.region_selection(ctx)

        embed = discord.Embed(title=player_name, url = None) 
        try:
            summoner_data = watcher.summoner.by_name(region=region, summoner_name=player_name)
            rank_info = watcher.league.by_summoner(region=region, encrypted_summoner_id=summoner_data["id"])[0]
            
            embed.set_thumbnail(url="http://ddragon.leagueoflegends.com/cdn/13.4.1/img/profileicon/{}.png".format(summoner_data["profileIconId"]))
            embed.add_field(name="Summoner level:", value=str(summoner_data["summonerLevel"]))
            embed.add_field(name= "Region", value=(region[:-1]).upper())
            embed.add_field(name="Rank", value=rank_info["tier"] + " " + rank_info["rank"])
            #add as many fields as necessary
        except ApiError as err:
            if err.response.status_code == 404:
                await ctx.send("The player doesn't exist in the given region.")
                return
            await ctx.send(err)
            await ctx.send("Make sure the form is /player <player_name> ")
            return
        #print(rank_info)

        #TODO exception handling!!
        
        await ctx.send(embed = embed)
        
    """
    @commands.command()
    async def reg(self, ctx):
        chosen = await tfthelper.region_selection(ctx)        
        await ctx.send("Looking for " + "None" + " in " + chosen)

    
    @commands.command()
    async def timeout_example(self, ctx):
        
        view = MyView()
        # Step 1
        view.message = await ctx.send('Press me!', view=view)
    """

async def setup(bot):
    await bot.add_cog(Tft(bot))