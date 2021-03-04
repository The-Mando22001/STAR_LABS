import os
#import dotenv
import discord
import asyncio

from discord.ext import commands, tasks
from discord.voice_client import VoiceClient

from random import choice
import csv
import pytz
from datetime import datetime
import time


#Token Placed in another txt file
f = open('token.txt', 'r')
token = str(f.read())

async def get_pre(bot, message):
        return ["i!", "I!", "|!"]  # or a list, ["pre1","pre2"]

custom_prefixes = {}
default_prefixes = ["i!", "I!", "|!"]

async def determine_prefix(bot, message):
    guild = message.guild
    #Only allow custom prefixs in guild
    if guild:
        return custom_prefixes.get(guild.id, default_prefixes)
    else:
        return default_prefixes

#Setting prefix to the bot
client = commands.Bot(command_prefix=determine_prefix, case_insensitive=True)

#Removing Default Help Command
client.remove_command('help')

voice_feature = {}
synergy_feature = {}
build_feature = {}
passive_feature = {}
calc_feature = {}


#Replies when ready
@client.event
async def on_ready():
    change_status.start()
    #await client.change_presence(status=discord.Status.online, activity=discord.Game(f"type {default_prefixes}help"))
    print("bot is online")
    print(client.user)
    count = 0
    global voice_feature
    global synergy_feature
    global build_feature
    global passive_feature
    global calc_feature
    for guild in client.guilds:
        count = count+1
        voice_feature[guild.id] = True
        synergy_feature[guild.id] = True
        build_feature[guild.id] = True
        passive_feature[guild.id] = True
        calc_feature[guild.id] = True
    print(f'Total number of Servers: {count}')

@client.command(name='serverstats', aliases=['ss','stats'])
async def _serverstats(ctx):
    count_ser = 0
    count_mem = 0
    for guild in client.guilds:
        member_list = []
        for member in guild.members:
            member_list += member.name
        count_mem = count_mem + len(member_list)
        count_ser = count_ser + 1
    embed = discord.Embed(colour=discord.Colour(0x29a98e), url="https://discordapp.com",
                          description="The following shows the stats of the bot.")
    embed.set_author(name="Bot Statistics")
    embed.add_field(name="Number of servers", value=f"{count_ser}")
    embed.add_field(name='Number of Users', value=f"{count_mem}")
    embed.add_field(name="Latency", value=f"{round(client.latency*1000)} ms")
    file = discord.File("./STAR_LABS.jpg", filename="STAR_LABS.jpg")
    embed.set_thumbnail(url="attachment://STAR_LABS.jpg")
    await ctx.channel.send(embed=embed, file=file)

@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(f"type {choice(default_prefixes)}help"))


@client.command(pass_context=True)
async def dashboard(ctx):
    embed = discord.Embed(colour=discord.Colour(0xc414c4),
                          description=f"""Welcome to STAR LABS Dashboard {ctx.message.author.name}!""")
    embed.set_author(name="STAR LABS Dashboard", url="https://discordapp.com")
    await ctx.channel.send(embed=embed)

@client.command(name='solo')
async def solo_pip(ctx, cmd:str = None):
    if ctx.message.author.id == 685455946390044674:
        if cmd == 'start1':
            await ctx.channel.send("Solo Raid Pip Reminder starts now.")
            start_spam_aftermath.start(ctx.channel)
        if cmd == 'start2':
            await ctx.channel.send("Solo Raid Pip Reminder starts now.")
            start_spam_rouge.start(ctx.channel)
        if cmd == 'start3':
            await ctx.channel.send("Solo Raid Pip Reminder starts now.")
            start_spam_eternity.start(ctx.channel)
        if cmd == 'start4':
            await ctx.channel.send("Solo Raid Pip Reminder starts now.")
            start_spam_haha.start(ctx.channel)
        if cmd == 'start5':
            await ctx.channel.send("Solo Raid Pip Reminder starts now.")
            start_spam_gotham.start(ctx.channel)
        if cmd == 'stop1':
            await ctx.channel.send("Aight, I'mma stop reminding now")
            start_spam_aftermath.cancel()
        if cmd == 'stop2':
            await ctx.channel.send("Aight, I'mma stop reminding now")
            start_spam_rouge.cancel()
        if cmd == 'stop3':
            await ctx.channel.send("Aight, I'mma stop reminding now")
            start_spam_eternity.cancel()
        if cmd == 'stop4':
            await ctx.channel.send("Aight, I'mma stop reminding now")
            start_spam_haha.cancel()
        if cmd == 'stop5':
            await ctx.channel.send("Aight, I'mma stop reminding now")
            start_spam_gotham.cancel()
    else:
        await ctx.channel.send("You're not my Owner. Only my Owner and Sensei (Mando) has this permission to write the command. Contact him.")

@tasks.loop(seconds=1)
async def start_spam_aftermath(channel):
    time_in = datetime.now(pytz.timezone('Asia/Kolkata'))
    count = time_in.strftime("%I.%M.%S")
    if count == '08.00.00':
        await channel.send('<@&776819305714810911> 30 mins early reminder pip refresh!! Play your pips before it expires!')
    if count == '08.30.00':
        await channel.send('<@&776819305714810911> pip refresh!! Enjoy your solo raid pips!')

@tasks.loop(seconds=1)
async def start_spam_rouge(channel):
    time_in = datetime.now(pytz.timezone('Asia/Kolkata'))
    count = time_in.strftime("%I.%M.%S")
    if count == '08.00.00':
        await channel.send('<@&776976184843698207> 30 mins early reminder pip refresh!! Play your pips before it expires!')
    if count == '08.30.00':
        await channel.send('<@&776976184843698207> pip refresh!! Enjoy your solo raid pips!')

@tasks.loop(seconds=1)
async def start_spam_eternity(channel):
    time_in = datetime.now(pytz.timezone('Asia/Kolkata'))
    count = time_in.strftime("%I.%M.%S")
    if count == '08.00.00':
        await channel.send('<@&694066334140465172> 30 min Solo Raid pip refresh reminder!!')
    if count == '08.30.00':
        await channel.send('<@&694066334140465172> Solo Raid pip refresh reminder!!')

@tasks.loop(seconds=1)
async def start_spam_haha(channel):
    time_in = datetime.now(pytz.timezone('Asia/Kolkata'))
    count = time_in.strftime("%I.%M.%S")
    if count == '08.00.00':
        await channel.send('<@&789562565071339561> 30 min Solo Raid pip refresh reminder!!')
    if count == '08.30.00':
        await channel.send('<@&789562565071339561> Solo Raid pip refresh reminder!!')

@tasks.loop(seconds=1)
async def start_spam_gotham(channel):
    time_in = datetime.now(pytz.timezone('Asia/Kolkata'))
    count = time_in.strftime("%I.%M.%S")
    if count == '08.00.00':
        await channel.send('<@&789533444328783892> 30 min Solo Raid pip refresh reminder!!')
    if count == '08.30.00':
        await channel.send('<@&789533444328783892> Solo Raid pip refresh reminder!!')

'''Loading, Unloading Extensions or Cogs'''
class SecretServerError(commands.CheckFailure):
    pass

def check_server():
    def predicate(ctx):
        if not (ctx.message.guild.name == 'Aftermath Community'):
            raise SecretServerError('Something Spooky is going on... don\'t worry')
        return True
    return commands.check(predicate)


@client.command(name= 'load')
@commands.has_permissions(administrator= True)
@check_server()
async def load(ctx, extension):
    client.load_extension(f'Cogs.{extension}')
    await ctx.channel.send(f"{extension} loaded successfully")

@load.error
async def secret_stuff(ctx, error):
    if isinstance(error, SecretServerError):
        await ctx.channel.send(error)


@client.command(name= 'unload')
@commands.has_permissions(administrator= True)
@check_server()
async def unload(ctx, extension):
    client.unload_extension(f'Cogs.{extension}')
    await ctx.channel.send(f"{extension} unloaded successfully")


@unload.error
async def secret_stuff(ctx, error):
    if isinstance(error, SecretServerError):
        await ctx.channel.send(error)


@client.command(name='reload')
@commands.has_permissions(administrator= True)
@check_server()
async def reload(ctx):
    for filename in os.listdir('./Cogs'):
        if filename.endswith('.py'):
            client.unload_extension(f'Cogs.{filename[:-3]}')
    await ctx.channel.send(f"Extensions unloaded successfully")
    for filename in os.listdir('./Cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'Cogs.{filename[:-3]}')
    await ctx.channel.send(f"Extensions loaded successfully")


@reload.error
async def secret_stuff(ctx, error):
    if isinstance(error, SecretServerError):
        await ctx.channel.send(error)

#Ping command
@client.command()
async def ping(ctx):
    await ctx.channel.send(f'**Pong**! {round(client.latency*1000)}ms')

'''@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        await message.channel.send("You can type `i!help` for more info.")'''

for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'Cogs.{filename[:-3]}')


client.run(token)