import discord
from discord import app_commands
from discord.ext import commands
from discord.ext import tasks


import dotenv
import os
import time

#Loads file containing the environment variables with secrets
dotenv.load_dotenv()

#Sets the intents that the bot will subscribe to, to get events from
intents = discord.Intents.default()
#Sets seeing the message content to true
intents.message_content = True

#Creates a discord client instance
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def test(ctx, *args):
    arguments = ','.join(args)
    await ctx.send(f'{len(args)} arguments: {arguments}')

#Lookup guide for slash commands using discord.ext.commands
#@bot.command(name='help2',description='provides help to the user')
#async def help2(ctx, arg: str):
#    await ctx.send(f'Preparing the help function for the {arg} provided....')


#Code to run upon bot being ready and logged in and setup
@bot.event
async def on_ready():
    await bot.load_extension('modules.unlqueue.unlq')
    await bot.tree.sync(guild=None)
    print(f'We have logged in as {bot.user}')


#Code to run upon a message being recieved that the client can see.
#@bot.event
#async def on_message(message):
#    if message.author == bot.user:
#        return
    
#    if message.content.startswith('$hello'):
#        await message.channel.send('Hello!')



#Runs the client using the discord bot token saved in the env variable.
bot.run(os.getenv('DISCORD_TOKEN'))