import discord
from discord.ext import commands


B = ('b', 'B', '🅱️')
QUACK = '<a:quack:875209729117413387>'


class Quack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content in B:
            await message.add_reaction(QUACK)

    # @commands.Cog.listener()
    # async def on_reaction_add(self, reaction, user):
    #     if reaction.emoji == '🅱️':
    #         await reaction.message.reply(QUACK)


def setup(bot):
    bot.add_cog(Quack(bot))
