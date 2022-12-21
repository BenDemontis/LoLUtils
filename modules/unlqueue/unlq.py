import discord
from discord.ext import commands, tasks
from discord import app_commands
from typing import Literal

class queueFlags(commands.FlagConverter):
    command: str = commands.flag(description='Command that info is desired for')

#Defines a cog that is used to handle the basics of the UNLQ module.
class unlqCog(commands.Cog):
    def __init__(self, bot: commands.Bot)  -> None:
        self.bot = bot
        self._last_member = None
        self.ctx_menu = app_commands.ContextMenu(  
            name = 'queue',
            callback = self.queueRun,
        )
        self.bot.tree.add_command(self.ctx_menu)
        bot.remove_command("help")

    async def cog_unload(self) -> None:
        self.bot.tree.remove_command(self.ctx_menu.name, type=self.ctx_menu.type)

    #@commands.hybrid_command()
    #async def help(ctx, *, flags: helpFlags):
    #async def help(self, ctx, command):
    #    if(command=='test'):
    #        await ctx.reply(f'The command you wanted help with was {command}.\nThis command is to test hybrid command functionality.')
    #    else:
    #        await ctx.reply(f'The command you wanted help with was {command}.\nThis command is not currently recognised by the bot or has no help description.')


#Change this back to an app command not a context menu.
    #@app_commands.command(name='unlq',description='queue for UNLQ')
    async def queueRun(self, interaction: discord.Interaction, message: discord.Message) -> None:
        await interaction.response.send_message('You have queued for UNLQ!', ephemeral=True)

    
#When unlq.py is loaded as an extension, the extension will then load the unlq cog.
async def setup(bot):
    await bot.add_cog(unlqCog(bot))
    print(f'UNLQ cog loaded')