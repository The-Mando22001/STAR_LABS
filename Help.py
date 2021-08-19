import discord
from discord.ext import commands
from random import choice
gifs = ["https://media.giphy.com/media/LyJ6KPlrFdKnK/giphy.gif",
                    "https://media.giphy.com/media/tJeGZumxDB01q/giphy.gif",
                    "https://media.giphy.com/media/xL7PDV9frcudO/giphy.gif",
                    "https://media.giphy.com/media/pPhyAv5t9V8djyRFJH/giphy.gif",
                    "https://media.giphy.com/media/3oFyDl7xbRgcAu8O8E/giphy.gif",
                    "https://media.giphy.com/media/l3V0H7bYv5Ml5TOfu/giphy.gif",
                    "https://media.giphy.com/media/l378rrt5tAawaCQ9i/giphy.gif",
                    "https://media.giphy.com/media/l41lXS5zVQYVwF3Xi/giphy.gif",
                    "https://media.giphy.com/media/3o7buckytFnpXail0Y/giphy.gif"]

bruh = ["What are you thinking?", "Are you out of your mind?", "Dude, you can't do that", "Bruhhh",
                    "Yare Yare (It means showing pity on you in Japanese)", "Seriously?!", "Nani?!!"]

class Help(commands.Cog):
    def __init__(self, client):
        self.Bot = client

    @commands.guild_only()
    @commands.command(name='vote', aliases=['v'])
    async def _vote(self, ctx):
        print(f"Bot vote pressed by {ctx.message.author.name}")
        embed = discord.Embed(colour=discord.Colour(0xe01c38), url="https://discordapp.com",
                              description="Please vote this bot. The bot's **main purpose** is to help those who require the necessary information. You can vote this bot for every **12 hours**. Open this link in a browser - [Vote the bot in top.gg](https://top.gg/bot/742228161986691145/vote)")
        embed.set_author(name="STAR LABS Vote", url="https://discordapp.com")
        embed.set_footer(
            text=f"Last used by: {ctx.message.author.name} | Check out the `credits` command to see the list of people who helped making this bot.")

        await ctx.channel.send(embed=embed)

    @commands.guild_only()
    @commands.command(name='patreon')
    async def _patreon(self, ctx):
        embed = discord.Embed(colour=discord.Colour(0xe01c38), url="https://discordapp.com",
                              description="""I have made a Patreon page for the bots that I make. Kindly check the website and the tiers. If you're interested in becoming a patron, I'll be very happy.

Kindly visit this website - [Patreon Page of Mandothemerc](https://www.patreon.com/mandothemerc)

Reason I have created a patreon account is: Motivation, Encouragement and Inspiration. If more of you people support and become patrons, the more I make the bots for everyone. Running a bot in a VPS costs money. Hence, if you're using the bot, please think of donating some money for the bot to run 24x7. I hope you guys understand.

- Mando_The_Mercenary

`This is The Way`""")
        embed.set_author(name="Patreon Support", url="https://discordapp.com")
        embed.set_footer(
            text=f"Last used by: {ctx.message.author.name} | Check out the `credits` command to see the list of people who helped making this bot.")

        await ctx.channel.send(embed=embed)

    @commands.guild_only()
    @commands.command(name='setup')
    @commands.has_permissions(manage_messages=True, manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    async def _setup(self, ctx):
        await ctx.channel.send("Setup started...")
        category = await ctx.guild.create_category("✨S. T. A. R. LABS✨", overwrites=None, reason=None)
        await ctx.guild.create_text_channel('📋character-abbreviations', category=category)
        await ctx.guild.create_text_channel('⚙build-commands', category=category)
        await ctx.guild.create_text_channel('⚙build-info', category=category)
        await ctx.guild.create_text_channel('⚡passive-commands', category=category)
        await ctx.guild.create_text_channel('⚡passive-info', category=category)
        await ctx.guild.create_text_channel('💎artifact-commands', category=category)
        await ctx.guild.create_text_channel('💎artifact-info', category=category)
        await ctx.guild.create_text_channel('⚔team-synergy-commands', category=category)
        await ctx.guild.create_text_channel('⚔team-synergy-info', category=category)
        await ctx.guild.create_text_channel('🧮calculator-commands', category=category)
        await ctx.guild.create_text_channel('🧮gear-calc', category=category)
        await ctx.guild.create_text_channel('🧮sp-calc', category=category)
        await ctx.guild.create_text_channel('🧮artifact-calc', category=category)
        await ctx.guild.create_text_channel('🧮xp-calc', category=category)
        await ctx.channel.send("Setup completed Successfully")

    @_setup.error
    async def setup_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5), url="https://discordapp.com",
                                  description="There is an error while using this command. Please check the following.")
            embed.set_author(name="Something wrong with Setup command..", url="https://discordapp.com")
            embed.add_field(name='S. T. A. R. LABS Missing Permissions', value="The bot **must** have `Manage Channels` permission to create category and channels.")
            embed.add_field(name="User Missing Permissions", value="The person who used this command **must** have `Manage Messages` **and** `Manage Channels` permissions to run this command.")
            error = ['https://media.giphy.com/media/3oEjHERaTIdeuFQrXq/giphy.gif',
                     'https://media.giphy.com/media/3osxY9kuM2NGUfvThe/giphy.gif',
                     'https://media.giphy.com/media/8L0Pky6C83SzkzU55a/giphy.gif',
                     'https://media.giphy.com/media/fV1yHo8YyoKjzvMCKr/giphy.gif',
                     'https://media.giphy.com/media/TqiwHbFBaZ4ti/giphy.gif',
                     'https://media.giphy.com/media/ifdPjn6m4WyNlnXMTj/giphy.gif']
            embed.set_image(url=choice(error))
            embed.set_footer(
                text=f"Last used by: {ctx.message.author.name} | Check out the `credits` command to see the list of people who helped making this bot.")
            await ctx.channel.send(embed=embed)



    @commands.guild_only()
    @commands.command(name='invite', aliases= ['i'])
    async def invite(self, ctx):
        print(f"Bot invite pressed by {ctx.message.author.name}")
        embed = discord.Embed(colour=discord.Colour(0xe01c38), url="https://discordapp.com",
                              description="Open this link in browser - [Invite the bot](https://discord.com/api/oauth2/authorize?client_id=742228161986691145&permissions=67492945&scope=bot)\nSupport server link - [Aftermath Server](https://discord.gg/bfbYNWE)")
        embed.set_author(name="Bot invite and support links", url="https://discordapp.com")
        embed.set_footer(
            text=f"Last used by: {ctx.message.author.name} | Check out the `credits` command to see the list of people who helped making this bot.")

        await ctx.channel.send(embed=embed)

    @commands.guild_only()
    @commands.command(name='about', aliases=['credits'])
    async def _about(self, ctx):
        print(f"About command Pressed by {ctx.message.author.name}")
        embed = discord.Embed(colour=discord.Colour(0x29a98e), url="https://discordapp.com",
                              description="This bot is made with love by me. This contains all the necessary info required for Injustice 2 Mobile Game. More commands and features are added soon. Many people have helped build this bot by providing info, suggestions and ideas. That is why I have made this command for honoring those who have helped me. I would like to thank each and everyone who have supported me while making this bot.\n\n- `Mando_The_Mercenary™#9484`")
        embed.set_author(name="Credits")
        embed.add_field(name="Bot's Logo Design",
                        value="`ARCAS#0954` is a great guy and makes Logo desgins for Discord Profile Pics. He made this logo desgin specially for the bot.")
        embed.add_field(name="Character Build Details",
                        value="`ʙᴏʀɴ2ᴋɪʟʟ™#4215` from `Destiny` and `[Δ₭] OVERMAN#0001` from `Apokolips Kingdom`, `Decebalus#7982` from `Rouge` have accepted to use the builds from their servers. `SIGMA#5422` and `YSOSERIOUS™#7777` has helped in designing the character Build template.")
        embed.add_field(name="Character Passive Details",
                        value="`SIGMA#5422` and `shadowofintent#1026` have helped me in adding the passive info. Both of them shared the screenshots of their characters, so that, it would be easy to see the picture than read the details.")
        embed.add_field(name="Honourable Mentions",
                        value="Many people use this bot everyday. But, with request of few people, they have helped this bot get to this stage. So, my special thanks to\n- `Decebalus#7982`: Build Suggestions\n- `Noremac#7255`: Bot Tester\n- `resveratrol#7110`: Suggestions\n- `The asian cat#3430`: Bot Tester\n- `SigvaldTheGrim#2431`: Youtuber who spoke about my bot\n- `AGB | Roids#0182`: The Aftermath Overlord who accepted to build this bot in Aftermath Server\n- `《ԙ》kreampuffs#1992`: Suggestions\n- `MattRyan#7598`: Bot Tester and Suggestions\n- `EthanHunt#2416`: Suggestions\n and many more..\n\n*This is the Way!*")
        file = discord.File("./STAR_LABS.jpg", filename="STAR_LABS.jpg")
        embed.set_thumbnail(url="attachment://STAR_LABS.jpg")
        await ctx.channel.send(embed=embed, file=file)

    @commands.guild_only()
    @commands.command(name='help', aliases= ['h'])
    async def _help(self, ctx, cmd: str = None):
        if cmd is None:
            print(f"No command. Hence, printing common help. - {ctx.message.author.name}")
            embed = discord.Embed(colour=discord.Colour(0x29a98e), url="https://discordapp.com",
                              description="Hello Player! This bot will guide you by providing details like character builds, gears and materials and so on..\n\nJust type `i!help` If you are stuck anywhere and I'll be here to help! 😎 ")

        # embed.set_image(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/5/5a/BlackManta.jpg")
            embed.set_thumbnail(
                url="https://www.injusticeonline.com/wp-content/uploads/2017/05/injustice-2-mobile-icon.jpg")
            embed.set_author(name="Help Command", icon_url="https://cdn.discordapp.com/embed/avatars/1.png")
            embed.add_field(name="Bot Statistics", value="To check the bot's statistics, type `i!stats` or `i!ss` or `i!serverstats`.")
            embed.add_field(name="Vote the bot", value="Please vote the bot using the link provided in the command `i!vote`.")
            embed.add_field(name="Bot Invite and support",
                        value="If you really want me to help you out in your server, type `i!invite` to invite me into your server. I'll be there to help you and your friends 🥰. It also has link to support server.")
            embed.add_field(name="Credits",
                            value="Check this out with `i!credits` or `i!about` to see the list of people who helped making this bot.")
            embed.add_field(name="Patreon Support", 
                        value="If you want me to support in Patreon, you can check the link the command `i!patreon`. Please do support my Sensei (Mando)!!")
            embed.add_field(name='Bot channels setup', value="If you want the bot to create the category and the respective channels for you, then you can type ```i!setup``` to create a category and corresponding channels in that category.")
            embed.add_field(name="Prefix checking and changing",
                        value="If you want to check or change the prefix, then, you need to type:\n`i!prefix` to get the prefix, and\n`i!set_prefix` to set the prefix in the server.")
            embed.add_field(name="Character Abbreviations",
                        value="This will show the list of characters available in the game in the abbreviated form. If you want to know more, type, `i!help chars`")
            embed.add_field(name="Character Builds",
                        value="This will provide the best character builds. To know more, type, `i!help b`")
            embed.add_field(name="Character Passives",
                        value="There are passive abilities for characters which are unique for every character. To know more, type, `i!help passive`")
            embed.add_field(name="Artifact Information",
                        value="This will show information about different artifacts available in the game. To know more, type, `i!art`")
            embed.add_field(name='Artifact Effect Information',
                            value='This will provide the reroll values for artifact talent. To know more, type `i!ae` or `i!arteff`')
            embed.add_field(name="Team Synergy Information",
                            value="This will show the Team synergy information, which give boost to your characters in battle during team selection. To know more, type, `i!syn`")
            embed.add_field(name="Upgrade Calculator",
                        value="You can type start and end of number of levels of any upgrade (gear, artifact, xp and sp) to calculate how much material or coins required. To know more, type, `i!help calc`")
            embed.set_footer(
                text=f"Last used by: {ctx.message.author.name} | Check out the `credits` command to see the list of people who helped making this bot.")
        # file = discord.File("./source.gif", filename="source.gif")
        # embed.set_image(url="attachment://source.gif")
            await ctx.channel.send(embed=embed)

        elif cmd == 'chars':
            print(f"Character Abbrev command by {ctx.message.author.name}")
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
                text=f"Last used by: {ctx.message.author.name} | Check out the `credits` command to see the list of people who helped making this bot.")
            await ctx.channel.send(embed=embed)

        elif cmd == 'b' or cmd == 'build':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""Here are the builds available in STAR LABS. We will add other builds soon. To use the command, type, ```i!b [character command]```If you wish to add your builds to this bot, you can DM `Mando_The_Mercenary™#9484`. He will mention you in the credits!!""")
            embed.set_author(name="Build Commands", url="https://discordapp.com")
            embed.add_field(name="🟪 Legendary Characters", value="""```akbm - Arkham Knight Batman
bm - Black Manta
bnc - Brainiac
bngg - Batman Ninja Gorilla Grodd
ds - Darkseid
jls - Justice League Superman
sshq - Suicide Squad Harley Quinn 
sse - Suicide Squad Enchantress
mmh - Martian Manhunter```""")
            embed.add_field(name="⬜ Silver Characters", value="""```aww - Amazon Wonder Woman
svbc - Sonic Black Canary
svcw - Silver Catwoman 
svam - Silver Aquaman 
svc - Silver Cyborg
svf - Silver Flash
svj - Silver Joker 
svhq - Silver Harley Quinn
svst - Silver Swamp Thing
svgg - Silver Gorilla Grodd
svb - Silver Bane
svds - Silver Deadshot
svsc - Silver Scarecrow
svr - Silver Robin
svdf - Silver Doctor Fate
svga - Silver Green Arrow
svww - Silver Wonder Woman 
svsm - Silver Superman
svgl - Silver Green Lantern
svbm - Silver Batman```""")
            embed.add_field(name="🟨 Gold Characters (Batman Ninjas)", value="""```bnbm - Batman Ninja Batman
bnhq - Batman Ninja Harley Quinn
bncw - Batman Ninja Catwoman
bnr - Batman Ninja Robin
bnlj - Batman Ninja Lord Joker```""")
            embed.add_field(name="🟨 Gold Characters (Multiverse Gang)", value="""```mvbw - Multiverse Bat Woman
mvf - Multiverse The Flash
mvbl - Multiverse Black Lightning
mvga - Multiverse Green Arrow 
mvwc - Multiverse White Canary
mvbw - Multiverse Batwoman
mvcc - Multiverse Captain Cold
mvsg - Multiverse Supergirl
mvasg - Multiverse Armored Supergirl```""")
            embed.add_field(name="🟨 Gold Characters (The Justice League)", value="""```jlc - Justice League Cyborg
jlf - Justice League Flash
jla - Justice League Aquaman
jlb - Justice League Batman
mww - Mythic Wonder woman```""")
            embed.add_field(name="🟨 Gold Characters (League of Anarchy)", value="""```epi - Entangling Poison Ivy
hbhq - Heart Breaker Harley Quinn
llj - Last Laugh Joker ```""")

            embed.add_field(name='🟨 Gold Characters (Others Part 1)', value="""```bb - Blue Beetle
asm - Armoured Superman
koaam - King of Atlantis Aquaman
sb - Silver Banshee
szm - Shazam
aaam - Atlantean Armored Aquaman
egl - Emerald Green Lantern
mtcw - Masterthief Catwoman
bmr - Blade Master Robin
atc - Atrocitus
ba - Black Adam
csm - Classic Superman 
dsg - Dark Super Girl
esf - Energized Starfire
fpi - Flora Poison Ivy 
hb - Hellboy
hsc - Horrific Scarecrow 
jsgl - John Stewart Green Lantern
kbm - Knightmare Batman
pg - Power Girl 
pbm - Predator Batman
rh - Red Hood
rf - Reverse Flash
sff - Speed Force the Flash
tkgg - TeleKinetic Gorilla Grodd 
wqww - Warrior Queen Wonder Woman 
rdn - Raiden
sz - Subzero
ssds - Suicide Squad Deadshot```""")
            embed.add_field(name='🟨 Gold Characters (Others Part 2)', value="""```grid - Grid
cbm - Classic Batman
eb - Enraged Bane
nw - Nightwing
psg - Powered Supergirl
cth - Cheetah
rdn - Raiden
ssdf - Soul Stealer Doctor Fate 
pst - Primal Swamp Thing
cc - Captain Cold
sbc - Sonic Black Canary
ubc - Unbreakable Cyborg
fs - Firestorm
uhq - Unhinged Harley Quinn```""")

            embed.set_footer(
                text=f"Last used by: {ctx.message.author.name} | Check out the `credits` command to see the list of people who helped making this bot.")
            embed.set_image(url="")
            await ctx.channel.send(embed=embed)

        elif cmd == 'passive' or cmd == 'p':
            print(f"Character Passive command by {ctx.message.author.name}")
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
                text=f"Last used by: {ctx.message.author.name} | Check out the `credits` command to see the list of people who helped making this bot.")

            # await ctx.channel.send(embed=embed)
            await ctx.channel.send(embed=embed)

        elif cmd == 'calc':
            print(f"Calculator command by {ctx.message.author.name}")
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
                text=f"Last used by: {ctx.message.author.name} | Check out the `credits` command to see the list of people who helped making this bot.")

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
                text=f"Last used by: {ctx.message.author.name} | Check out the `credits` command to see the list of people who helped making this bot.")

            await ctx.channel.send(embed=embed)

    @commands.command(name='hack')
    async def _hack(self, ctx):
        embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""You really think you could hack me??!!""")
        embed.set_author(name=choice(bruh), url="https://discordapp.com")
        embed.set_image(url=choice(gifs))
        embed.set_footer(text=f"{ctx.message.author.name} thinks he/ she could hack... jeez. Can someone explain him/ her that he can't hack into STAR LABS like this?")
        await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))