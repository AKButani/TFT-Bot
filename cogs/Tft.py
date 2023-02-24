from discord.ext import commands
import discord
import config
from riotwatcher import TftWatcher

watcher = TftWatcher(api_key=config.tft_key)

class RegionView(discord.ui.View):
    chosen = None
    async def on_timeout(self) -> None:
        # Step 2
        for item in self.children:
            item.disabled = True

        # Step 3
        await self.message.edit(view=self)

    @discord.ui.button(label='EUN')
    async def example_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Hello!', ephemeral=True)

    @discord.ui.button(label="EUW")
    async def second(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('second!', ephemeral=True)
    






class Tft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def player(self, ctx, region, *, player_name):
        #todo: add message with buttons for region
        region += "1"
        data = watcher.summoner.by_name(region=region, summoner_name=player_name)
        print(data)
        embed = discord.Embed(title=player_name, url = None)
        embed.set_thumbnail(url="http://ddragon.leagueoflegends.com/cdn/13.4.1/img/profileicon/{}.png".format(data["profileIconId"]))
        embed.add_field(name="Summoner level:", value=str(data["summonerLevel"]))
        rank_info = watcher.league.by_summoner(region=region, encrypted_summoner_id=data["id"])[0]
        print(rank_info)
        embed.add_field(name="Rank", value=rank_info["tier"] + " " + rank_info["rank"])
        #todo: get image from the id http://ddragon.leagueoflegends.com/cdn/13.4.1/img/profileicon/685.png
        await ctx.send(embed = embed)
        
        


    """
    @commands.command()
    async def timeout_example(self, ctx):
        
        view = MyView()
        # Step 1
        view.message = await ctx.send('Press me!', view=view)
    """

async def setup(bot):
    await bot.add_cog(Tft(bot))