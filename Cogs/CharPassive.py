import discord
from discord.ext import commands

class CharPassive(commands.Cog):
    def __init__(self, client):
        self.Bot = client

    @commands.command()
    async def p(self, ctx, cmd=None):
        if cmd is None:
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

            # await ctx.channel.send(embed=embed)
            await ctx.channel.send(embed=embed)
        if cmd == 'svb':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""""")
            embed.set_image(
                url="https://cdn1.bbcode0.com/uploads/2020/8/22/f4c23b6f3147e1b13af9142a873504d0-full.jpg")
            embed.set_author(name="Silver Bane", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'sbm':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""""")
            embed.set_image(
                url="https://cdn1.bbcode0.com/uploads/2020/8/22/ceb831d47b080fc757d3724e3ea60743-full.jpg")
            embed.set_author(name="Silver Batman", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'svbc':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""""")
            embed.set_image(
                url="https://cdn1.bbcode0.com/uploads/2020/8/22/2e8d0f935f23ee6ebc423ff05e1f9677-full.jpg")
            embed.set_author(name="Silver Black Canary", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'svcw':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""""")
            embed.set_image(
                url="")
            embed.set_author(name="Silver Catwoman", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'svc':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Cyborg:

    Regenerates 1% health per second while tagged out

    +2% health for the team""")
            embed.set_image(
                url="")
            embed.set_author(name="Silver Cyborg", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'sds':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Deadshot:

    +5% damage when far away

    +2% critical chance for the team""")
            embed.set_image(
                url="")
            embed.set_author(name="Silver Deadshot", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'akbm':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Wayne Tech
                                  Passive 2: Fear Multi-Takedown
                                  Passive 3: Freeflow Counter""")
            embed.set_image(
                url="https://cdn1.bbcode0.com/uploads/2020/8/23/d06af08af1466d318be0f13b21ae7e69-full.jpg")
            embed.set_author(name="Arkham Knight Batman", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'df':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""""")
            embed.set_image(
                url="https://cdn1.bbcode0.com/uploads/2020/8/22/d7ad391d4f32980bce72ef3e3b915f8d-full.jpg")
            embed.set_author(name="Silver Doctor Fate", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'svgg':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Gorilla Grodd:

    +10% damage below 40% health""")
            embed.set_image(
                url="")
            embed.set_author(name="Silver Gorilla Grodd", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'svga':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""""")
            embed.set_image(
                url="https://cdn1.bbcode0.com/uploads/2020/8/22/95ab0976a209ae21765afe0f5b7d65eb-full.jpg")
            embed.set_author(name="Silver Green Arrow", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'sgl':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""""")
            embed.set_image(
                url="https://cdn1.bbcode0.com/uploads/2020/8/22/6a509032edf4123b27cc98f0172e2860-full.jpg")
            embed.set_author(name="Silver Green Lantern", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'svhq':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Harley Quinn:

    +20% damage on her jump/rush/ranged/crouched attacks

    +2% attack for the team""")
            embed.set_image(
                url="")
            embed.set_author(name="Silver Harley Quinn", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'svr':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""""")
            embed.set_image(
                url="https://cdn1.bbcode0.com/uploads/2020/8/22/0373b29218ace52d030ca8eb01ffdd66-full.jpg")
            embed.set_author(name="Silver Robin", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'svsc':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Scarecrow:

    15% chance for enemy tag outs to be stopped and the enemy to be stunned for 1 second""")
            embed.set_image(
                url="")
            embed.set_author(name="Silver Scarecrow", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'ssm':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""""")
            embed.set_image(
                url="https://cdn1.bbcode0.com/uploads/2020/8/22/f9af214e7cdc0b0c73a4a494ddec3e8b-full.jpg")
            embed.set_author(name="Silver Superman", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'svst':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Swamp Thing:

    Heals 51 hp over time when an ability is used""")
            embed.set_image(
                url="")
            embed.set_author(name="Silver Swamp Thing", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'svf':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""""")
            embed.set_image(
                url="https://cdn1.bbcode0.com/uploads/2020/8/22/e00b618d29520ec125232560ab1bdec9-full.jpg")
            embed.set_author(name="Silver Flash", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'svj':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""The Joker:

    When defeated, his team gains 1 bar and the opponent is stunned for 5 seconds""")
            embed.set_image(
                url="")
            embed.set_author(name="Silver Joker", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'svww':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Wonder Woman:

    +10% Feminist Damage when fighting an oppresive male harasser

    +4% Attack for the team""")
            embed.set_image(
                url="")
            embed.set_author(name="Silver Wonder Woman", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'aww':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Amazon Wonder Woman:

    Women in your roster gain +1% health""")
            embed.set_image(
                url="")
            embed.set_author(name="Amazon Wonder Woman", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'aaam':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: The Waterbearer""")
            embed.set_image(
                url="https://cdn1.bbcode0.com/uploads/2020/8/23/f16c01c6541021efbb5bc0a2526c01db-full.jpg")
            embed.set_author(name="Atlantean Armor Aquaman", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'aga':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Power Lock Arrow""")
            embed.set_image(
                url="https://cdn1.bbcode0.com/uploads/2020/8/23/52ff2a58d34b89f3e003a1a72ba14c5c-full.jpg")
            embed.set_author(name="Ace Green Arrow", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'asm':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Kryptonian Armor""")
            embed.set_image(
                url="https://cdn1.bbcode0.com/uploads/2020/8/23/0944d506ba573f5f05e21636d2efe473-full.jpg")
            embed.set_author(name="Armored Superman", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'ats':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Dex-Starr""")
            embed.set_image(
                url="https://cdn1.bbcode0.com/uploads/2020/8/23/b5f83267bbba354b67d0a2fbfddd667e-full.jpg")
            embed.set_author(name="Atrocitus", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'ba':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Power of Aton""")
            embed.set_image(
                url="https://cdn1.bbcode0.com/uploads/2020/8/23/fa2ec7c7715be63a58f316187bc5ed0c-full.jpg")
            embed.set_author(name="Black Adam", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'bb':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Power Blades""")
            embed.set_image(
                url="https://cdn1.bbcode0.com/uploads/2020/8/23/3ea3dad4c22d9e23e043dceae5dc7186-full.jpg")
            embed.set_author(name="Blue Beetle", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'bmr':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Perfect Son""")
            embed.set_image(
                url="https://cdn1.bbcode0.com/uploads/2020/8/23/45aba4a8028eb6ae66ddefc422f8151a-full.jpg")
            embed.set_author(name="Blade Master Robin", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'bnbm':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Aikido""")
            embed.set_image(
                url="https://cdn1.bbcode0.com/uploads/2020/8/23/868815f4355e470b1507c068f08b008c-full.jpg")
            embed.set_author(name="Batman Ninja Batman", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        if cmd == 'bnhq':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Ninja Sidekick""")
            embed.set_author(name="Batman Ninja Harley Quinn", url="https://discordapp.com")
            file = discord.File("./Images_Passive/bnhq1.jpg", filename="bnhq1.jpg")
            embed.set_image(url="attachment://bnhq1.jpg")
            await ctx.send(file=file, embed=embed)
        if cmd == 'bnlj':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Eternal Foe""")
            embed.set_author(name="Batman Ninja Lord Joker", url="https://discordapp.com")
            file = discord.File("./Images_Passive/bnlj1.jpg", filename="bnlj1.jpg")
            embed.set_image(url="attachment://bnlj1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'cc':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Absolute Zero""")
            embed.set_author(name="Captain Cold", url="https://discordapp.com")
            file = discord.File("./Images_Passive/cc1.jpg", filename="cc1.jpg")
            embed.set_image(url="attachment://cc1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'csm':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Titanic Strength""")
            embed.set_author(name="Classic Superman", url="https://discordapp.com")
            file = discord.File("./Images_Passive/csm1.jpg", filename="csm1.jpg")
            embed.set_image(url="attachment://csm1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'cth':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Claws of Death""")
            embed.set_author(name="Cheetah", url="https://discordapp.com")
            file = discord.File("./Images_Passive/cth1.jpg", filename="cth1.jpg")
            embed.set_image(url="attachment://cth1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'dsg':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Kryptonian Slam""")
            embed.set_author(name="Dark Supergirl", url="https://discordapp.com")
            file = discord.File("./Images_Passive/dsg1.jpg", filename="dsg1.jpg")
            embed.set_image(url="attachment://dsg1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'eb':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Antivenom""")
            embed.set_author(name="Enraged Bane", url="https://discordapp.com")
            file = discord.File("./Images_Passive/ebane1.jpg", filename="ebane1.jpg")
            embed.set_image(url="attachment://ebane1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'egl':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: For the Corps""")
            embed.set_author(name="Emerald Green Lantern", url="https://discordapp.com")
            file = discord.File("./Images_Passive/egl1.jpg", filename="egl1.jpg")
            embed.set_image(url="attachment://egl1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'esf':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Energy Absorption""")
            embed.set_author(name="Energized Starfire", url="https://discordapp.com")
            file = discord.File("./Images_Passive/esf1.jpg", filename="esf1.jpg")
            embed.set_image(url="attachment://esf1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'fpi':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Poison Vines""")
            embed.set_author(name="Flora Poison Ivy", url="https://discordapp.com")
            file = discord.File("./Images_Passive/fpi1.jpg", filename="fpi1.jpg")
            embed.set_image(url="attachment://fpi1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'fs':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: DoT (Damage Over Time) Resistance""")
            embed.set_author(name="Firestorm", url="https://discordapp.com")
            file = discord.File("./Images_Passive/fs1.jpg", filename="fs1.jpg")
            embed.set_image(url="attachment://fs1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'gd':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Circuit Breaker""")
            embed.set_author(name="Grid", url="https://discordapp.com")
            file = discord.File("./Images_Passive/grid1.jpg", filename="grid1.jpg")
            embed.set_image(url="attachment://grid1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'hb':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Box of Evil""")
            embed.set_author(name="HellBoy", url="https://discordapp.com")
            file = discord.File("./Images_Passive/hb1.jpg", filename="hb1.jpg")
            embed.set_image(url="attachment://hb1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'hsc':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Fear Aura""")
            embed.set_author(name="Horrific Scarecrow", url="https://discordapp.com")
            file = discord.File("./Images_Passive/hsc1.jpg", filename="hsc1.jpg")
            embed.set_image(url="attachment://hsc1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'jla':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Primordial Power""")
            embed.set_author(name="Justice League Aquaman", url="https://discordapp.com")
            file = discord.File("./Images_Passive/jla1.jpg", filename="jla1.jpg")
            embed.set_image(url="attachment://jla1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'jlb':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Tactical Batsuit""")
            embed.set_author(name="Justice League Batman", url="https://discordapp.com")
            file = discord.File("./Images_Passive/jlbm1.jpg", filename="jlbm1.jpg")
            embed.set_image(url="attachment://jlbm1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'jlc':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1:Cybernetic Body""")
            embed.set_author(name="Justice League Cyborg", url="https://discordapp.com")
            file = discord.File("./Images_Passive/jlc1.jpg", filename="jlc1.jpg")
            embed.set_image(url="attachment://jlc1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'jlf':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Hyperspeed Assault""")
            embed.set_author(name="Justice League Flash", url="https://discordapp.com")
            file = discord.File("./Images_Passive/jlf1.jpg", filename="jlf1.jpg")
            embed.set_image(url="attachment://jlf1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'jsgl':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Reinforced Constructs""")
            embed.set_author(name="John Stewart Green Lantern", url="https://discordapp.com")
            file = discord.File("./Images_Passive/jsgl1.jpg", filename="jsgl1.jpg")
            embed.set_image(url="attachment://jsgl1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'kbm':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Knightmare Ambush""")
            embed.set_author(name="Knightmare Batman", url="https://discordapp.com")
            file = discord.File("./Images_Passive/kbm1.jpg", filename="kbm1.jpg")
            embed.set_image(url="attachment://kbm1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'mtcw':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Finders Keepers""")
            embed.set_author(name="Master Thief Catwoman", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mtcw1.jpg", filename="mtcw1.jpg")
            embed.set_image(url="attachment://mtcw1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'mvba':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Overload""")
            embed.set_author(name="Multiverse Black Lightning", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mvba.jpg", filename="mvba.jpg")
            embed.set_image(url="attachment://mvba.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'mvcc':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Cold Barrier""")
            embed.set_author(name="Multiverse Captain Cold", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mvcc.jpg", filename="mvcc.jpg")
            embed.set_image(url="attachment://mvcc.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'mvsg':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Multiverse Tenacity""")
            embed.set_author(name="", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mvsg1.jpg", filename="mvsg1.jpg")
            embed.set_image(url="attachment://mvsg1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'mvwc':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Multiverse Weapon Master""")
            embed.set_author(name="Multiverse White Canary", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mvwc1.jpg", filename="mvwc1.jpg")
            embed.set_image(url="attachment://mvwc1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'mww':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: God Killer Sword""")
            embed.set_author(name="Mythic Wonder Woman", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mww1.jpg", filename="mww1.jpg")
            embed.set_image(url="attachment://mww1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'nw':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Staff of Grayson""")
            embed.set_author(name="Nightwing", url="https://discordapp.com")
            file = discord.File("./Images_Passive/nw1.jpg", filename="nw1.jpg")
            embed.set_image(url="attachment://nw1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'pbm':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Batwing Airstrike""")
            embed.set_author(name="Predator Batman", url="https://discordapp.com")
            file = discord.File("./Images_Passive/pbm1.jpg", filename="pbm1.jpg")
            embed.set_image(url="attachment://pbm1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'pg':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Solar Energy Absorption""")
            embed.set_author(name="Power Girl", url="https://discordapp.com")
            file = discord.File("./Images_Passive/pg1.jpg", filename="pg1.jpg")
            embed.set_image(url="attachment://pg1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'psg':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Powered Heat Vision""")
            embed.set_author(name="Powered Supergirl", url="https://discordapp.com")
            file = discord.File("./Images_Passive/psg1.jpg", filename="psg1.jpg")
            embed.set_image(url="attachment://psg1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'pst':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Force of Nature""")
            embed.set_author(name="Primal Swamp Thing", url="https://discordapp.com")
            file = discord.File("./Images_Passive/pst1.jpg", filename="pst1.jpg")
            embed.set_image(url="attachment://pst1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'rdn':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Chain Lighting""")
            embed.set_author(name="Raiden", url="https://discordapp.com")
            file = discord.File("./Images_Passive/rdn1.jpg", filename="rdn1.jpg")
            embed.set_image(url="attachment://rdn1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'rf':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Reverse Time""")
            embed.set_author(name="The Reverse Flash", url="https://discordapp.com")
            file = discord.File("./Images_Passive/rf1.jpg", filename="rf1.jpg")
            embed.set_image(url="attachment://rf1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'rh':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Time Extension""")
            embed.set_author(name="Redhood", url="https://discordapp.com")
            file = discord.File("./Images_Passive/rh1.jpg", filename="rh1.jpg")
            embed.set_image(url="attachment://rh1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'sb':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Torment's Grasp""")
            embed.set_author(name="Silver Banshee", url="https://discordapp.com")
            file = discord.File("./Images_Passive/sb1.jpg", filename="sb1.jpg")
            embed.set_image(url="attachment://sb1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'sbc':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Sonic Attack""")
            embed.set_author(name="Sonic Black Canary", url="https://discordapp.com")
            file = discord.File("./Images_Passive/sbc1.jpg", filename="sbc1.jpg")
            embed.set_image(url="attachment://sbc1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'ssdf':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Reversal of Fate""")
            embed.set_author(name="Soul Stealer Doctor Fate", url="https://discordapp.com")
            file = discord.File("./Images_Passive/ssdf1.jpg", filename="ssdf1.jpg")
            embed.set_image(url="attachment://ssdf1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'sff':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Lightning Reflexes""")
            embed.set_author(name="Speed Force Flash", url="https://discordapp.com")
            file = discord.File("./Images_Passive/ssf1.jpg", filename="ssf1.jpg")
            embed.set_image(url="attachment://ssf1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'sz':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Klone Kombatant""")
            embed.set_author(name="Sub-Zero", url="https://discordapp.com")
            file = discord.File("./Images_Passive/sz1.jpg", filename="sz1.jpg")
            embed.set_image(url="attachment://sz1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'tkgg':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Telekinesis""")
            embed.set_author(name="Telekinetic Gorilla Grodd", url="https://discordapp.com")
            file = discord.File("./Images_Passive/tgg1.jpg", filename="tgg1.jpg")
            embed.set_image(url="attachment://tgg1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'ubc':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Resurrection""")
            embed.set_author(name="Unbreakable Cyborg", url="https://discordapp.com")
            file = discord.File("./Images_Passive/ubc1.jpg", filename="ubc1.jpg")
            embed.set_image(url="attachment://ubc1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'uhq':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Psychotic Charm""")
            embed.set_author(name="Unhinged Harley Quinn", url="https://discordapp.com")
            file = discord.File("./Images_Passive/uhq1.jpg", filename="uhq1.jpg")
            embed.set_image(url="attachment://uhq1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'wqww':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Amazon Warriors""")
            embed.set_author(name="Warrior Queen Wonder Woman", url="https://discordapp.com")
            file = discord.File("./Images_Passive/wqww1.jpg", filename="wqww1.jpg")
            embed.set_image(url="attachment://wqww1.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'bm':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Open Wounds\nPassive 2: Revenge Mission\nPassive 3: Black Manta Suit""")
            embed.set_author(name="Black Manta", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/bm_full.jpg", filename="bm_full.jpg")
            embed.set_image(url="attachment://bm_full.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'bnc':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Force Field\nPassive 2: Living Metal\nPassive 3: 12th Level Intellect""")
            embed.set_author(name="Brainiac", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/bnc_full.jpg", filename="bnc_full.jpg")
            embed.set_image(url="attachment://bnc_full.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'bncw':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Blinding Strikes\nPassive 2: 9 Lives\nPassive 3: Are You Kitten Me?""")
            embed.set_author(name="Batman Ninja Catwoman", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/bncw_full.jpg", filename="bncw_full.jpg")
            embed.set_image(url="attachment://bncw_full.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'bngg':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Crippling Blow\nPassive 2: Dramatic Reversal\nPassive 3: Master Plan""")
            embed.set_author(name="Batman Ninja Gorilla Grodd", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/bngg_full.jpg", filename="bngg_full.jpg")
            embed.set_image(url="attachment://bngg_full.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'bnr':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Combo Kid\nPassive 2: Ninja Lethality\nPassive 3: Monkey Style Swordplay""")
            embed.set_author(name="Batman Ninja Robin", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/bnr_full.jpg", filename="bnr_full.jpg")
            embed.set_image(url="attachment://bnr_full.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'cbm':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Batman Inc.\nPassive 2: Classically Trained\nPassive 3: Power Seize""")
            embed.set_author(name="Classic Batman", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/cbm_full.jpg", filename="cbm_full.jpg")
            embed.set_image(url="attachment://cbm_full.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'ds':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Parademons\nPassive 2: Sacrifices Are Necessary\nPassive 3: Apokolips Bombardment""")
            embed.set_author(name="Darkseid", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/ds_full.jpg", filename="ds_full.jpg")
            embed.set_image(url="attachment://ds_full.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'epi':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Entangling Vines\nPassive 2: Toxins\nPassive 3: Regrowth""")
            embed.set_author(name="Entangling Poison Ivy", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/epi_full.jpg", filename="epi_full.jpg")
            embed.set_image(url="attachment://epi_full.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'hbhq':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: It's Not Me, It's You\nPassive 2: Let Your Guard Down\nPassive 3: Straight To The Heart""")
            embed.set_author(name="Heart Breaker Harley Quinn", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/hbhq_full.jpg", filename="hbhq_full.jpg")
            embed.set_image(url="attachment://hbhq_full.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'koaam':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Building Tsunami\nPassive 2: Ocean's Retribution\nPassive 3: Waters of Life""")
            embed.set_author(name="King of Atlantis Aquaman", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/koaam_full.jpg", filename="koaam_full.jpg")
            embed.set_image(url="attachment://koaam_full.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'llj':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Killing Joker\nPassive 2: Joker Venom\nPassive 3: Caught You Off Guard""")
            embed.set_author(name="Last Laugh Joker", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/llj_full.jpg", filename="llj_full.jpg")
            embed.set_image(url="attachment://llj_full.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'mvasg':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Multiverse Power\nPassive 2: Fueled By Might\nPassive 3: Interruption""")
            embed.set_author(name="Multiverse Armored Supergirl", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/mvasg_full.jpg", filename="mvasg_full.jpg")
            embed.set_image(url="attachment://mvasg_full.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'mvbw':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Tactical Strikes\nPassive 2: Tactical Rep\nPassive 3: Combat Focus""")
            embed.set_author(name="Multiverse Batwoman", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/mvbw_full.jpg", filename="mvbw_full.jpg")
            embed.set_image(url="attachment://mvbw_full.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'mvf':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Multiverse Critical\nPassive 2: Multiverse Haste\nPassive 3: S. T. A. R. LABS""")
            embed.set_author(name="Multiverse The Flash", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/mvf_full.jpg", filename="mvf_full.jpg")
            embed.set_image(url="attachment://mvf_full.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'mvga':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Multiverse Power Drain\nPassive 2: Multiverse Incendiaries\nPassive 3: Endurance Training""")
            embed.set_author(name="Multiverse Green Arrow", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/mvga_full.jpg", filename="mvga_full.jpg")
            embed.set_image(url="attachment://mvga_full.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'shz':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Courage of Achilles\nPassive 2: Retribution of Zeus\nPassive 3: Stamina of Atlas""")
            embed.set_author(name="Shazam", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/shz_full.jpg", filename="shz_full.jpg")
            embed.set_image(url="attachment://shz_full.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'ssds':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: Sniper\nPassive 2: Suppressive Fire\nPassive 3: Assassin""")
            embed.set_author(name="Suicide Squad Deadshot", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/ssds_full.jpg", filename="ssds_full.jpg")
            embed.set_image(url="attachment://ssds_full.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == 'sshq':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Passive 1: The Suicide Squad\nPassive 2: Psychoanalyze\nPassive 3: Twisted Love""")
            embed.set_author(name="Suicide Squad Harley Quinn", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/sshq_full.jpg", filename="sshq_full.jpg")
            embed.set_image(url="attachment://sshq_full.jpg")
            await ctx.channel.send(file=file, embed=embed)
        if cmd == '':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""""")
            embed.set_author(name="", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/.jpg", filename=".jpg")
            embed.set_image(url="attachment://.jpg")
            await ctx.channel.send(file=file, embed=embed)


def setup(client):
    client.add_cog(CharPassive(client))