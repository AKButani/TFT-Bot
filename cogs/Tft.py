from discord.ext import commands
import discord
import config
from riotwatcher import TftWatcher, ApiError
from helpers import tfthelper
import requests
from table2ascii import table2ascii as t2a, PresetStyle

watcher = TftWatcher(api_key=config.tft_key)


class Tft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        url =  "https://raw.communitydragon.org/latest/cdragon/tft/en_us.json"
        response = requests.get(url)
        self.data = response.json()
    
    
    @commands.command()
    async def player(self, ctx, *, player_name):
        #todo: add message with buttons for region
        """ region += "1" #temp sol for popular regions"""
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

        
        await ctx.send(embed = embed)

    @commands.command()
    async def data_units(self, ctx, count, *, player):
        res = {}
        region = await tfthelper.region_selection(ctx)
        try:
            summoner = watcher.summoner.by_name(region=region, summoner_name=player)
            match_history = watcher.match.by_puuid(region, summoner['puuid'], count=count)
            for match in match_history:
                match_info = watcher.match.by_id(region,match)
                res = tfthelper.find_units_played(res, tfthelper.find_correct_info(match_info, summoner['puuid']))
            #temp = list(dict(sorted(res.items(), key = lambda x: x[1], reverse=True)).keys())[:10] #list of fav 10 units
            temp = sorted(res.items(), key= lambda x: x[1][0], reverse=True)
            t2 = tfthelper.convert_list(temp, self.data)
            """
            msg = ""
            for unit in t2:
                msg += unit[0] + ", "
            await ctx.send("Your favourite units are: ")
            await ctx.send(msg[:-2])
            """
            output = t2a(header=["Unit", "Games", "Average Placement", "Top 4 %"],
             body=t2[:10],
             style=PresetStyle.minimalist)
        
            await ctx.send(f"```\n{output}```")

        except ApiError as err:
            await ctx.send(err)

        #TODO: Add average placement, items, etc.

        
        
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
