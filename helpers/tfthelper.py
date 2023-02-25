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
