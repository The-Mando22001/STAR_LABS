import discord
from discord.ext import commands

class CharList(commands.Cog):
    def __init__(self, client):
        self.Bot = client

    @commands.command()
    async def chars(self, ctx, cmd=None):
        if cmd is None:
            embed = discord.Embed(colour=discord.Colour(0x60dcd5), url="https://discordapp.com",
                                  description="This command will show the full names of the abbrieviated names. Type, ```1. i!chars gold - for gold characters\n2. i!chars silver - for silver characters\n3. i!chars legend - for legendary characters```")

            embed.set_author(name="Character Abbrieviation", url="https://discordapp.com",
                             icon_url="https://cdn.discordapp.com/embed/avatars/0.png")

            await ctx.channel.send(embed=embed)
        if cmd == "gold":
            embed = discord.Embed(colour=discord.Colour(0x60dcd5), url="https://discordapp.com",
                                  description="")
            embed.add_field(name="List of Gold Characters (Justice League)",
                            value="```\njlc  : Justice League Cyborg\njlf  : Justice League Flash\njla  : Justice League Aquaman\njlb  : Justice League Batman\nmww  : Mythic Wonder Woman```")
            embed.add_field(name="List of Gold Characters (Green Lanterns)",
                            value="```\njsgl : John Stewart Green Lantern\negl  : Emeral Green Lantern\nats  : Atrocitus```")
            embed.add_field(name="List of Gold Characters (Multiverse)",
                            value="```\nmvf  : Multiverse Flash\nmvasg: Multiverse Armored SuperGirl\nmvbl : Multiverse Black Lightning\nmvga : Multiverse Green Arrow\nmvcc : Multiverse Captain Cold\nmvwc : Multiverse White Canary\nmvbw : Multiverse Batwoman\nmvsg : Multiverse Supergirl```")
            embed.add_field(name="List of Gold Characters (League of Anarchy)",
                            value="```\nllj  : Last Laugh Joker\nepi  : Entangling Poison Ivy\nhbhq : Heart Breaker Harley Quinn```")
            embed.add_field(name="List of Gold Characters (Batman Ninjas)",
                            value="```\nbnr  : Batman Ninja Robin\nbnbm : Batman Ninja Batman\nbnlj : Batman Ninja Lord Joker\nbncw : Batman Ninja Catwoman\nbnhq : Batman Ninja Harley Quinn```")
            embed.add_field(name="List of Gold Characters (Others Part 1)",
                            value="```\npbm  : Predator Batman\naww  : Amazon Wonder Woman\nhb   : Hellboy\nszm  : Shazam\nrdn  : Raiden \nrf   : Reverse Flash\nbb   : Blue Beetle\nkbm  : Knightmare Batman\nba   : Black Adam\nesf  : Energised StarFire \npg   : Power Girl\ndsg  : Dark Super Girl\nfpi  : Flora Poison Ivy\nhsc  : Horrific Scarecrow\nsff  : Speed force Flash\ngrid : Grid\naga  : Ace green arrow\nssdf : Soul Stealer Dr.Fate\nubc  : Unbreakable Cyborg\npst  : Primal Swamp Thing\ntkgg : Telekinetic Gorilla Grodd\nsz   : Subzero\nbmr  : Blade Master Robin\ncc   : Captain Cold\nuhq  : Unhinged Harley Quinn\nrh   : Redhood\npsg  : Powered Supergirl \nmds  : Marksman Deadshot\nfs   : Firestorm\ncth  : Cheetah\neb   : Enraged Bane\nmtcw : Masterthief Catwoman\ncbm  : Classic Batman\nsbc  : Sonic Black Canary\nsb   : Silver Banshee \nasm  : Armoured Superman\ncsm  : Classic Superman```")
            embed.add_field(name="List of Gold Characters (Others Part 2)",
                            value="```\naaam : Atlantean Armor Aquaman\nnw   : Nightwing\nwqww : Warrior Queen Wonder Woman```")
            embed.set_author(name="Character Abbrieviation Gold", url="https://discordapp.com",
                             icon_url="https://cdn.discordapp.com/embed/avatars/0.png")

            await ctx.channel.send(embed=embed)
        if cmd == "silver":
            embed = discord.Embed(colour=discord.Colour(0x6cf1ea), url="https://discordapp.com",
                                  description="```\nsgl  : Silver Green Lantern\nsbm  : Silver Batman\nssm  : Silver Superman \nsds  : Silver Deadshot\nsvf  : Silver Flash\nsvbc : Silver Black Canary\nsvb  : Silver Bane\nsvc  : Silver Cyborg\nsvr  : Silver Robin\nsvhq : Silver Harley Quinn\nsvga : Silver Green Arrow\nsvam : Silver Aquaman\nsvww : Silver Wonder Woman\nsvgg : Silver Gorilla Grodd\nsvj  : Silver Joker\nsvcw : Silver Catwoman\nsvsc : Silver Scarecrow\nsvst : Legendary Silver Swamp Thing\ndf   : Doctor Fate```")

            embed.set_author(name="Character Abbrieviation Silvers", url="https://discordapp.com",
                             icon_url="https://cdn.discordapp.com/embed/avatars/0.png")

            await ctx.channel.send(embed=embed)
        if cmd == "legend":
            embed = discord.Embed(colour=discord.Colour(0x6b7892), url="https://discordapp.com",
                                  description="```\nbm   : Black manta\nbvs  : Bvs superman\nds   : Darkseid\nbngg : Batman Ninja Gorilla Grodd \nbnc  : Discount Braniac\nect  : Enchantress\nsshq : Suicide Squad Harley Quinn\nakbm : Arkham Knight Batman```")

            embed.set_author(name="Character Abbrieviation Legendaries", url="https://discordapp.com",
                             icon_url="https://cdn.discordapp.com/embed/avatars/0.png")

            await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(CharList(client))