from discord.ext import commands
import discord

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """
    @bot.command(name='hello')
    async def on_message(ctx):
        await ctx.send('Hello!')
    """
    #this is a nicer way to write the commented block above
    #command name is the same as function name.
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello!")

    @commands.command()
    async def bye(self, ctx):
        await ctx.send("Bye! :(")
        emoji = "👋🏼"
        await ctx.message.add_reaction(emoji)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.channels,name= "general")
        #channel = bot.get_channel(1073167438042120204)
        await channel.send("Welcome " + member.name)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("This command doesn't exist. Try using /help to make sure you use the right command")
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Your command is missing an argument. Try using /help to make sure you use the right command")
        else:
            await ctx.send(error)


async def setup(bot):
    await bot.add_cog(Basic(bot))