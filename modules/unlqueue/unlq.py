from discord.ext import commands
from discord.ext import tasks
import discord

#class helpFlags(commands.FlagConverter):
#    command: str = commands.flag(description='Command that info is desired for')


class unlqCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self._last_member = None
        bot.remove_command("help")

    @commands.hybrid_command()
    #async def help(ctx, *, flags: helpFlags):
    async def help(self, ctx, command):
        if(command=='test'):
            await ctx.reply(f'The command you wanted help with was {command}.\nThis command is to test hybrid command functionality.')
        else:
            await ctx.reply(f'The command you wanted help with was {command}.\nThis command is not currently recognised by the bot or has no help description.')


async def setup(bot):
    await bot.add_cog(unlqCog(bot))