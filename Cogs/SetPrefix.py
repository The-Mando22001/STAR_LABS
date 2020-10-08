import discord
from discord.ext import commands
from Bot import *


class SetPrefix(commands.Cog):
    def __init__(self, bot):
        self.Bot = bot

    @commands.command(name='prefix')
    async def prefix(self, ctx):
        embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                              description=f"""The prefixes for this server are: {custom_prefixes.get(ctx.guild.id, default_prefixes)}""")
        embed.set_author(name="Prefix Command", url="https://discordapp.com")
        await ctx.channel.send(embed=embed)

    @commands.command(name='set_prefix')
    @commands.has_permissions(administrator=True, manage_channels=True, manage_guild=True, manage_messages=True,
                              manage_roles=True)
    async def set_prefix(self, ctx, *, cmd: str = None):
        if cmd is None:
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""I think you're missing a parameter.. To use this command properly, type, ```i!set_prefix [Prefix you want to add]```Example, ```i!set_prefix +```To know the default prefixes, type, ```i!prefix```""")
            embed.set_author(name="Set Prefix Command", url="https://discordapp.com")
            embed.set_image(url="https://media.giphy.com/media/3osxY9kuM2NGUfvThe/giphy.gif")
            await ctx.channel.send(embed=embed)
        else:
            custom_prefixes[ctx.guild.id] = cmd.split(" ") or default_prefixes
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description=f"Prefix set to {cmd}")
            embed.set_author(name="Set Prefix Command", url="https://discordapp.com")
            ok_gifs = ["https://media.giphy.com/media/111ebonMs90YLu/giphy.gif",
                       "https://media.giphy.com/media/tIeCLkB8geYtW/giphy.gif",
                       "https://media.giphy.com/media/sWWYgKVkOlL0c/giphy.gif",
                       "https://media.giphy.com/media/5DQdk5oZzNgGc/giphy.gif",
                       "https://media.giphy.com/media/l46C93LNM33JJ1SMw/giphy.gif",
                       "https://media.giphy.com/media/26uf0fVN7k4glSdBS/giphy.gif",
                       "https://media.giphy.com/media/KxiRwO7tqXCTDVKobo/giphy.gif",
                       "https://media.giphy.com/media/dBf4yjLVT9xOW6s9Vj/giphy.gif"]
            embed.set_image(url=choice(ok_gifs))
            await ctx.channel.send(embed=embed)

    @set_prefix.error
    async def prefix_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            bruh = ["What are you thinking?", "Are you out of your mind?", "Dude, you can't do that", "Bruhhh",
                    "Yare Yare (It means showing pity on you in Japanese)"]
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""You don't have the right permissions to change the prefix! Ask a moderator or admin to change it.""")
            embed.set_author(name=choice(bruh), url="https://discordapp.com")
            gifs = ["https://media.giphy.com/media/LyJ6KPlrFdKnK/giphy.gif",
                    "https://media.giphy.com/media/tJeGZumxDB01q/giphy.gif",
                    "https://media.giphy.com/media/xL7PDV9frcudO/giphy.gif",
                    "https://media.giphy.com/media/pPhyAv5t9V8djyRFJH/giphy.gif",
                    "https://media.giphy.com/media/3oFyDl7xbRgcAu8O8E/giphy.gif", "https://tenor.com/1ej5.gif"]
            embed.set_image(url=choice(gifs))
            await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(SetPrefix(bot))