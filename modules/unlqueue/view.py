import discord
from discord import app_commands, Interaction
from discord.ext import commands, tasks



class unlqView(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)
        
        self.add_item(dropdown())


class queueCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self._last_member = None
        
        bot.add_view(discord.ui.View(timeout=None).add_item(dropdown()))
        
    @commands.command()
    async def startqueue(self, ctx, *args):
        await ctx.send(f'Queue for UNLQ here:', view=unlqView())

class dropdown(discord.ui.Select):
    def __init__(self):

        options = [
            discord.SelectOption(label='Top', default=False),
            discord.SelectOption(label='Jungle', default=False),
            discord.SelectOption(label='Mid', default=False),
            discord.SelectOption(label='Bot', default=False),
            discord.SelectOption(label='Support', default=False),
            discord.SelectOption(label='Fill', default=False),
        ]


        super().__init__(placeholder='Select a role', custom_id='unlqSelectMenu', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        print(f'User that interacted:{interaction.user}\nValues output:{super().values}')
        await interaction.response.send_message(f'You have chosen: {super().values}', ephemeral=True)



    #@discord.ui.button(label='Top', style=discord.ButtonStyle.green, custom_id='unlqView:top')
    #async def top(self, interaction: discord.Interaction, button: discord.ui.Button):
    #    await interaction.response.send_message('You are queued for toplane', ephemeral=True)



async def setup(bot):
    await bot.add_cog(queueCog(bot))
    print(f'Queue cog loaded')
    