from riotwatcher import TftWatcher, ApiError
import discord

class RegionView(discord.ui.View):
    chosen = None

    async def on_timeout(self) -> None:
        # Step 2
        for item in self.children:
            item.disabled = True

        # Step 3
        await self.message.edit(view=self)

    async def disable(self, interaction: discord.Interaction):
        for item in self.children:
            item.disabled = True
        await interaction.response.edit_message(view=self)
        

    @discord.ui.button(label='EUN')
    async def eun(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.disable(interaction)
        #await interaction.response.edit_message(view = self)
        await interaction.followup.send('You chose EUN!', ephemeral=True)
        self.chosen = "eun1"
        self.stop()
        

    @discord.ui.button(label="EUW") 
    async def euw(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.disable(interaction)
        await interaction.followup.send('You chose EUW!', ephemeral=True)
        self.chosen = "euw1"
        self.stop()

    @discord.ui.button(label="NA")
    async def na(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.disable(interaction)
        await interaction.followup.send('You chose NA!', ephemeral=True)
        self.chosen = "na1"
        self.stop()
    
def get_summoner_from_id(watcher: TftWatcher, region, player_name):
    pass


async def region_selection(ctx):
    view = RegionView()
    view.message = await ctx.send("Choose the region", view=view)
    await view.wait()
    return view.chosen


def find_correct_info(match_info, puuid):
    for participant in match_info['info']['participants']:
        if participant['puuid'] == puuid:
            return participant

def find_units_played(res: dict, info):
    placement = info["placement"]
    top_four = 1 if placement <=4 else 0
    units_counted_already = []
    for unit in info["units"]:
        if unit["character_id"] not in units_counted_already:
            units_counted_already.append(unit["character_id"])
            res.setdefault(unit["character_id"], (0,0,0))
            res[unit["character_id"]] = (res[unit["character_id"]][0] + 1, res[unit["character_id"]][1] + placement, res[unit["character_id"]][2] + top_four)
    return res

def convert_unit_name(el, data):
    for unit in data['sets']['8']['champions']:
        if unit['apiName'] == el:
            return unit['name']

def convert_list(res, data):
    new_list = []
    for el in res:
        name = convert_unit_name(el[0], data)
        new_list.append([name, el[1][0], round((el[1][1]*1.0)/el[1][0],2), round(el[1][2]*100.0 /el[1][0],2)])
        #name, number of games, avg placement, number of top 4s
    return new_list
