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
                text=f"Requested by: {ctx.message.author.name}",icon_url=ctx.guild.icon_url)
        await ctx.channel.send(embed=embed)

    @commands.guild_only()
    @commands.command(name='donate')
    async def _patreon(self, ctx):
        embed = discord.Embed(colour=discord.Colour(0xe01c38), url="https://discordapp.com",
                              description="""I have made a Patreon page for the bots that I make. Kindly check the website and the tiers. If you're interested in becoming a patron, I'll be very happy.

Kindly visit this website - [Patreon Page of Mandothemerc](https://www.patreon.com/mandothemerc)

Reason I have created a patreon account is: Motivation, Encouragement and Inspiration. If more of you people support and become patrons, the more I make the bots for everyone. Running a bot in a VPS costs money. Hence, if you're using the bot, please think of donating some money for the bot to run 24x7. I hope you guys understand.

If you want to donate money through PayPal, then click this link - [@mandothemercenary](https://www.paypal.me/mandothemercenary)

- Mando_The_Mercenary

`This is The Way`""")
        embed.set_author(name="Bot Donation and Support", url="https://discordapp.com")
        embed.set_footer(
                text=f"Requested by: {ctx.message.author.name}",icon_url=ctx.guild.icon_url)
        await ctx.channel.send(embed=embed)

    @commands.guild_only()
    @commands.command(name='setup')
    @commands.has_permissions(manage_messages=True, manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    async def _setup(self, ctx):
        await ctx.channel.send("Setup started...")
        category = await ctx.guild.create_category("✨S. T. A. R. LABS✨", overwrites=None, reason=None)
        await ctx.guild.create_text_channel('⚙build-commands', category=category)
        await ctx.guild.create_text_channel('⚡passive-commands', category=category)
        await ctx.guild.create_text_channel('💎artifact-commands', category=category)
        await ctx.guild.create_text_channel('⚔team-synergy-commands', category=category)
        await ctx.guild.create_text_channel('🧮calculator-commands', category=category)
        await ctx.guild.create_text_channel('🧮gear-calc', category=category)
        await ctx.guild.create_text_channel('🧮sp-calc', category=category)
        await ctx.guild.create_text_channel('🧮artifact-calc', category=category)
        await ctx.guild.create_text_channel('🧮xp-calc', category=category)
        await ctx.channel.send("Setup completed Successfully. If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: Support server link - [S. T. A. R. LABS INJ2 Helper](https://discord.gg/S7MvBVh4Hy).")

    @_setup.error
    async def setup_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5), url="https://discordapp.com",
                                  description="There is an error while using this command. Please check the following.")
            embed.set_author(name="Something wrong with Setup command..", url="https://discordapp.com")
            embed.add_field(name='S. T. A. R. LABS Missing Permissions', value="The bot **must** have `Manage Channels` permission to create category and channels.")
            embed.add_field(name="User Missing Permissions", value="The person who used this command **must** have `Manage Messages` **and** `Manage Channels` permissions to run this command.\n\nIf you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: Support server link - [S. T. A. R. LABS INJ2 Helper](https://discord.gg/S7MvBVh4Hy).")
            error = ['https://media.giphy.com/media/3oEjHERaTIdeuFQrXq/giphy.gif',
                     'https://media.giphy.com/media/3osxY9kuM2NGUfvThe/giphy.gif',
                     'https://media.giphy.com/media/8L0Pky6C83SzkzU55a/giphy.gif',
                     'https://media.giphy.com/media/fV1yHo8YyoKjzvMCKr/giphy.gif',
                     'https://media.giphy.com/media/TqiwHbFBaZ4ti/giphy.gif',
                     'https://media.giphy.com/media/ifdPjn6m4WyNlnXMTj/giphy.gif']
            embed.set_image(url=choice(error))
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed)



    @commands.guild_only()
    @commands.command(name='invite', aliases= ['i'])
    async def invite(self, ctx):
        print(f"Bot invite pressed by {ctx.message.author.name}")
        embed = discord.Embed(colour=discord.Colour(0xe01c38), url="https://discordapp.com",
                              description="Open this link in browser - [Invite the bot](https://discord.com/api/oauth2/authorize?client_id=742228161986691145&permissions=67492945&scope=bot)\nSupport server link - [S. T. A. R. LABS INJ2 Helper](https://discord.gg/S7MvBVh4Hy)")
        embed.set_author(name="Bot invite and support links", url="https://discordapp.com")
        embed.set_footer(
                text=f"Requested by: {ctx.message.author.name}",icon_url=ctx.guild.icon_url)
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
                        value="`ʙᴏʀɴ2ᴋɪʟʟ™#4215` and `Herood#6676` from `Destiny` and `[Δ₭] OVERMAN#0001` from `Apokolips Kingdom`, `Decebalus#7982` from `ГΘGUΞ` and `Skvam#2453` have accepted to use the builds from their servers. `SIGMA#5422` and `YSOSERIOUS™#7777` has helped in designing the character Build template.")
        embed.add_field(name="Character Passive Details",
                        value="`SIGMA#5422` and `shadowofintent#1026` have helped me in adding the passive info. Both of them shared the screenshots of their characters, so that, it would be easy to see the picture than read the details.")
        embed.add_field(name="Honourable Mentions",
                        value="Many people use this bot everyday. But, with request of few people, they have helped this bot get to this stage. So, my special thanks to\n- `Decebalus#7982`: Build Suggestions\n- `Noremac#7255`: Bot Tester\n- `resveratrol#7110`: Suggestions\n- `The asian cat#3430`: Bot Tester\n- `SigvaldTheGrim#2431`: Youtuber who spoke about my bot\n- `AGB | Roids#0182`: The Aftermath Overlord who accepted to build this bot in Aftermath Server\n- `《ԙ》kreampuffs#1992`: Suggestions\n- `MattRyan#7598`: Bot Tester and Suggestions\n- `EthanHunt#2416`: Suggestions\n and many more..\n\n*This is the Way!*\n\n__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: Support server link - [S. T. A. R. LABS INJ2 Helper](https://discord.gg/S7MvBVh4Hy).")
        file = discord.File("./STAR_LABS.jpg", filename="STAR_LABS.jpg")
        embed.set_thumbnail(url="attachment://STAR_LABS.jpg")
        embed.set_footer(
                text=f"Requested by: {ctx.message.author.name}",icon_url=ctx.guild.icon_url)
        await ctx.channel.send(embed=embed, file=file)

    @commands.guild_only()
    @commands.command(name='help', aliases= ['h'])
    async def _help(self, ctx, cmd: str = None):
        if cmd is None:
            print(f"No command. Hence, printing common help. - {ctx.message.author.name}")
            embed = discord.Embed(colour=discord.Colour(0x29a98e), url="https://discordapp.com",
                              description="Hello Player! This bot will guide you by providing details like character builds, gears and materials and so on..\n\nJust type `i!help` If you are stuck anywhere and I'll be here to help! 😎 ")

        # :diamond_shape_with_a_dot_inside: `solo` - Solo Raid Reminder, embed.set_image(url="https://vignette.wikia.nocookie.net/injustice-2-mobile2242/images/5/5a/BlackManta.jpg")
            embed.set_thumbnail(
                url="https://www.injusticeonline.com/wp-content/uploads/2017/05/injustice-2-mobile-icon.jpg")
            embed.set_author(name="📖 Help Command")
            embed.add_field(name="__Basic Commands__", value="""
:diamond_shape_with_a_dot_inside: `art` - Artifact Information,
:diamond_shape_with_a_dot_inside: `arteff` - Artifact Reroll Effects,
:diamond_shape_with_a_dot_inside: `build` - Character Builds,
:diamond_shape_with_a_dot_inside: `calc` - Calculator,
:diamond_shape_with_a_dot_inside: `cd` - Jump Cooldown Tracker,
:diamond_shape_with_a_dot_inside: `chars` - Characters List,
:diamond_shape_with_a_dot_inside: `orb` - Orbs Information,
:diamond_shape_with_a_dot_inside: `setup` - Creates the Category and channels for the bot,
:diamond_shape_with_a_dot_inside: `syn` - Team Synergy Information""")
            embed.add_field(name='__Other Commands__', value="""
:diamond_shape_with_a_dot_inside: `about` - Information aboue the bot,
:diamond_shape_with_a_dot_inside: `donate` - Donate money to the Creator of the Bot,
:diamond_shape_with_a_dot_inside: `prefix` - Prefix set for the bot in the server,
:diamond_shape_with_a_dot_inside: `stats` - Bot Statistics,
:diamond_shape_with_a_dot_inside: `vote` - Vote the bot in Top.gg Website.

If you need more info about each command, then type `[prefix]help [command]`. For example, `i!help build` to show the list of character builds available in the bot.\n\n__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: Support server link - [S. T. A. R. LABS INJ2 Helper](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed)

        elif cmd == 'prefix':
            print(f"Character Abbrev command by {ctx.message.author.name}")
            embed = discord.Embed(colour=discord.Colour(0xf79263), url="https://discordapp.com",
                                  description="To check the prefix use in your server, you can type `i!prefix` to get the list. If you're unaware of the prefix, then you can mention the bot and type prefix to get the list, just like this: `@S. T. A. R. LABS prefix`.\n To reset the prefix, type `i!prefix reset` and it will change the prefix to default ones.\n\n__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: Support server link - [S. T. A. R. LABS INJ2 Helper](https://discord.gg/S7MvBVh4Hy).")

            embed.set_author(name="Prefix checking and setting", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name}",icon_url=ctx.guild.icon_url)
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
                            value="To get a list of Legendary characters, type, ```i!chars legend``` to get the list.\n\n__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: Support server link - [S. T. A. R. LABS INJ2 Helper](https://discord.gg/S7MvBVh4Hy).")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed)

        elif cmd == 'b' or cmd == 'build':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""Here are the builds available in STAR LABS. We will add other builds soon. To use the command, type, ```i!b [character command]```If you wish to add your builds to this bot, you can DM `Mando_The_Mercenary™#9484`.""")
            embed.set_author(name="Build Commands", url="https://discordapp.com")
            embed.add_field(name="🟪 Legendary Characters", value="""```akbm - Arkham Knight Batman
bm   - Black Manta
bnc  - Brainiac
bngg - Batman Ninja Gorilla Grodd
cowsm- Collector of Worlds Superman
ds   - Darkseid
dtk  - Deathstroke
jls  - Justice League Superman
raven- Raven
sshq - Suicide Squad Harley Quinn 
sse  - Suicide Squad Enchantress
mmh  - Martian Manhunter```""")
            embed.add_field(name="⬜ Silver Characters", value="""```aww - Amazon Wonder Woman
svbc - Sonic Black Canary
svcw - Silver Catwoman 
svam - Silver Aquaman 
svc  - Silver Cyborg
svf  - Silver Flash
svj  - Silver Joker 
svhq - Silver Harley Quinn
svst - Silver Swamp Thing
svgg - Silver Gorilla Grodd
svb  - Silver Bane
svds - Silver Deadshot
svsc - Silver Scarecrow
svr  - Silver Robin
svdf - Silver Doctor Fate
svga - Silver Green Arrow
svww - Silver Wonder Woman 
svsm - Silver Superman
svgl - Silver Green Lantern
svbm - Silver Batman```""")
            embed.add_field(name="🟨 Gold Characters (Batman Ninjas)", value="""```bnbm - Batman Ninja Batman
bnhq - Batman Ninja Harley Quinn
bncw - Batman Ninja Catwoman
bnr  - Batman Ninja Robin
bnlj - Batman Ninja Lord Joker```""")
            embed.add_field(name="🟨 Gold Characters (Multiverse Gang)", value="""```mvbw - Multiverse Bat Woman
mvf  - Multiverse The Flash
mvbl - Multiverse Black Lightning
mvga - Multiverse Green Arrow 
mvwc - Multiverse White Canary
mvbw - Multiverse Batwoman
mvcc - Multiverse Captain Cold
mvsg - Multiverse Supergirl
mvasg- Multiverse Armored Supergirl```""")
            embed.add_field(name="🟨 Gold Characters (The Justice League)", value="""```jlc  - Justice League Cyborg
jlf  - Justice League Flash
jla  - Justice League Aquaman
jlb  - Justice League Batman
mww  - Mythic Wonder woman```""")
            embed.add_field(name="🟨 Gold Characters (League of Anarchy)", value="""```epi  - Entangling Poison Ivy
hbhq - Heart Breaker Harley Quinn
llj  - Last Laugh Joker ```""")

            embed.add_field(name='🟨 Gold Characters (Others Part 1)', value="""```bb  - Blue Beetle
asm  - Armoured Superman
koaam- King of Atlantis Aquaman
sb   - Silver Banshee
szm  - Shazam
aaam - Atlantean Armored Aquaman
egl  - Emerald Green Lantern
mtcw - Masterthief Catwoman
bmr  - Blade Master Robin
atc  - Atrocitus
ba   - Black Adam
csm  - Classic Superman 
dsg - Dark Super Girl
esf - Energized Starfire
fpi - Flora Poison Ivy 
hb  - Hellboy
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
vxn - Vixen
uhq - Unhinged Harley Quinn```\n\n__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: Support server link - [S. T. A. R. LABS INJ2 Helper](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed)

        elif cmd == 'passive' or cmd == 'p':
            print(f"Character Passive command by {ctx.message.author.name}")
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="There are passives for each and every character, which get enabled during battle or at the start of the battle. To know the character's passive, type, ```i!p [character name]``` Where, we type the character's name without the brackets []. For Example, ```i!p jsgl```The following list of characters have their respective passives.")

            embed.set_author(name="Character Passives", url="https://discordapp.com",
                             icon_url="https://cdn.discordapp.com/embed/avatars/3.png")
            embed.add_field(name="🟪 Legendary Characters", value="""```akbm - Arkham Knight Batman
bm - Black Manta
bnc - Brainiac
bngg - Batman Ninja Gorilla Grodd
cowsm- Collector of Worlds Superman
ds - Darkseid
dtk  - Deathstroke
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
uhq - Unhinged Harley Quinn
vxn - Vixen```\n\n__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: Support server link - [S. T. A. R. LABS INJ2 Helper](https://discord.gg/S7MvBVh4Hy).""")
            
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name}",icon_url=ctx.guild.icon_url)
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
                            value="The command will show the amount of artifact material required to upgrade the artifacts. To know more, type, ```i!a [from] [to]```\n\n__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: Support server link - [S. T. A. R. LABS INJ2 Helper](https://discord.gg/S7MvBVh4Hy).")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name}",icon_url=ctx.guild.icon_url)
            # await ctx.channel.send(embed=embed)
            await ctx.channel.send(embed=embed)

        elif cmd == 'solo':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5), url="https://discordapp.com",
                                  description="This command will remind you for pip refresh.")

            embed.set_author(name="Solo Raid Reminder", url="https://discordapp.com",
                             icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
            embed.add_field(name="__Points to Note__",
                            value="""There are few things to consider when using this command. Command usage as follows:

__Solo Raid Register__

```i!solo register -r @role -c #channel```
(or)
```i!solo register -c #channel -r @role```

This will register your server for reminding specified role in specified channel. Please note that there must be only one space between the commands.

__Solo Raid Update__

```i!solo update -r @role -c #channel```
(or)
```i!solo update -c #channel -r @role```

This will update the specified role and channel.

__Solo Raid Switch__

```i!solo on``` - This will start the bot to mention that role whenever it's refresh time.
```i!solo off``` - This will stop the bot to mention the role and send message.

If you have any doubts, tag or message `Mando_The_Mercenary™#9484`.
""")
            embed.add_field(name="__Permissions to the bot and the user__",
                            value="""The command will work only when, 

1) The bot has the `Send message` in that channel and ability to mention specified role.
2) The user of this command must have permissions: `Manage Server/Guild` and `Manage Channels`.

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: Support server link - [S. T. A. R. LABS INJ2 Helper](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name}",icon_url=ctx.guild.icon_url)
            # await ctx.channel.send(embed=embed)
            await ctx.channel.send(embed=embed)
        
        elif cmd == 'cd':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5), url="https://discordapp.com",
                                  description="This command will help you track your jump cooldown and when the cooldown is over, it will send a DM to you stating your cooldown is finished.")
            embed.set_author(name="Jump Cooldown Tracker", url="https://discordapp.com")
            embed.add_field(name = '**__How to use__**', 
                    value="Type `i!cd start` to start the cooldown tracker. To get to know how many days left for cooldown reset, type `i!cd status` and it will show the details. To stop the tracker, type `i!cd stop`.")
            embed.add_field(name = '**__Important Note__**',
                    value = '''Once you stop the tracker, it will reset back to 22 days (Default value). Since the general cooldown is 21 days in the game, I added another day just to be safe and avoid confusion while jumping.

Also, in the game, once you jump back to your original league, only then the cooldown will be in effect. Hence, it is better to start the tracker after that.

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: Support server link - [S. T. A. R. LABS INJ2 Helper](https://discord.gg/S7MvBVh4Hy).''')
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed)

        else:
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5), url="https://discordapp.com",
                                  description="You have typed a command which is not present in the command list, to know the help commands, type ```i!help```\n\n__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: Support server link - [S. T. A. R. LABS INJ2 Helper](https://discord.gg/S7MvBVh4Hy).")
            embed.set_author(name="Something wrong..", url="https://discordapp.com")
            error = ['https://media.giphy.com/media/3oEjHERaTIdeuFQrXq/giphy.gif',
                     'https://media.giphy.com/media/3osxY9kuM2NGUfvThe/giphy.gif',
                     'https://media.giphy.com/media/8L0Pky6C83SzkzU55a/giphy.gif',
                     'https://media.giphy.com/media/fV1yHo8YyoKjzvMCKr/giphy.gif',
                     'https://media.giphy.com/media/TqiwHbFBaZ4ti/giphy.gif',
                     'https://media.giphy.com/media/ifdPjn6m4WyNlnXMTj/giphy.gif']
            embed.set_image(url=choice(error))
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name}",icon_url=ctx.guild.icon_url)
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