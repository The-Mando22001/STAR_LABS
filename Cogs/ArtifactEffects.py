import discord
from discord.ext import commands
from random import choice

class ArtifactEffects(commands.Cog):
    def __init__(self, client):
        self.Bot = client

    @commands.command(name='ae', aliases=['arteff'])
    async def _ae(self, ctx):
        embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                              description="""""")
        embed.add_field(name="🥉Common", value="""```Resistance to Crit, Stuns, Dot - 15%
Attack - 145
DoT Damage - 11%
Power generation - 5%
Lethal Attack damage - 10%
Health - 1400
Damage for Special 1 - 15%
Damage for Special 2 - 15%
Damage for Special 3 - 15%```""")
        embed.add_field(name="🥈Rare", value="""```Resistance to Crit, Stuns, Dot - 35%
Attack - 285
DoT Damage - 22.50%
Power generation - 10%
Lethal Attack damage - 20%
Health - 2850
Damage for Special 1 - 30%
Damage for Special 2 - 30%
Damage for Special 3 - 30%```""")
        embed.add_field(name="🥇Epic", value="""```Resistance to Crit, Stuns, Dot - 75%
Attack - 570
DoT Damage - 45%
Power generation - 20%
Lethal Attack damage - 40%
Health - 5700
Damage for Special 1 - 60%
Damage for Special 2 - 60%
Damage for Special 3 - 60%```

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: Support server link - [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")

        embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
        embed.set_author(name="Artifact Effects", url="https://discordapp.com")
        file = discord.File("arteff.png", filename="arteff.png")
        embed.set_image(url="attachment://arteff.png")
        embed.set_thumbnail(url="")
        await ctx.channel.send(embed=embed, file=file)


def setup(client):
    client.add_cog(ArtifactEffects(client))