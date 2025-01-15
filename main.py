import discord
import os
from dotenv import load_dotenv,dotenv_values
from discord.ext import commands

load_dotenv(".env")

TOKEN: str = os.getenv("TOKEN")
bot = commands.Bot(command_prefix = "!",intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Its Alive!!")

@bot.event
async def on_message(message):
    await bot.process_commands(message)    

@bot.command()
async def test(ctx):
    view = discord.ui.View()
    button = discord.ui.Button(label = "Click Me")
    view.add_item(button)

    await ctx.send(view=view)

bot.run(TOKEN)