import discord
from discord.ext import commands

TOKEN = "ODgzMzQ2MjQ5NzAzNjQxMTI5.YTImTQ.akA3AMhYkxthzn_bmKz5VuhCtO4"

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    activity = discord.Game(name="youtube")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print("bot is ready.")

client.run(TOKEN)
