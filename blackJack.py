# blackjack
import discord
import asyncio
from discord.ext import commands

class blackJack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def blackJack(self, ctx):
        economy = self.bot.get_cog('Economy')
        if economy is not None:
            money = 10;
            await economy.deposit_money(ctx.author, money)
        m = await ctx.send(f'Welcome To Blackjack! React with ✅ to begin.')
        await m.add_reaction("✅")
        
               

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == "✅"

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await m.edit('timed out. :(')
        else:
            await ctx.send('POGCHAMP')

def setup(bot):
    bot.add_cog(blackJack(bot))
