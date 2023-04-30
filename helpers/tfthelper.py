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
    for unit in info["units"]:
        res.setdefault(unit["character_id"], 0)
        res[unit["character_id"]] += 1
    return res

def convert_unit_name(el, data):
    for unit in data['sets']['8']['champions']:
        if unit['apiName'] == el:
            return (unit['name'], unit['icon'])

def convert_list(res, data):
    new_list = []
    for el in res:
        new_list.append(convert_unit_name(el, data))
    return new_list
