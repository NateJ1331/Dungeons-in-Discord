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
bot.run(TOKEN)