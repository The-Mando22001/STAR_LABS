import discord
from discord.ext import commands
from random import choice

class RaidHelp(commands.Cog):
    def __init__(self, client):
        self.Bot = client

def setup(client):
    client.add_cog(RaidHelp(client))