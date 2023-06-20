import discord
from discord.ext import commands
import music

cogs = [music]

intents = discord.Intents.default()

intents.members = True


client = commands.Bot(command_prefix='-', intents = intents)

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run("BOT SECRET")