import dbl
import discord
from discord.ext import commands, tasks

import asyncio


class TopGG(commands.Cog):
    """
    This example uses dblpy's webhook system.
    In order to run the webhook, at least webhook_port must be specified (number between 1024 and 49151).
    """

    def __init__(self, client):
        self.bot = client
        self.token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ijc0MjIyODE2MTk4NjY5MTE0NSIsImJvdCI6dHJ1ZSwiaWF0IjoxNjA0OTMwMjg5fQ.XLoBuUqtDFLCPXEOHpqyuEsootj66fTZXifllJxL00E'  # set this to your DBL token
        self.dblpy = dbl.DBLClient(self.bot, self.token)

    @commands.Cog.listener()
    async def on_guild_post():
        print("Server count posted successfully")

    @commands.Cog.listener()
    async def on_dbl_vote(self, data):
        print(f"Received an upvote:{data}")

    @commands.Cog.listener()
    async def on_dbl_test(self, data):
        """An event that is called whenever someone tests the webhook system for your bot on top.gg."""
        print(f"Received a test upvote:{data}")





def setup(client):
    client.add_cog(TopGG(client))