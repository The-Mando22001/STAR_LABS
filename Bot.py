import os
#import dotenv
import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
'''Token Placed in another txt file
f = open('token.txt', 'r')
TOKEN = str(f.read()) '''
async def get_pre(bot, message):
        return ["i!", "I!", "|!"]  # or a list, ["pre1","pre2"]

#Setting prefix to the bot
client = commands.Bot(command_prefix=get_pre,case_insensitive=True)



#Removing Default Help Command
client.remove_command('help')

#Replies when ready
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,activity=discord.Game("type i!help"))
    print("bot is online")
    print(client.user)
    count=0
    for guild in client.guilds:
        count = count+1
        print(guild.name)
        print(guild.owner)
        print("\n")
    print(count)


'''Loading, Unloading Extensions or Cogs'''
@client.command()
async def load(ctx, extension):
    client.load_extension(f'Cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'Cogs.{extension}')


#Ping command
@client.command()
async def ping(ctx):
    await ctx.channel.send(f'Pong! {round(client.latency*1000)}ms')

@client.group(name="help", invoke_without_command=True)
async def help(ctx):
    print("No command. Hence, printing common help.")
    embed = discord.Embed(colour=discord.Colour(0x29a98e), url="https://discordapp.com",
                          description="Hello Player! This bot will guide you by providing details like character builds, gears and materials and so on..\n\nJust type ```i!help``` If you are stuck anywhere and I'll be here to help! 😎 ")

    #embed.set_image(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/5/5a/BlackManta.jpg")
    embed.set_thumbnail(url="https://www.injusticeonline.com/wp-content/uploads/2017/05/injustice-2-mobile-icon.jpg")
    embed.set_author(name="Help Command", icon_url="https://cdn.discordapp.com/embed/avatars/1.png")

    embed.add_field(name="Character Abbreviations",
                    value="This will show the list of characters available in the game in the abbreviated form. If you want to know more, type, ```i!help chars```")
    #embed.add_field(name="Character Build",
    #                value="This will provide the best character build. To know more, type, ```i!help build```")
    embed.add_field(name="Buffs",
                    value="There are specific buffs for each characters and there are different type of buffs. To know more, type, ```i!help buff```")
    embed.add_field(name="Synergy",
                    value="Synergy is where the characters will get additional boosts or bonus while they are in the team during battle. To know more, type, ```i!help syn```")
    embed.add_field(name="Character Passives",
                    value="There are passive abilities for characters which are unique for every character. To know more, type, ```i!help passive```")
    embed.add_field(name="Upgrade Calculator",
                    value="You can type start and end of number of levels of any upgrade (gear, artifact, xp and sp) to calculate how much material or coins required. To know more, type, ```i!help calc```")
    embed.set_footer(
        text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Passive info provided by SIGMA#5422, shadowofintent#1026")
    #file = discord.File("./source.gif", filename="source.gif")
    #embed.set_image(url="attachment://source.gif")
    await ctx.channel.send(embed=embed)

@help.command(name='chars')
async def chars(ctx):
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
        text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Passive info provided by SIGMA#5422, shadowofintent#1026")
    await ctx.channel.send(embed=embed)

@help.command(name='buff')
async def buff(ctx):
    print("Character Buffs command")
    embed = discord.Embed(colour=discord.Colour(0xe01c38), url="https://discordapp.com",
                          description="While choosing the characters before the battle, always choose characters which give buffs to the characters during the battle. There are several types of Buffs: ```1. Sp Buffs (Like MV, LOA, etc)\n2. Passive Buffs (KOAAM, etc)\n3. Tagin Buffs (ATS, RF, BNR, etc)\n4. Hazard Buffs``` Note: Tag in buffs should be paired with other tagin buffs for max advantage.")

    embed.set_author(name="Character Buffs", url="https://discordapp.com",
                     icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
    embed.add_field(name="Sp Buffs",
                    value="These buffs are enabled after selecting sp for few characters like mvasg, etc.")
    embed.add_field(name="Passive Buffs",
                    value="These buffs consists of def boost ,atk boost ,cac ,cad ,fac, fah ,lac ,lad dmg stacking etc.")
    embed.add_field(name="Tagin Buffs",
                    value="These buffs are power swap, lac, lad, combo increase,reflect shield etc.")
    embed.add_field(name="Hazard Buffs",
                    value="Hazard Buffs are the dmg dealt by traps like jsgl, egl sp1, mvbl sp2, aaam sp2, ats sp1,2, bnr banana peel, pbm sbm akbm sp2, epi sp2, ubc sp2 etc.")
    embed.set_footer(
        text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Passive info provided by SIGMA#5422, shadowofintent#1026")
    #await ctx.channel.send(embed=embed)
    await ctx.channel.send(embed=embed)

@help.command(name='syn')
async def syn(ctx):
    print("Character Synergy command")
    embed = discord.Embed(colour=discord.Colour(0x6b7892), url="https://discordapp.com",
                          description="The following list gives combination synergy bonus in battles.")

    embed.set_author(name="Team Character Combination Synergy", url="https://discordapp.com",
                     icon_url="https://cdn.discordapp.com/embed/avatars/2.png")

    embed.add_field(name="Mvasg+Mvf",
                    value="```NO CAC AND CAD on any of them!\n\n⚡️Mvf boosts 52% of team CAC. Which mean with the last gear @ g70 , your Cac on any of MVF teammates will be maxed to 75 without having any CAC on talents and gears.\n⚡️MVF also boosts 45% team CAD. \n\nSo while entering the match MVF & MVASG have 195% and 215% CAD respectively. With the use of 1 MVASG SP3, you’ll get +80% CAD along with +2% CAD with every combo hit increase.\n\nIndirectly you’ll reach 300% CAD after hitting 1 mvasg sp3 for every 35 seconds. ```")
    embed.add_field(name="Legendaries with Brnc",
                    value="```NO LAC on any teammates\n\nBrnc grants 150% of his lac to his purple teammates. If Brnc has 40% Lac on self, teammates will gain 60% (maxed out) LAC.\n\nIn order to avoid lethal hits for Bm in raids, i always suggest to use naked Brnc without Lac talents.```")
    embed.add_field(name="AKBM + agility and tech teammates",
                    value="```NO DEF required\n\nLvl 5 passive , Akbm grants 60% Def and 125% base health boost to self along with tech and Agility teammates. \n\nHence , Def is not needed anywhere.```")
    embed.add_field(name="BVS with JL and legendaries",
                    value="```NO DEF required\n\nLvl 6 passive , Bvs boosts 48% Def to JL and Purple teammates.\n\nHence , Def is not needed in this case as well.```")
    embed.add_field(name="Suicide Squad",
                    value="```No resist talents needed for healing\n\nEct passive = Heal upon resisting crit hit.\n\nSshq passive = 55% crit resist to ss team + she’s immune to crit herself.\n\nSS team also has base crit resist or 10-20% which’ll max out the crit resist to 70% eitherway.\n\nHence, you don’t need resist talents to heal.```")
    embed.add_field(name="SVAM + 2 Metahumans on the team",
                    value="```ONLY 35% Total def on the team.\n\nSvam grants 20% Def per meta teammate to the full team . Hence, it’s a must to use 2 meta teammate with SVAM.\n35% + 20% + 20%= 75% (Maxed out) Def.```")
    embed.set_footer(
        text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Passive info provided by SIGMA#5422, shadowofintent#1026")

    #await ctx.channel.send(embed=embed)
    await ctx.channel.send(embed=embed)

'''@help.command(name='build')
async def build(ctx):
    print("Character Build command")
    embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                          description="There are build configurations for each and every character. To know the character's best builds, type, ```i!build [character name]``` Where, we type the character's name without the brackets []. For Example, ```i!build jsgl```The following list of characters have their respective builds.")

    embed.set_author(name="Character Build", url="https://discordapp.com",
                     icon_url="https://cdn.discordapp.com/embed/avatars/3.png")

    embed.add_field(name="List of Silver Characters",
                    value="```\nsgl  : Silver Green Lantern\nsbm-hbhq : Silver Batman for Hbhq\nsbm  : Silver Batman\nssm  : Silver Superman \nsds  : Silver Deadshot\nsvf  : Silver Flash\nsvbc : Silver Black Canary\nsvb  : Silver Bane\nsvc  : Silver Cyborg\nsvr  : Silver Robin\nsvhq : Silver Harley Quinn\nsvga : Silver Green Arrow\nsvam : Silver Aquaman\nsvww : Silver Wonder Woman\nsvgg : Silver Gorilla Grodd\nsvj  : Silver Joker\nsvcw : Silver Catwoman\nsvsc : Silver Scarecrow\nsvst : Legendary Silver Swamp Thing\ndf   : Doctor Fate```")
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
                    value="```\npbm  : Predator Batman\npbm-sb   : Predator Batman for Sb\npbm-hbhq : Predator Batman for Hbhq\naww  : Amazon Wonder Woman\nhb   : Hellboy\nszm  : Shazam\nrdn  : Raiden \nrf   : Reverse Flash\nbb   : Blue Beetle\nkbm  : Knightmare Batman\nba   : Black Adam\nesf  : Energised StarFire \npg   : Power Girl\ndsg  : Dark Super Girl\nfpi  : Flora Poison Ivy\nhsc  : Horrific Scarecrow\nsff  : Speed force Flash\ngrid : Grid\naga  : Ace green arrow\nssdf : Soul Stealer Dr.Fate\nubc  : Unbreakable Cyborg\npst  : Primal Swamp Thing\ntkgg : Telekinetic Gorilla Grodd\nsz   : Subzero\nbmr  : Blade Master Robin\ncc   : Captain Cold\nuhq  : Unhinged Harley Quinn\nrh   : Redhood\npsg  : Powered Supergirl \nmds  : Marksman Deadshot\nfs   : Firestorm\ncth  : Cheetah\neb   : Enraged Bane\nmtcw : Masterthief Catwoman\ncbm  : Classic Batman\nsbc  : Sonic Black Canary\nsb   : Silver Banshee \nasm  : Armoured Superman\ncsm  : Classic Superman```")
    embed.add_field(name="List of Gold Characters (Others Part 2)",
                    value="```\naaam : Atlantean Armor Aquaman\nkoaam-p2 : KOAAM For Phase 2\nkoaam: KOAAM Crit build\nkoaam-hsc: KOAAM for boss Hsc\nnw   : Nightwing\nwqww : Warrior Queen Wonder Woman```")

    #await ctx.channel.send(embed=embed)
    await ctx.channel.send(embed=embed)'''

@help.command(name='passive')
async def passive(ctx):
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
        text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Passive info provided by SIGMA#5422, shadowofintent#1026")

    #await ctx.channel.send(embed=embed)
    await ctx.channel.send(embed=embed)

@help.command(name='calc')
async def calc(ctx):
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
                    value="The command will show the amount of artifact material required to upgrade the artifacts. To know more, type, ```i!art [from] [to]```")
    embed.set_footer(
        text="Made by Mando_The_Mercenary#9484 | Bot's Logo designed by ARCAS#0954 | Passive info provided by SIGMA#5422, shadowofintent#1026")

    #await ctx.channel.send(embed=embed)
    await ctx.channel.send(embed=embed)

for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'Cogs.{filename[:-3]}')

client.run(token)