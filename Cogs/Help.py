import discord
from discord.ext import commands
from random import choice


class Help(commands.Cog):
    def __init__(self, client):
        self.Bot = client

    @commands.guild_only()
    @commands.command(name='invite')
    async def invite(self, ctx):
        print("Bot invite pressed")
        embed = discord.Embed(colour=discord.Colour(0xe01c38), url="https://discordapp.com",
                              description="Open this link in browser - [Invite the bot](https://discord.com/api/oauth2/authorize?client_id=742228161986691145&permissions=67624001&scope=bot)\nSupport server link - [Aftermath Server](https://discord.gg/FadZThM)")
        embed.set_author(name="Bot invite and support links", url="https://discordapp.com")
        embed.set_footer(
            text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422 | Passive info provided by SIGMA#5422, shadowofintent#1026")

        await ctx.channel.send(embed=embed)

    @commands.guild_only()
    @commands.command(name='help')
    async def _help(self, ctx, cmd: str = None):
        if cmd is None:
            print("No command. Hence, printing common help.")
            embed = discord.Embed(colour=discord.Colour(0x29a98e), url="https://discordapp.com",
                              description="Hello Player! This bot will guide you by providing details like character builds, gears and materials and so on..\n\nJust type ```i!help``` If you are stuck anywhere and I'll be here to help! 😎 ")

        # embed.set_image(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/5/5a/BlackManta.jpg")
            embed.set_thumbnail(
                url="https://www.injusticeonline.com/wp-content/uploads/2017/05/injustice-2-mobile-icon.jpg")
            embed.set_author(name="Help Command", icon_url="https://cdn.discordapp.com/embed/avatars/1.png")
            embed.add_field(name="Bot Invite",
                        value="If you really want me to help you out in your server, type ```i!invite``` to invite me into your server. I'll be there to help you and your friends 🥰. It also has link to support server.")
            embed.add_field(name="Prefix checking and changing",
                        value="If you want to check or change the prefix, then, you need to type:\n`i!prefix` to get the prefix, and\n`i!set_prefix` to set the prefix in the server.")
            embed.add_field(name="Character Abbreviations",
                        value="This will show the list of characters available in the game in the abbreviated form. If you want to know more, type, ```i!help chars```")
            embed.add_field(name="Character Builds",
                        value="This will provide the best character builds. To know more, type, ```i!help b```")
            embed.add_field(name="Character Passives",
                        value="There are passive abilities for characters which are unique for every character. To know more, type, ```i!help passive```")
            embed.add_field(name="Artifact Information",
                        value="This will show information about different artifacts available in the game. To know more, type, ```i!art```")
            embed.add_field(name="Team Synergy Information",
                            value="This will show the Team synergy information, which give boost to your characters in battle during team selection. To know more, type, ```i!syn```")
            embed.add_field(name="Upgrade Calculator",
                        value="You can type start and end of number of levels of any upgrade (gear, artifact, xp and sp) to calculate how much material or coins required. To know more, type, ```i!help calc```")
            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422 | Passive info provided by SIGMA#5422, shadowofintent#1026")
        # file = discord.File("./source.gif", filename="source.gif")
        # embed.set_image(url="attachment://source.gif")
            await ctx.channel.send(embed=embed)

        elif cmd == 'chars':
            print("Character Abbrev command")
            embed = discord.Embed(colour=discord.Colour(0xf79263), url="https://discordapp.com",
                                  description="To check the character abbreviation, you can type the following commands and it will show the respective list of characters.")

            embed.set_author(name="Character Abbreviation", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")

            embed.add_field(name="List of Gold Characters",
                            value="To get a list of Gold characters, type, ```i!chars gold``` to get the list.")
            embed.add_field(name="List of Silver Characters",
                            value="To get a list of Silver characters, type, ```i!chars silver``` to get the list.")
            embed.add_field(name="List of Legendary Characters",
                            value="To get a list of Legendary characters, type, ```i!chars legend``` to get the list.")
            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422 | Passive info provided by SIGMA#5422, shadowofintent#1026")
            await ctx.channel.send(embed=embed)

        elif cmd == 'b' or cmd == 'build':
            print("Character Build command")
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""Currently, only the character builds on those lists below, are available as of now. We will add other builds soon.""")
            embed.set_author(name="Build Commands", url="https://discordapp.com")
            embed.add_field(name="⚡DAMAGE DEALERS",
                            value="""```\nkoaam - King of Atlantis Aquaman\nmvasg - Multiverse Armored Supergirl\nhbhq - Heart Breaker Harley Quinn\nbncw - Batman Ninja Catwoman\nbngg - Batman Ninja Gorilla Grodd\nbm - Black Manta\nsbn - Silver Banshee\nllj - Last Laugh Joker\nba - Black Adam\nbnr - Batman Ninja Robin\nbnlj - Batman Ninja Lord Joker\njlf - Justice League Flash\njlc - Justice League Cyborg\ncsm - Classic Superman\nds - Darksied\nesf - Energized Starfire\nsshq - Suicide Squad Harley Quinn\nenc - Suicide Squad Enchantress\njlam - Justice League Aquaman\nsbm - Silver Batman```""")
            embed.add_field(name="👊COMBO BUILDERS and 💪TANKS",
                            value="""```\nhsc - Horrific Scarecrow\ngl - Silver Green Lantern\njsgl - John Stewart Green Lantern\natr - Atrocitus\npbm - Predator Batman\nepi - Entangling Poison Ivy\nmvtf - Multiverse the Flash\npst - Primal Swamp Thing\nrb - Silver Robin\nsm - Silver Superman\nakbm - Arkham Night Batman\nbrc - Brainiac\nszm - Shazam\nrf - Reverse Flash\nsdf - Silver Doctor Fate\npg - Power Girl\ngrid - Grid\nmvsg - Multiverse Supergirl\nrh - Redhood\nasm - Armored Superman\nbmr - Blade Master Robin```""")
            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            # file = discord.File("./Images_Passive/mto_passives/.jpg", filename=".jpg")
            embed.set_image(url="")
            # await ctx.channel.send(embed=embed)
            await ctx.channel.send(embed=embed)

        elif cmd == 'passive' or cmd == 'p':
            print("Character Passive command")
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="There are passives for each and every character, which get enabled during battle or at the start of the battle. To know the character's passive, type, ```i!p [character name]``` Where, we type the character's name without the brackets []. For Example, ```i!p jsgl```The following list of characters have their respective passives.")

            embed.set_author(name="Character Passives", url="https://discordapp.com",
                             icon_url="https://cdn.discordapp.com/embed/avatars/3.png")
            embed.add_field(name="List of Silver Characters",
                            value="```\nsgl  : Silver Green Lantern\nsbm  : Silver Batman\nssm  : Silver Superman \nsds  : Silver Deadshot\nsvf  : Silver Flash\nsvbc : Silver Black Canary\nsvb  : Silver Bane\nsvc  : Silver Cyborg\nsvr  : Silver Robin\nsvhq : Silver Harley Quinn\nsvga : Silver Green Arrow\nsvam : Silver Aquaman\nsvww : Silver Wonder Woman\nsvgg : Silver Gorilla Grodd\nsvj  : Silver Joker\nsvcw : Silver Catwoman\nsvsc : Silver Scarecrow\nsvst : Legendary Silver Swamp Thing\ndf   : Doctor Fate```")
            embed.add_field(name="List of Legendary Characters",
                            value="```\nbm   : Black manta\nbvs  : Bvs superman\nds   : Darkseid\nbngg : Batman Ninja Gorilla Grodd \nbnc  : Discount Braniac\nect  : Enchantress\nsshq : Suicide Squad Harley Quinn\nakbm : Arkham Knight Batman```")
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
            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422 | Passive info provided by SIGMA#5422, shadowofintent#1026")

            # await ctx.channel.send(embed=embed)
            await ctx.channel.send(embed=embed)

        elif cmd == 'calc':
            print("Calculator command")
            embed = discord.Embed(colour=discord.Colour(0xe01c38), url="https://discordapp.com",
                                  description="This command can be used to calculate gear, xp, artifact and sp upgrade costs")

            embed.set_author(name="Cost Calculator", url="https://discordapp.com",
                             icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
            embed.add_field(name="Gear Calculator",
                            value="The command will show amount of gear material required to upgrade 1 gear and 5 gears. To know more, type, ```i!gear [from] [to]```")
            embed.add_field(name="Sp Upgrade Calculator",
                            value="The command will show the amount of coins required to upgrade each sp move. To know more, type, ```i!sp [from] [to]```")
            embed.add_field(name="XP Upgrade Calculator",
                            value="The command will show amount of xp required to upgrade a character from one level to another. To know more, type, ```i!xp [from] [to]```")
            embed.add_field(name="Artifact Upgrade Calculator",
                            value="The command will show the amount of artifact material required to upgrade the artifacts. To know more, type, ```i!a [from] [to]```")
            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422 | Passive info provided by SIGMA#5422, shadowofintent#1026")

            # await ctx.channel.send(embed=embed)
            await ctx.channel.send(embed=embed)



        else:
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5), url="https://discordapp.com",
                                  description="You have typed a command which is not present in the command list, to know the help commands, type ```i!help```")
            embed.set_author(name="Something wrong..", url="https://discordapp.com")
            error = ['https://media.giphy.com/media/3oEjHERaTIdeuFQrXq/giphy.gif',
                     'https://media.giphy.com/media/3osxY9kuM2NGUfvThe/giphy.gif',
                     'https://media.giphy.com/media/8L0Pky6C83SzkzU55a/giphy.gif',
                     'https://media.giphy.com/media/fV1yHo8YyoKjzvMCKr/giphy.gif',
                     'https://media.giphy.com/media/TqiwHbFBaZ4ti/giphy.gif',
                     'https://media.giphy.com/media/ifdPjn6m4WyNlnXMTj/giphy.gif']
            embed.set_image(url=choice(error))
            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422 | Passive info provided by SIGMA#5422, shadowofintent#1026")

            await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))