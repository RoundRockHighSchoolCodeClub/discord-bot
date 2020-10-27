import discord
from discord.ext import commands

class Tests(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        await ctx.send('Hello {0.name}'.format(member))

def setup(bot):
    bot.add_cog(Tests(bot))
