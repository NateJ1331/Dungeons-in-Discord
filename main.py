from discord.ext import commands
import discord
import os

path = os.getcwd()
parent = os.chdir('..')

with open(f"{parent}/token.txt") as file:
    token = file.read()

bot = commands.Bot(command_prefix = "!",intents=discord.Intents.all())
