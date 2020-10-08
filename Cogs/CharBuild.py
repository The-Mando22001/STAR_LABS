import discord
from discord.ext import commands
from random import choice

class CharBuild(commands.Cog):
    def __init__(self, client):
        self.Bot = client

    @commands.command()
    async def b(self, ctx, cmd: str= None):
        if cmd is None:
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""Currently, only the character builds on those lists below, are available as of now. We will add other builds soon. To use the command, type, ```i!b [character command]```""")
            embed.set_author(name="Build Commands", url="https://discordapp.com")
            embed.add_field(name="⚡DAMAGE DEALERS", value="""```\nkoaam - King of Atlantis Aquaman\nmvasg - Multiverse Armored Supergirl\nhbhq - Heart Breaker Harley Quinn\nbncw - Batman Ninja Catwoman\nbngg - Batman Ninja Gorilla Grodd\nbm - Black Manta\nsbn - Silver Banshee\nllj - Last Laugh Joker\nba - Black Adam\nbnr - Batman Ninja Robin\nbnlj - Batman Ninja Lord Joker\njlf - Justice League Flash\njlc - Justice League Cyborg\ncsm - Classic Superman\nds - Darksied\nesf - Energized Starfire\nsshq - Suicide Squad Harley Quinn\nenc - Suicide Squad Enchantress\njlam - Justice League Aquaman\nsbm - Silver Batman\naaam - Atlantean Armor Aquaman\negl - Emerald Green Lantern\ncc - Captain Cold\nhb - Hellboy```""")
            embed.add_field(name="👊COMBO BUILDERS and 💪TANKS", value="""```\nhsc - Horrific Scarecrow\ngl - Silver Green Lantern\njsgl - John Stewart Green Lantern\natr - Atrocitus\npbm - Predator Batman\nepi - Entangling Poison Ivy\nmvtf - Multiverse the Flash\npst - Primal Swamp Thing\nrb - Silver Robin\nsm - Silver Superman\nakbm - Arkham Night Batman\nbrc - Brainiac\nszm - Shazam\nrf - Reverse Flash\nsdf - Silver Doctor Fate\npg - Power Girl\ngrid - Grid\nmvsg - Multiverse Supergirl\nrh - Redhood\nasm - Armored Superman\nbmr - Blade Master Robin\nsff  - Speedforce The Flash\ntgg  - Telekenetic Gorilla Grodd\nubc  - Unbreakable Cyborg```""")
            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            #file = discord.File("./Images_Passive/mto_passives/.jpg", filename=".jpg")
            embed.set_image(url="")
            await ctx.channel.send(embed=embed)
        elif cmd == 'akbm':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Build - G70]**""")
            embed.add_field(name="⚙STATS",value="""```ATTACK - 4956
HEALTH - 53712
DEFENSE - 24%
CAC - 61%
CAD - 271%
FAC - 69%
LAC - 1%
BLOCKING - 25%
STUN RESIST - 0%
DOT RESIST - 0%
CA RESIST - 0%```""")
            embed.add_field(name="⚙TALENTS", value="""```4 CAD, 2 CAC```""")
            embed.add_field(name="⚙GEARS", value="""```7 HEALTH, 4 FAC, 4 ATTACK```""")
            embed.set_author(name="Arkham Night Batman", url="https://discordapp.com")
            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/6/60/A500bc2231663fcea8e4ba20b32b0580.jpg/revision/latest/scale-to-width-down/310?cb=20181203181319")
            await ctx.channel.send(embed=embed)
        elif cmd == 'asm':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Tank Build - G60]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 2561
HEALTH - 56064
DEFENSE - 75%
CAC - 22%
CAD - 150%
FAC - 1%
LAC - 1%
STUN RESIST - 75%
DOT RESIST - 75%
CA RESIST - 70%```""")
            embed.add_field(name="⚙TALENTS", value="""```4 RESIST, 2 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```2 DEF, 13 HEALTH```""")

            embed.set_author(name="Armored Superman", url="https://discordapp.com")
            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/0/08/299cabb1b42743ad744177cd9ba7bb00.jpg/revision/latest/scale-to-width-down/220?cb=20190610155534")
            await ctx.channel.send(embed=embed)
        elif cmd == 'atr':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Combo Tank Build- G60]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 3647
HEALTH - 42016
DEFENSE - 75%
CAC - 22%
CAD - 150%
FAC - 75%
LAC - 10%
STUN RESIST - 40%
BLOCKING - 25%
DOT RESIST - 40%
CA RESIST - 40%
```""")
            embed.add_field(name="⚙TALENTS", value="""```2 RESIST, 4 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```7 HEALTH, 5 FAC, 3 ATTACK```""")

            embed.set_author(name="Atrocitus", url="https://discordapp.com")
            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/6/62/5818e2856e30f83a58be8f7795339ce0.jpg/revision/latest/scale-to-width-down/310?cb=20190610161328")
            await ctx.channel.send(embed=embed)
        elif cmd == 'ba':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 6106
HEALTH - 24234
DEFENSE - 65%
CAC - 75%
CAD - 300%
FAC - 1%
LAC - 10%
BLOCKING - 35%
STUN RESIST - 0%
DOT RESIST - 0%
CA RESIST - 0%```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAD , 3 DEF ```""")
            embed.add_field(name="⚙GEARS", value="""```10 ATTACK, 2 CAD, 3 CAC```""")

            embed.set_author(name="Black Adam", url="https://discordapp.com")
            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/f/ff/E987aeb3cd783a0d3e245dcc54d834c1.jpg/revision/latest/scale-to-width-down/220?cb=20190610163652")
            await ctx.channel.send(embed=embed)
        elif cmd == 'bm':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 5144
HEALTH - 26639
DEFENSE - 34%
CAC - 71%
CAD - 294%
FAC - 69%
LAC - 11%
STUN RESIST - 0%
DOT RESIST - 0%
CA RESIST - 0%
```""")
            embed.add_field(name="⚙TALENTS", value="""```4 AP, 1 CAD, 1 CAC```""")
            embed.add_field(name="⚙GEARS", value="""```6 ATTACK, 4 FAC, 3 CAD, 2 CAC```""")

            embed.set_author(name="Black Manta", url="https://discordapp.com")
            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/5/5a/BlackManta.jpg/revision/latest/scale-to-width-down/310?cb=20200614031132")
            await ctx.channel.send(embed=embed)
        elif cmd == 'bmr':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Combo Build Tank - G60]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 3175
HEALTH - 38300
DEFENSE - 75%
CAC - 22%
CAD - 150%
FAC - 71%
LAC - 13%
BLOCKING - 25%
STUN RESIST - 75%
DOT RESIST - 75%
CA RESIST - 70%```""")
            embed.add_field(name="⚙TALENTS", value="""```4 RESIST, 1 DEF, 1 LAC```""")
            embed.add_field(name="⚙GEARS", value="""```8 HEALTH, 4 FAC, 3 DEF```""")

            embed.set_author(name="Blade Master Robin", url="https://discordapp.com")
            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/c/ca/4e8737b1a3b4764d91a3377bb66aa183.jpg/revision/latest?cb=20190610160134")
            await ctx.channel.send(embed=embed)
        elif cmd == 'bncw':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build 1 - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 5636
HEALTH - 25252
DEFENSE - 29%
CAC - 75%
CAD - 300%
FAC - 62%
LAC - 13%
STUN RESIST - 5%
DOT RESIST - 0%
CA RESIST - 0%```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAD, 2 CAC, 1 LAC```""")
            embed.add_field(name="⚙GEARS", value="""```9 ATTACK, 3 FAC, 2 CAD, 1 CAC```""")
            #embed.add_field(name="", value="")
            embed.add_field(name="⚡[Damage Dealer Build 2 - G70]\n⚙STATS", value="""```ATTACK - 4766
HEALTH - 25252
DEFENSE - 29%
CAC - 75%
CAD - 300%
FAC - 62%
LAC - 60%
STUN RESIST - 5%
DOT RESIST - 0%
CA RESIST - 0%```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAD, 2 CAC, 1 LAC```""")
            embed.add_field(name="⚙GEARS", value="""```6 ATTACK, 3 FAC, 3 LAC, 2 CAD, 1 CAC```""")
            embed.set_author(name="Batman Ninja Catwoman", url="https://discordapp.com")
            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/1/14/7cf976bda697f8dab020ebfd0624ba34.jpg/revision/latest/scale-to-width-down/310?cb=20190610164254")
            await ctx.channel.send(embed=embed)
        elif cmd == 'bngg':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 4673
HEALTH - 33496
DEFENSE - 44%
CAC - 75%
CAD - 300%
FAC - 69%
LAC - 60%
STUN RESIST - 0%
DOT RESIST - 0%
CA RESIST - 0%```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAC, 3 CAD```""")
            embed.add_field(name="⚙GEARS", value="""```5 ATTACK, 4 FAC, 3 LAC, 2 CAD, 1 CAC```""")

            embed.set_author(name="Batman Ninja Gorilla Grodd", url="https://discordapp.com")
            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/b/b6/Batman_Ninja_Gorilla_Grodd.jpg/revision/latest?cb=20200201010324")
            await ctx.channel.send(embed=embed)
        elif cmd == 'bnlj':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 6291
HEALTH - 22660
DEFENSE - 24%
CAC - 73%
CAD - 298%
FAC - 1%
LAC - 60%
STUN RESIST - 0%
DOT RESIST - 15%
CA RESIST - 0%```""")
            embed.add_field(name="⚙TALENTS", value="""```4 CAC, 2 CAD```""")
            embed.add_field(name="⚙GEARS", value="""```10 ATTACK, 3 LAC, 2 CAD```""")

            embed.set_author(name="Batman Ninja Lord Joker", url="https://discordapp.com")
            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/c/c0/A4524a7097285ae487d030ba09a9c2e6.jpg/revision/latest/scale-to-width-down/220?cb=20190610172255")
            await ctx.channel.send(embed=embed)
        elif cmd == 'bnr':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build 1 - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 4716
HEALTH - 24196
DEFENSE - 29%
CAC - 71%
CAD - 300%
FAC - 62%
LAC - 59%
STUN RESIST - 0%
DOT RESIST - 0%
CA RESIST - 10%```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAD, 2 LAC, 1 CAC```""")
            embed.add_field(name="⚙GEARS", value="""```6 ATTACK, 3 FAC, 2 CAC, 2 CAD, 2 LAC```""")
            embed.add_field(name="⚡[Damage Dealer Build 2 - G70]\n⚙STATS", value="""```ATTACK - 5586
HEALTH - 24196
DEFENSE - 29%
CAC - 71%
CAD - 300%
FAC - 11%
LAC - 59%
STUN RESIST - 0%
DOT RESIST - 0%
CA RESIST - 10%```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAD, 2 LAC, 1 CAC```""")
            embed.add_field(name="⚙GEARS", value="""```9 ATTACK, 2 CAC, 2 CAD, 2 LAC```""")

            embed.set_author(name="Batman Ninja Robin", url="https://discordapp.com")
            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/4/4a/BMNR.jpg/revision/latest/scale-to-width-down/310?cb=20200613051247")
            await ctx.channel.send(embed=embed)
        elif cmd == 'brc':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Tank Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 3523
HEALTH - 58400
DEFENSE - 75%
CAC - 25%
CAD - 150%
FAC - 11%
LAC - 56%
STUN RESIST - 75%
DOT RESIST - 75%
CA RESIST - 70%```""")
            embed.add_field(name="⚙TALENTS", value="""```4 RESIST, 2 LAC```""")
            embed.add_field(name="⚙GEARS", value="""```11 HEALTH, 3 DEF, 1 LAC```""")

            embed.set_author(name="Brainiac", url="https://discordapp.com")
            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/0/0a/BrainiacMaxed.png/revision/latest/scale-to-width-down/310?cb=20200614031840")
            await ctx.channel.send(embed=embed)
        elif cmd == 'csm':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 6001
HEALTH - 21916
DEFENSE - 65%
CAC - 75%
CAD - 300%
FAC - 1%
LAC - 1%
STUN RESIST - 0%
DOT RESIST - 0%
CA RESIST - 10%```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAD, 3 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```10 ATTACK, 3 CAC, 2 CAD```""")

            embed.set_author(name="Classic Superman", url="https://discordapp.com")
            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/f/f9/ClassicSuperman.jpg/revision/latest/scale-to-width-down/310?cb=20200622233431")
            await ctx.channel.send(embed=embed)
        elif cmd == 'ds':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 6425
HEALTH - 33354
DEFENSE - 63%
CAC - 71%
CAD - 300%
FAC - 1%
LAC - 15%
STUN RESIST - 12%
DOT RESIST - 0%
CA RESIST - 0%```""")
            embed.add_field(name="⚙TALENTS", value="""```1 CAC, 3 CAD, 2 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```11 ATTACK, 2 CAD, 2 CAC```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Darksied", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/3/37/Boss_Darkseid.jpg/revision/latest/scale-to-width-down/310?cb=20200624181742")
            await ctx.channel.send(embed=embed)
        elif cmd == 'enc':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 6443
HEALTH - 26074
DEFENSE - 24%
CAC - 71%
CAD - 300%
FAC - 69%
LAC - 1%
STUN RESIST - 10%
DOT RESIST - 20%
CA RESIST - 20%```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAD, 3 CAC```""")
            embed.add_field(name="⚙GEARS", value="""```9 ATTACK, 4 FAC, 2 CAD
```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Suicide Squad Enchantress", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/b/bb/Enchantress.jpg/revision/latest/scale-to-width-down/310?cb=20200614015132")
            await ctx.channel.send(embed=embed)
        elif cmd == 'epi':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 3417
HEALTH - 30524
DEFENSE - 75%
CAC - 73%
CAD - 300%
FAC - 69%
LAC - 1%
STUN RESIST - 0%
DOT RESIST - 0%
CA RESIST - 20%```""")
            embed.add_field(name="⚙TALENTS", value="""```4 AP, 2 CAD```""")
            embed.add_field(name="⚙GEARS", value="""```4 FAC, 3 DEF, 3 CAD, 2 HEALTH, 2 CAC, 1 ATTACK```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Entangling Poison Ivy", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/9/9b/C919496c3adb4038b4b4b6a606a7e9d2.jpg/revision/latest/scale-to-width-down/310?cb=20190519152923")
            await ctx.channel.send(embed=embed)
        elif cmd == 'esf':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 5531
HEALTH - 17860
DEFENSE - 60%
CAC - 75%
CAD - 300%
FAC - 52%
LAC - 1%
BLOCKING - 25%
STUN RESIST - 0%
DOT RESIST - 0%
CA RESIST - 0%
```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAD , 3 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```7 ATTACK, 3 CAC, 2 CAD, 3 FAC```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Energized Starfire", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/7/7c/Energized_Starfire_60_Gear.png/revision/latest/scale-to-width-down/310?cb=20190509162955")
            await ctx.channel.send(embed=embed)
        elif cmd == 'gl':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Combo Build Tank - G60]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 2609
HEALTH - 38127
DEFENSE - 75%
CAC - 22%
CAD - 150%
FAC - 75%
LAC - 1%
STUN RESIST - 75%
BLOCKING - 25%
DOT RESIST - 75%
CA RESIST - 70%```""")
            embed.add_field(name="⚙TALENTS", value="""```4 RESIST, 2 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```8 HEALTH, 5 FAC, 2 DEF
```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Silver Green Lantern", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/8/83/Green_Lantern.jpg/revision/latest/scale-to-width-down/310?cb=20200621005135")
            await ctx.channel.send(embed=embed)
        elif cmd == 'grid':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Combo Build Tank - G60]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 3551
HEALTH - 36464
DEFENSE - 75%
CAC - 22%
CAD - 150%
FAC - 75%
LAC - 1%
BLOCKING - 25%
STUN RESIST - 75%
DOT RESIST - 75%
CA RESIST - 70%
```""")
            embed.add_field(name="⚙TALENTS", value="""```4 RESIST, 2 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```5 FAC, 2 DEF, 5 HEALTH, 3 ATTACK```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Grid", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/2/26/490111a84db03fa95d0efef925c2ccf6.jpg/revision/latest/scale-to-width-down/310?cb=20190610165702")
            await ctx.channel.send(embed=embed)
        elif cmd == 'hbhq':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 5121
HEALTH - 26896
DEFENSE - 24%
CAC - 75%
CAD - 300%
FAC - 66%
STUN RESIST - 0%
DOT RESIST - 0%
CA RESIST - 0%```""")
            embed.add_field(name="⚙TALENTS", value="""```4 AP, 2 CAC```""")
            embed.add_field(name="⚙GEARS", value="""```7 ATTACK, 4 CAD, 3 FAC, 1 CAC ```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Heart Breaker Harley Quinn", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/8/81/Maxresdefault_%281%29.jpg/revision/latest?cb=20190611164954")
            await ctx.channel.send(embed=embed)
        elif cmd == 'hsc':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Combo Build Tank - G60]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 3103
HEALTH - 40916
DEFENSE - 75%
CAC - 22%
CAD - 170%
FAC - 75%
LAC - 1%
BLOCKING - 25%
STUN RESIST - 75%
DOT RESIST - 75%
CA RESIST - 70%```""")
            embed.add_field(name="⚙TALENTS", value="""```4 RESIST, 2 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```8 HEALTH, 5 FAC, 2 DEF```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Horrific Scarecrow", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/7/7a/0af440f88c02441053d2cf6087a27660.jpg/revision/latest/scale-to-width-down/220?cb=20190610170756")
            await ctx.channel.send(embed=embed)
        elif cmd == 'jlam':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 5421
HEALTH - 22428
DEFENSE - 39%
CAC - 75%
CAD - 300%
FAC - 69%
LAC - 1%
STUN RESIST - 0%
DOT RESIST - 0%
CA RESIST - 0%
```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAC, 3 CAD```""")
            embed.add_field(name="⚙GEARS", value="""```8 ATTACK, 4 FAC, 1 CAC, 2 CAD```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Justice League Aquaman", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/7/74/Justice_League_Aquaman.png/revision/latest/scale-to-width-down/310?cb=20200613022703")
            await ctx.channel.send(embed=embed)
        elif cmd == 'jlc':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 4591
HEALTH - 23308
DEFENSE - 60%
CAC - 75%
CAD - 300%
FAC - 75%
LAC - 1%
STUN RESIST - 0%
DOT RESIST - 10%
CA RESIST - 0%```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAD, 3 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```4 FAC, 6 ATTACK, 2 CAD, 3 CAC```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Justice League Cyborg", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/5/58/959536899c5c0d826fe094bddb4285c6.jpg/revision/latest/scale-to-width-down/220?cb=20190610165131")
            await ctx.channel.send(embed=embed)
        elif cmd == 'jlf':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 5685
HEALTH - 22420
DEFENSE - 24%
CAC - 75%
CAD - 300%
FAC - 75%
LAC - 1%
STUN RESIST - 0%
DOT RESIST - 0%
CA RESIST - 0%```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAC, 3 CAD```""")
            embed.add_field(name="⚙GEARS", value="""```8 ATTACK, 4 FAC, 2 CAD, 1 CAC```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Justice League Flash", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/2/28/Ce3ada9874e05c01d1211d17cca313b3.jpg/revision/latest/scale-to-width-down/310?cb=20190610163529")
            await ctx.channel.send(embed=embed)
        elif cmd == 'jsgl':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Combo Build Tank - G60]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 2705
HEALTH - 45360
DEFENSE - 75%
CAC - 22%
CAD - 150%
FAC - 75%
LAC - 1%
BLOCKING - 25%
STUN RESIST - 60%
DOT RESIST - 60%
CA RESIST - 60%```""")
            embed.add_field(name="⚙TALENTS", value="""```3 RESIST, 3 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```5 FAC, 9 HEALTH ,1 DEF```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="John Stewart Green Lantern", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/6/62/678917fdb7e152bd9495b6e5bdfc1898.jpg/revision/latest/scale-to-width-down/310?cb=20190610171606")
            await ctx.channel.send(embed=embed)
        elif cmd == 'koaam':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**Damage Dealer**\n**[Crit Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 5632
HEALTH - 24580
DEFENSE - 44%
CAC - 75%
CAD - 300%
FAC - 69%
LAC - 1%
STUN RESIST - 0%
DOT RESIST - 0%
CA RESIST - 0%```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAC, 3 CAD```""")
            embed.add_field(name="⚙GEARS", value="""```8 ATTACK, 4 FAC, 2 CAD, 1 CAC```""")
            embed.add_field(name="[Non Crit Build - G70]\n⚙STATS", value="""```ATTACK - 6826
HEALTH - 24580
DEFENSE - 75%
CAC - 25%
CAD - 150%
FAC - 69%
LAC - 1%
STUN RESIST - 0%
DOT RESIST - 0%
CA RESIST - 0%```""")
            embed.add_field(name="⚙TALENTS", value="""```3 DEF, 3 ATTACK```""")
            embed.add_field(name="⚙GEARS", value="""```11 ATTACK, 4 FAC```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="King of Atlantis Aquaman", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/d/dd/KOAAM.jpg/revision/latest?cb=20200613222929")
            await ctx.channel.send(embed=embed)
        elif cmd == 'llj':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build 1 - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 5296
HEALTH - 23620
DEFENSE - 24%
CAC - 75%
CAD - 300%
FAC - 69%
LAC - 1%
STUN RESIST - 0%
DOT RESIST - 0%
CA RESIST - 15%```""")
            embed.add_field(name="⚙TALENTS", value="""```4 AP, 1 CAD, 1 CAC```""")
            embed.add_field(name="⚙GEARS", value="""```6 ATTACK, 4 FAC, 3 CAD, 2 CAC```""")
            embed.add_field(name="⚡[Damage Dealer Build 2 - G70]\n⚙STATS", value="""```ATTACK - 6167
HEALTH - 23620		
DEFENSE - 24%
CAC - 75%		
CAD - 298%	
FAC - 69%		
STUN RESIST - 0%		
DOT RESIST - 0%		
CA RESIST - 15%```""")
            embed.add_field(name="⚙TALENTS", value="""```2 CAD, 4 CAC```""")
            embed.add_field(name="⚙GEARS", value="""```9 ATTACK, 4 FAC, 2 CAD```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Last Laugh Joker", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/c/c7/Last_Laugh_The_Joker_60_Gear.jpg/revision/latest/scale-to-width-down/220?cb=20190509165527")
            await ctx.channel.send(embed=embed)
        elif cmd == 'mvasg':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 7578
HEALTH - 26308
DEFENSE - 65%
CAC - 25%
CAD - 170%
FAC - 1%
LAC - 1%
STUN RESIST - 60%
DOT RESIST - 70%
CA RESIST - 70%```""")
            embed.add_field(name="⚙TALENTS", value="""```3 RESIST, 3 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```15 ATTACK```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Multiverse Armored Supergirl", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/b/b7/Images.jpg/revision/latest?cb=20181130173657")
            await ctx.channel.send(embed=embed)
        elif cmd == 'mvsg':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Combo Build Tank - G60]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 3627
HEALTH - 40696
DEFENSE - 75%
CAC - 22%
CAD - 170%
FAC - 75%
LAC - 1%
BLOCKING - 25%
STUN RESIST - 60%
DOT RESIST - 60%
CA RESIST - 60%```""")
            embed.add_field(name="⚙TALENTS", value="""```3 RESIST, 3 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```5 FAC, 7 HEALTH ,1 DEF, 2 ATTACK```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Mutiverse Supergirl", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/5/56/Eyn2l8q2ioo11.jpg/revision/latest/scale-to-width-down/220?cb=20190610171858")
            await ctx.channel.send(embed=embed)
        elif cmd == 'mvtf':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Combo Build Tank - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 4630
HEALTH - 40828
DEFENSE - 75%
CAC - 25%
CAD - 150%
FAC - 75%
LAC - 1%
STUN RESIST - 60%
DOT RESIST - 60%
CA RESIST - 60%```""")
            embed.add_field(name="⚙TALENTS", value="""```3 RESIST, 3 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```4 FAC, 6 HEALTH, 4 ATTACK, 1 DEF```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Multiverse The Flash", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/3/3e/DPqIqKHUQAYTcXj.jpg/revision/latest/scale-to-width-down/220?cb=20181203155138")
            await ctx.channel.send(embed=embed)
        elif cmd == 'pbm':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Combo Build Tank - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 3312
HEALTH - 50412
DEFENSE - 75%
CAC - 59%
CAD - 174%
FAC - 69%
LAC - 1%
STUN RESIST - 0%
DOT RESIST - 0%
CA RESIST - 0%
```""")
            embed.add_field(name="⚙TALENTS", value="""```3 DEF, 1 CAD, 2 CAC```""")
            embed.add_field(name="⚙GEARS", value="""```10 HEALTH, 4 FAC, 1 DEF```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Predator Batman", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/b/b6/E33623af5b0723c25218b7565517f708.jpg/revision/latest/scale-to-width-down/220?cb=20190502181600")
            await ctx.channel.send(embed=embed)
        elif cmd == 'pg':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Tank Build - G60]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 3262
HEALTH - 54424
DEFENSE - 75%
CAC - 32%
CAD - 150%
FAC - 1%
LAC - 1%
STUN RESIST - 75%
DOT RESIST - 75%
CA RESIST - 70%```""")
            embed.add_field(name="⚙TALENTS", value="""```2 DEF, 4 RESIST```""")
            embed.add_field(name="⚙GEARS", value="""```13 HEALTH, 2 DEF```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Power Girl", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/e/ef/753a98ab1fba8255d95e9e0a76fe7f11.jpg/revision/latest/scale-to-width-down/220?cb=20190610154655")
            await ctx.channel.send(embed=embed)
        elif cmd == 'pst':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Tank Build - G60]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 2465
HEALTH - 54808
DEFENSE - 75%
CAC - 22%
CAD - 150%
FAC - 1%
LAC - 1%
STUN RESIST - 75%
DOT RESIST - 75%
CA RESIST - 70%```""")
            embed.add_field(name="⚙TALENTS", value="""```4 RESIST, 2 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```13 HEALTH, 2 DEF```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Primal Swamp Thing", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/0/0d/Primal_Swamp_Thing_60_Gear.jpg/revision/latest/scale-to-width-down/310?cb=20190509165737")
            await ctx.channel.send(embed=embed)
        elif cmd == 'rb':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Combo Build Tank - G60]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 2724
HEALTH - 38880
DEFENSE - 75%
CAC - 22%
CAD - 150%
FAC - 66%
LAC - 1%
STUN RESIST - 75%
BLOCKING - 25%
DOT RESIST - 75%
CA RESIST - 70%```""")
            embed.add_field(name="⚙TALENTS", value="""```4 RESIST, 2 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```9 HEALTH, 4 FAC, 2 DEF```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Silver Robin", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/9/9b/35370321bc8d0a926351100146fd5e37.jpg/revision/latest/scale-to-width-down/220?cb=20190610170548")
            await ctx.channel.send(embed=embed)
        elif cmd == 'rf':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Combo Build Tank - G60]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 3473
HEALTH - 43416
DEFENSE - 75%
CAC - 22%
CAD - 150%
FAC - 71%
LAC - 1%
STUN RESIST - 75%
DOT RESIST - 75%
CA RESIST - 70%```""")
            embed.add_field(name="⚙TALENTS", value="""```2 DEF, 4 RESIST```""")
            embed.add_field(name="⚙GEARS", value="""```9 HEALTH, 4 FAC, 2 DEF```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Reverse Flash", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/5/5c/ReverseFlash.jpg/revision/latest?cb=20200625134157")
            await ctx.channel.send(embed=embed)
        elif cmd == 'rh':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Tank Build - G60]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 3127
HEALTH - 55168
DEFENSE - 75%
CAC - 36%
CAD - 150%
FAC - 1%
LAC - 1%
STUN RESIST - 75%
DOT RESIST - 75%
CA RESIST - 70%```""")
            embed.add_field(name="⚙TALENTS", value="""```4 RESIST, 2 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```13 HEALTH, 2 DEF```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Red Hood", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/5/59/Red_Hood.jpg/revision/latest/scale-to-width-down/310?cb=20200613224051")
            await ctx.channel.send(embed=embed)
        elif cmd == 'sbm':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 6095
HEALTH - 17284
DEFENSE - 24%
CAC - 59%
CAD - 300%
FAC - 1%
LAC - 1%
STUN RESIST - 0%
DOT RESIST - 0%
CA RESIST - 0%```""")
            embed.add_field(name="⚙TALENTS", value="""```1 CAC, 5 CAD```""")
            embed.add_field(name="⚙GEARS", value="""```13 ATTACK, 1 CAC, 1 CAD```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Silver Batman", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/c/c0/1769da60219d4b3dac82ab816a848f61.jpg/revision/latest/scale-to-width-down/310?cb=20190610163122")
            await ctx.channel.send(embed=embed)
        elif cmd == 'sbn':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 6456
HEALTH - 16130
DEFENSE - 75%
CAC - 75%
CAD - 300%
FAC - 10%
LAC - 1%
STUN RESIST - 0%
DOT RESIST - 0%
CA RESIST - 10%```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAC, 3 CAD```""")
            embed.add_field(name="⚙GEARS", value="""```12 ATTACK, 2 CAD, 1 CAC```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Silver Banshee", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/e/e4/0c91d8e9d1c35d30b737b051203e9dad.jpg/revision/latest?cb=20190610160400")
            await ctx.channel.send(embed=embed)
        elif cmd == 'sdf':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Combo Build Tank - G60]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 2502
HEALTH - 37186
DEFENSE - 75%
CAC - 22%
CAD - 150%
FAC - 75%
LAC - 1%
STUN RESIST - 75%
DOT RESIST - 75%
CA RESIST - 70%```""")
            embed.add_field(name="⚙TALENTS", value="""```2 DEF, 4 RESIST```""")
            embed.add_field(name="⚙GEARS", value="""```8 HEALTH, 5 FAC, 2 DEF```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Silver Doctor Fate", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/1/1d/Ee5d7fd818dd22a7ebdb3adf26402392.jpg/revision/latest/scale-to-width-down/310?cb=20190610161144")
            await ctx.channel.send(embed=embed)
        elif cmd == 'sff':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Combo Build Tank - G60]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 3156
HEALTH - 45896
DEFENSE - 75%
CAC - 22%
CAD - 150%
FAC - 41%
LAC - 1%
BLOCKING - 25%
STUN RESIST - 75%
DOT RESIST - 75%
CA RESIST - 70%```""")
            embed.add_field(name="⚙TALENTS", value="""```2 DEF, 4 RESIST```""")
            embed.add_field(name="⚙GEARS", value="""```2 FAC, 2 DEF, 11 HEALTH```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Speed Force Flash", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/e/ea/Download-1-1.jpg/revision/latest?cb=20190521180131")
            await ctx.channel.send(embed=embed)
        elif cmd == 'sm':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Combo Build Tank - G60]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 2225
HEALTH - 39202
DEFENSE - 75%
CAC - 22%
CAD - 150%
FAC - 75%
LAC - 1%
STUN RESIST - 75%
BLOCKING - 25%
DOT RESIST - 75%
CA RESIST - 70%```""")
            embed.add_field(name="⚙TALENTS", value="""```4 RESIST, 2 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```8 HEALTH, 5 FAC, 2 DEF```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Silver Superman", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/1/1d/C02916b06a50ea58bc0252c330b62268.jpg/revision/latest/scale-to-width-down/220?cb=20190610160040")
            await ctx.channel.send(embed=embed)
        elif cmd == 'sshq':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 5724
HEALTH - 28324
DEFENSE - 44%
CAC - 75%
CAD - 300%
FAC - 69%
LAC - 11%
STUN RESIST - 0%
DOT RESIST - 0%
CA RESIST - 0%
```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAD, 3 CAC```""")
            embed.add_field(name="⚙GEARS", value="""```8 ATTACK, 4 FAC, 2 CAD, 1 CAC```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Suicide Squad Harley Quinn", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/a/a2/SSHarley.png/revision/latest/scale-to-width-down/310?cb=20200614030224")
            await ctx.channel.send(embed=embed)
        elif cmd == 'shz' or cmd == 'szm':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Combo Build Tank - G60]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 3041
HEALTH - 44948
DEFENSE - 75%
CAC - 22%
CAD - 150%
FAC - 75%
LAC - 1%
BLOCKING - 25%
STUN RESIST - 75%
DOT RESIST - 75%
CA RESIST - 70%```""")
            embed.add_field(name="⚙TALENTS", value="""```4 RESIST, 2 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```5 FAC, 8 HEALTH ,2 DEF```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Shazam", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/c/c9/ShazamHR.jpg/revision/latest/scale-to-width-down/310?cb=20200613032105")
            await ctx.channel.send(embed=embed)
        elif cmd == 'tgg':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Combo Build Tank - G60]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 2513
HEALTH - 42600
DEFENSE - 75%
CAC - 22%
CAD - 150%
FAC - 75%
LAC - 1%
STUN RESIST - 60%
BLOCKING - 25%
DOT RESIST - 60%
CA RESIST - 60%```""")
            embed.add_field(name="⚙TALENTS", value="""```3 DEF, 3 RESIST```""")
            embed.add_field(name="⚙GEARS", value="""```9 HEALTH, 5 FAC, 1 DEF```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Telekinetic Gorilla Grodd", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/8/8a/837dbeb890056d15220a5a88f8313935.jpg/revision/latest/scale-to-width-down/310?cb=20190610171200")
            await ctx.channel.send(embed=embed)
        elif cmd == 'aaam':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 5712
HEALTH - 21028
DEFENSE - 58%
CAC - 75%
CAD - 294%
FAC - 1%
LAC - 1%
STUN RESIST - 0%
DOT RESIST - 0%
CA RESIST - 0%```""")
            embed.add_field(name="⚙TALENTS", value="""```2 DEF, 1 CAD, 3 CAC```""")
            embed.add_field(name="⚙GEARS", value="""```11 ATTACK, 3 CAD, 1 CAC```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Atlantean Armor Aquaman", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/1/15/DoDmTmLV4AEjaXg.jpg/revision/latest?cb=20190610154346")
            await ctx.channel.send(embed=embed)
        elif cmd == 'egl':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 5463
HEALTH - 21652
DEFENSE - 60%
CAC - 75%
CAD - 300%
FAC - 1%
LAC - 1%
STUN RESIST - 0%
DOT RESIST - 0%
CA RESIST - 0%```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAD, 3 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```10 ATTACK, 3 CAC, 2 CAD```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Emerald Green Lantern", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/b/bd/Emerald_GL.png/revision/latest?cb=20200625174648")
            await ctx.channel.send(embed=embed)
        elif cmd == 'cc':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 6236
HEALTH - 19828
DEFENSE - 60%
CAC - 75%
CAD - 300%
FAC - 11%
LAC - 1%
STUN RESIST - 0%
DOT RESIST - 0%
CA RESIST - 0%```""")
            embed.add_field(name="⚙TALENTS", value="""```3 DEF, 3 CAD```""")
            embed.add_field(name="⚙GEARS", value="""```10 ATTACK, 3 CAC, 2 CAD```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Captain Cold", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/e/ee/Captain_Cold.jpg/revision/latest/scale-to-width-down/310?cb=20200614032201")
            await ctx.channel.send(embed=embed)
        elif cmd == "hb":
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 6027
HEALTH - 23428
DEFENSE - 63%
CAC - 73%
CAD - 294%
FAC - 1%
LAC - 1%
STUN RESIST -10%
DOT RESIST - 0%
CA RESIST - 0%```""")
            embed.add_field(name="⚙TALENTS", value="""```1 CAD, 4 CAC, 1 DEF ```""")
            embed.add_field(name="⚙GEARS", value="""```11 ATTACK, 3 CAD, 1 DEF```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Hell Boy", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/f/f1/Hellboy_INJ2_Mobile.jpg/revision/latest/scale-to-width-down/310?cb=20190320043838")
            await ctx.channel.send(embed=embed)
        elif cmd == 'sff':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Combo Build Tank - G60]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 3156
HEALTH - 45896
DEFENSE - 75%
CAC - 22%
CAD - 150%
FAC - 41%
LAC - 1%
BLOCKING - 25%
STUN RESIST - 75%
DOT RESIST - 75%
CA RESIST - 70%```""")
            embed.add_field(name="⚙TALENTS", value="""```2 DEF, 4 RESIST```""")
            embed.add_field(name="⚙GEARS", value="""```2 FAC, 2 DEF, 11 HEALTH```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Speed Force the Flash", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/e/ea/Download-1-1.jpg/revision/latest?cb=20190521180131")
            await ctx.channel.send(embed=embed)
        elif cmd == 'ubc':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Combo Build Tank - G60]**""")
            embed.add_field(name="⚙STATS", value="""```ATTACK - 2657
HEALTH - 39548
DEFENSE - 75%
CAC - 22%
CAD - 150%
FAC - 75%
LAC - 1%
BLOCKING - 25%
STUN RESIST - 70%
DOT RESIST - 60%
CA RESIST - 60%```""")
            embed.add_field(name="⚙TALENTS", value="""```3 DEF, 3 RESIST```""")
            embed.add_field(name="⚙GEARS", value="""```8 HEALTH, 5 FAC, 2 DEF```""")

            embed.set_footer(
                text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Builds Made by SIGMA#5422")

            embed.set_author(name="Unbreakable Cyborg", url="https://discordapp.com")
            embed.set_thumbnail(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/b/b2/A7f3ab39e668d4ab50207e3ddafc23dd.jpg/revision/latest/scale-to-width-down/220?cb=20190610165444")
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5), url="https://discordapp.com",
                                  description="You have typed a command which is not present in the command list, to know the build commands, type ```i!b```")
            embed.set_author(name="Something wrong with Build command..", url="https://discordapp.com")
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
    client.add_cog(CharBuild(client))