import discord
from discord.ext import commands
from random import choice
from disputils import BotEmbedPaginator

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
                        value="`ʙᴏʀɴ2ᴋɪʟʟ™#4215` from `Destiny` and `[Δ₭] OVERMAN#0001` from `Apokolips Kingdom` have accepted to use the builds from their servers. `SIGMA#5422` and `YSOSERIOUS™#7777` has helped in designing the character Build template.")
        embed.add_field(name="Character Passive Details",
                        value="`SIGMA#5422` and `shadowofintent#1026` have helped me in adding the passive info. Both of them shared the screenshots of their characters, so that, it would be easy to see the picture than read the details.")
        embed.add_field(name="Honourable Mentions",
                        value="Many people use this bot everyday. But, with request of few people, they have helped this bot get to this stage. So, my special thanks to\n- `Noremac#7255`: Bot Tester\n- `resveratrol#7110`: Suggestions\n- `The asian cat#3430`: Bot Tester\n- `SigvaldTheGrim#2431`: Youtuber who spoke about my bot\n- `AGB | Roids#0182`: The Aftermath Overlord who accepted to build this bot in Aftermath Server\n- `《ԙ》kreampuffs#1992`: Suggestions\n- `MattRyan#7598`: Bot Tester and Suggestions\n- `EthanHunt#2416`: Suggestions\nand many more..\n\n*This is the Way!*")
        file = discord.File("./STAR_LABS.jpg", filename="STAR_LABS.jpg")
        embed.set_thumbnail(url="attachment://STAR_LABS.jpg")
        await ctx.channel.send(embed=embed, file=file)

    @commands.guild_only()
    @commands.command(name='help', aliases= ['h'])
    async def _help(self, ctx, cmd: str = None):
        if cmd is None:
            print(f"No command. Hence, printing common help. - {ctx.message.author.name}")
            embeds = [
                discord.Embed(color=ctx.author.color, url="https://discordapp.com",
                      description=f"Hello {ctx.message.author.name}! This bot will guide you by providing details like character builds, gears and materials and so on..\n\nJust type `i!help` If you are stuck anywhere and I'll be here to help! 😎 ").set_author(
                    name="Help Command").add_field(name="Bot Statistics",
                                                   value="To check the bot's statistics, type `i!stats` or `i!ss` or `i!serverstats`.").set_footer(
                    text=f"Last used by: {ctx.message.author.name} | Check out the `credits` command to see the list of people who helped making this bot.").set_thumbnail(
                    url="https://images.discordapp.net/avatars/742228161986691145/1fc82ca89577831cdb9863295820f681.png"),
                discord.Embed(color=ctx.author.color, url="https://discordapp.com",
                      description=f"Hello {ctx.message.author.name}! This bot will guide you by providing details like character builds, gears and materials and so on..\n\nJust type `i!help` If you are stuck anywhere and I'll be here to help! 😎 ").set_author(
                    name="Help Command").add_field(name="Vote the bot",
                                                   value="Please vote the bot using the link provided in the command `i!vote`.").set_footer(
                    text=f"Last used by: {ctx.message.author.name} | Check out the `credits` command to see the list of people who helped making this bot.").set_thumbnail(
                    url="https://images.discordapp.net/avatars/742228161986691145/1fc82ca89577831cdb9863295820f681.png"),
                discord.Embed(color=ctx.author.color, url="https://discordapp.com",
                      description=f"Hello {ctx.message.author.name}! This bot will guide you by providing details like character builds, gears and materials and so on..\n\nJust type `i!help` If you are stuck anywhere and I'll be here to help! 😎 ").set_author(
                    name="Help Command").add_field(name="Bot Invite and support",
                                                   value="If you really want me to help you out in your server, type `i!invite` to invite me into your server. I'll be there to help you and your friends 🥰. It also has link to support server.").set_footer(
                    text=f"Last used by: {ctx.message.author.name} | Check out the `credits` command to see the list of people who helped making this bot.").set_thumbnail(
                    url="https://images.discordapp.net/avatars/742228161986691145/1fc82ca89577831cdb9863295820f681.png"),
                discord.Embed(color=ctx.author.color, url="https://discordapp.com",
                      description=f"Hello {ctx.message.author.name}! This bot will guide you by providing details like character builds, gears and materials and so on..\n\nJust type `i!help` If you are stuck anywhere and I'll be here to help! 😎 ").set_author(
                    name="Help Command").add_field(name="Credits",
                                                   value="Check this out with `i!credits` or `i!about` to see the list of people who helped making this bot.").set_footer(
                    text=f"Last used by: {ctx.message.author.name} | Check out the `credits` command to see the list of people who helped making this bot.").set_thumbnail(
                    url="https://images.discordapp.net/avatars/742228161986691145/1fc82ca89577831cdb9863295820f681.png"),
                discord.Embed(color=ctx.author.color, url="https://discordapp.com",
                      description=f"Hello {ctx.message.author.name}! This bot will guide you by providing details like character builds, gears and materials and so on..\n\nJust type `i!help` If you are stuck anywhere and I'll be here to help! 😎 ").set_author(
                    name="Help Command").add_field(name='Bot channels setup',
                                                   value="If you want the bot to create the category and the respective channels for you, then you can type ```i!setup``` to create a category and corresponding channels in that category.").set_footer(
                    text=f"Last used by: {ctx.message.author.name} | Check out the `credits` command to see the list of people who helped making this bot.").set_thumbnail(
                    url="https://images.discordapp.net/avatars/742228161986691145/1fc82ca89577831cdb9863295820f681.png"),
                discord.Embed(color=ctx.author.color, url="https://discordapp.com",
                      description=f"Hello {ctx.message.author.name}! This bot will guide you by providing details like character builds, gears and materials and so on..\n\nJust type `i!help` If you are stuck anywhere and I'll be here to help! 😎 ").set_author(
                    name="Help Command").add_field(name="Prefix checking and changing",
                                                   value="If you want to check or change the prefix, then, you need to type:\n`i!prefix` to get the prefix, and\n`i!set_prefix` to set the prefix in the server.").set_footer(
                    text=f"Last used by: {ctx.message.author.name} | Check out the `credits` command to see the list of people who helped making this bot.").set_thumbnail(
                    url="https://images.discordapp.net/avatars/742228161986691145/1fc82ca89577831cdb9863295820f681.png"),
                discord.Embed(color=ctx.author.color, url="https://discordapp.com",
                      description=f"Hello {ctx.message.author.name}! This bot will guide you by providing details like character builds, gears and materials and so on..\n\nJust type `i!help` If you are stuck anywhere and I'll be here to help! 😎 ").set_author(
                    name="Help Command").add_field(name="Character Abbreviations",
                                                   value="This will show the list of characters available in the game in the abbreviated form. If you want to know more, type, `i!chars`").set_footer(
                    text=f"Last used by: {ctx.message.author.name} | Check out the `credits` command to see the list of people who helped making this bot.").set_thumbnail(
                    url="https://images.discordapp.net/avatars/742228161986691145/1fc82ca89577831cdb9863295820f681.png"),
                discord.Embed(color=ctx.author.color, url="https://discordapp.com",
                      description=f"Hello {ctx.message.author.name}! This bot will guide you by providing details like character builds, gears and materials and so on..\n\nJust type `i!help` If you are stuck anywhere and I'll be here to help! 😎 ").set_author(
                    name="Help Command").add_field(name="Character Builds",
                                                   value="This will provide the best character builds. To know more, type, `i!b`").set_footer(
                    text=f"Last used by: {ctx.message.author.name} | Check out the `credits` command to see the list of people who helped making this bot.").set_thumbnail(
                    url="https://images.discordapp.net/avatars/742228161986691145/1fc82ca89577831cdb9863295820f681.png"),
                discord.Embed(color=ctx.author.color, url="https://discordapp.com",
                      description=f"Hello {ctx.message.author.name}! This bot will guide you by providing details like character builds, gears and materials and so on..\n\nJust type `i!help` If you are stuck anywhere and I'll be here to help! 😎 ").set_author(
                    name="Help Command").add_field(name="Character Passives",
                                                   value="There are passive abilities for characters which are unique for every character. To know more, type, `i!passive`").set_footer(
                    text=f"Last used by: {ctx.message.author.name} | Check out the `credits` command to see the list of people who helped making this bot.").set_thumbnail(
                    url="https://images.discordapp.net/avatars/742228161986691145/1fc82ca89577831cdb9863295820f681.png"),
                discord.Embed(color=ctx.author.color, url="https://discordapp.com",
                      description=f"Hello {ctx.message.author.name}! This bot will guide you by providing details like character builds, gears and materials and so on..\n\nJust type `i!help` If you are stuck anywhere and I'll be here to help! 😎 ").set_author(
                    name="Help Command").add_field(name="Artifact Information",
                                                   value="This will show information about different artifacts available in the game. To know more, type, `i!art`").set_footer(
                    text=f"Last used by: {ctx.message.author.name} | Check out the `credits` command to see the list of people who helped making this bot.").set_thumbnail(
                    url="https://images.discordapp.net/avatars/742228161986691145/1fc82ca89577831cdb9863295820f681.png"),
                discord.Embed(color=ctx.author.color, url="https://discordapp.com",
                      description=f"Hello {ctx.message.author.name}! This bot will guide you by providing details like character builds, gears and materials and so on..\n\nJust type `i!help` If you are stuck anywhere and I'll be here to help! 😎 ").set_author(
                    name="Help Command").add_field(name='Artifact Effect Information',
                                                   value='This will provide the reroll values for artifact talent. To know more, type `i!ae` or `i!arteff`').set_footer(
                    text=f"Last used by: {ctx.message.author.name} | Check out the `credits` command to see the list of people who helped making this bot.").set_thumbnail(
                    url="https://images.discordapp.net/avatars/742228161986691145/1fc82ca89577831cdb9863295820f681.png"),
                discord.Embed(color=ctx.author.color, url="https://discordapp.com",
                      description=f"Hello {ctx.message.author.name}! This bot will guide you by providing details like character builds, gears and materials and so on..\n\nJust type `i!help` If you are stuck anywhere and I'll be here to help! 😎 ").set_author(
                    name="Help Command").add_field(name="Team Synergy Information",
                                                   value="This will show the Team synergy information, which give boost to your characters in battle during team selection. To know more, type, `i!syn`").set_footer(
                    text=f"Last used by: {ctx.message.author.name} | Check out the `credits` command to see the list of people who helped making this bot.").set_thumbnail(
                    url="https://images.discordapp.net/avatars/742228161986691145/1fc82ca89577831cdb9863295820f681.png"),
                discord.Embed(color=ctx.author.color, url="https://discordapp.com",
                      description=f"Hello {ctx.message.author.name}! This bot will guide you by providing details like character builds, gears and materials and so on..\n\nJust type `i!help` If you are stuck anywhere and I'll be here to help! 😎 ").set_author(
                    name="Help Command").add_field(name="Upgrade Calculator",
                                                   value="You can type start and end of number of levels of any upgrade (gear, artifact, xp and sp) to calculate how much material or coins required. To know more, type, `i!calc`").set_footer(
                    text=f"Last used by: {ctx.message.author.name} | Check out the `credits` command to see the list of people who helped making this bot.").set_thumbnail(
                    url="https://images.discordapp.net/avatars/742228161986691145/1fc82ca89577831cdb9863295820f681.png")
            ]

            paginator = BotEmbedPaginator(ctx, embeds)
            await paginator.run()

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