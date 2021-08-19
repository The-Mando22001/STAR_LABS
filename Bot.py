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
import itertools
import json
""" import schedule

schedule.every(25).seconds.do(update_cache) """

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
        return commands.when_mentioned_or(*custom_prefixes.get(str(guild.id), default_prefixes))(bot, message)
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

#guilds = []
#channel_list = []
#role_list = []
#status_list = []
jumpcd_user = []
jumpcd_time = []

""" def update_cache():
global channel_list
global role_list
global status_list
global guilds

channel_list = []
role_list = []
status_list = []
guilds = []

with open('data.json') as json_file: 
    data = json.load(json_file) 

    temp = data['solo']
    for t in temp:
        #guilds.append(t['id'])
        if (client.get_guild(t['id']) != None):
            if client.get_channel(t['channel']):
                if (t['status'] == True):
                    guilds.append(t['id'])
                    role: discord.Role = t['role']
                    channel: discord.TextChannel = t['channel']
                    role_list.append(role)
                    channel_list.append(channel) """

@tasks.loop(seconds=60)
async def update_jumpcd():
    global jumpcd_user
    global jumpcd_time
    jumpcd_user = []
    jumpcd_time = []
    with open('jumpcd.json') as json_file: 
        data = json.load(json_file)

        temps = data['jumpcd']
        for p in temps:
            if client.get_user(p['id']):
                if int(p['time_rem']) > 0:
                    jumpcd_user.append(int(p['id']))
                    jumpcd_time.append(int(p['time_rem']))

        for num, user in zip(jumpcd_time, jumpcd_user):
            num = num - 60
            if num == 0:
                value = check_jumpcd_json(jumpcd_user[jumpcd_user.index(user)])
                temps[value]['time_rem'] = 0
                
                #print(jumpcd_user.index(user))
                try:
                    msg = await client.fetch_user(int(user))
                    await msg.send('This is cooldown reminder! Your cooldown is now 0. You are now able to attend jumps!')
                except:
                    pass
                finally:
                    write_json_jumpcd(data)
            else:
                value = check_jumpcd_json(jumpcd_user[jumpcd_user.index(user)])
                #print(jumpcd_user[jumpcd_user.index(user)])
                temps[value]['time_rem'] = num
                write_json_jumpcd(data)

#Replies when ready
@client.event
async def on_ready():
    change_status.start()
    #await client.change_presence(status=discord.Status.online, activity=discord.Game(f"type {default_prefixes}help"))
    print("bot is online")
    print(client.user)
    count = 0
    for guild in client.guilds:
        count = count+1
    print(f'Total number of Servers: {count}')
    
    

    try:
        update_prefix.start()
    except:
        update_prefix.cancel()
        update_prefix.start()
    
    try:
        update_jumpcd.start()
    except:
        update_jumpcd.cancel()
        update_jumpcd.start()
    
    """ while True:
        schedule.run_pending()
        time.sleep(1) """

@tasks.loop(seconds=1)
async def update_prefix():
    global custom_prefixes
    custom_prefixes = {}
    with open('prefix.json') as json_file: 
        data = json.load(json_file)

        temps = data['prefix']
        for p in temps:
            custom_prefixes[str(p['id'])] = p['pre']
            #print(p)

def write_json_prefix(data, filename='prefix.json'): 
        with open(filename,'w') as f: 
            json.dump(data, f, indent=4) 

def write_json_jumpcd(data, filename='jumpcd.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

@tasks.loop(seconds=1)
async def start_solo_reminder():
    status_list = []
    guilds = []
    
    
                        
    time_in = datetime.now(pytz.timezone('Asia/Kolkata'))
    count = time_in.strftime("%I.%M.%S")
    if count == '07.00.00':
        channel_list = []
        role_list = []
        with open('data.json') as json_file: 
            data = json.load(json_file) 
        
            temp = data['solo']
            for t in temp:
                #guilds.append(t['id'])
                if (client.get_guild(t['id']) != None):
                    if client.get_channel(t['channel']):
                        if (t['status'] == True):
                            #guilds.append(t['id'])
                            role: discord.Role = t['role']
                            channel: discord.TextChannel = t['channel']
                            role_list.append(role)
                            channel_list.append(channel)
        for (channel, role) in zip(channel_list, role_list):
            channel = await client.fetch_channel(int(channel))
            await channel.send(f'<@&{role}> 30 mins early reminder for pip refresh!! Play your pips before it expires!')

        json_file.close()
    if count == '07.30.00':
        channel_list = []
        role_list = []
        with open('data.json') as json_file: 
            data = json.load(json_file) 
        
            temp = data['solo']
            for t in temp:
                #guilds.append(t['id'])
                if (client.get_guild(t['id'])):
                    if client.get_channel(t['channel']):
                        if (t['status'] == True):
                            #guilds.append(t['id'])
                            role: discord.Role = t['role']
                            channel: discord.TextChannel = t['channel']
                            role_list.append(role)
                            channel_list.append(channel)
        for (channel, role) in zip(channel_list, role_list):
            channel = await client.fetch_channel(int(channel))
            await channel.send(f'<@&{role}> Solo Raid Pip refresh!! Play your pips before it expires!')

        json_file.close()

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
    count = 0
    for guild in client.guilds:
        count = count+1
    await client.change_presence(activity=discord.Game(f"Injustice 2 Mobile! Running in {count} Servers."))

def write_json(data, filename='data.json'): 
        with open(filename,'w') as f: 
            json.dump(data, f, indent=4) 
    
def check_solo_json(value):
    with open('data.json') as json_file: 
        data = json.load(json_file) 
    
        temp = data['solo']
        guilds = []
        for t in temp:
            guilds.append(t['id'])

        try:
            value = guilds.index(value)
        except:
            value = -1
    
    return value

def check_prefix_json(value):
    with open('prefix.json') as json_file: 
        data = json.load(json_file) 
    
        temp = data['prefix']
        guilds = []
        for t in temp:
            guilds.append(int(t['id']))

        try:
            value = guilds.index(value)
        except:
            value = -1
    
    return value

def check_jumpcd_json(value):
    with open('jumpcd.json') as json_file:
        data = json.load(json_file)

        temp = data['jumpcd']
        users = []
        for t in temp:
            users.append(int(t['id']))

        try:
            value = users.index(value)
        except:
            value = -1

    return value



@client.command(pass_context=True)
@commands.has_permissions(manage_guild=True, manage_channels=True)
async def solo(ctx, *, values: str):
    txt = values.split(" ")
    
    if txt[0] == 'register':
        value = check_solo_json(ctx.message.guild.id)
        if value == -1:
            if txt[1] == '-c':
                channel = txt[2]
                channel = channel.replace("<","")
                channel = channel.replace("#","")
                channel = channel.replace(">","")
                channel = int(channel)
                print(channel)
                print(type(channel))
            elif txt[1] == '-r':
                role = txt[2]
                role = role.replace("<","")
                role = role.replace("@","")
                role = role.replace("&","")
                role = role.replace(">","")
                role = int(role)
                print(role)
                print(type(role))
        
            if txt[3] == '-c':
                channel = txt[4]
                channel = channel.replace("<","")
                channel = channel.replace("#","")
                channel = channel.replace(">","")
                channel = int(channel)
                print(channel)
                print(type(channel))
            elif txt[3] == '-r':
                role = txt[4]
                role = role.replace("<","")
                role = role.replace("@","")
                role = role.replace("&","")
                role = role.replace(">","")
                role = int(role)
                print(role)
                print(type(role))
            guild = ctx.message.guild.id
            status = False
            y = {"id": guild, "status": status, "channel": channel, "role": role}
            with open('data.json') as json_file: 
                data = json.load(json_file) 
            temp = data['solo']
            temp.append(y)
            write_json(data) 
            await ctx.channel.send(f'Role registered successfully. Reminder will be starting in <#{channel}> and remind <@&{role}>')
        else:
            await ctx.channel.send('Reminder already registered!')  
    
    if txt[0] == 'on':
        value = check_solo_json(ctx.message.guild.id)
        if value != -1:
            with open('data.json') as json_file: 
                    data = json.load(json_file) 
            temp = data['solo']
            temp[value]['status'] = True
            write_json(data)
            await ctx.channel.send("Solo Raid Reminder Switched on!")
        else:
            await ctx.channel.send("This feature is not registered! Kindly register to enable this feature.")
    
    if txt[0] == 'off':
        value = check_solo_json(ctx.message.guild.id)
        if value != -1:
            with open('data.json') as json_file: 
                    data = json.load(json_file) 
            temp = data['solo']
            temp[value]['status'] = False
            write_json(data)
            await ctx.channel.send("Solo Raid Reminder Switched off!")
        else:
            await ctx.channel.send("This feature is not registered! Kindly register to enable this feature.")
    
    if txt[0] == 'update':
        value = check_solo_json(ctx.message.guild.id)
        if value == -1:
            await ctx.channel.send("This feature is not registered! Kindly register to enable this feature.")
        else:
            if txt[1] == '-c':
                channel = txt[2]
                channel = channel.replace("<","")
                channel = channel.replace("#","")
                channel = channel.replace(">","")
                channel = int(channel)
            elif txt[1] == '-r':
                role = txt[2]
                role = role.replace("<","")
                role = role.replace("@","")
                role = role.replace("&","")
                role = role.replace(">","")
                role = int(role)
        
            if txt[3] == '-c':
                channel = txt[4]
                channel = channel.replace("<","")
                channel = channel.replace("#","")
                channel = channel.replace(">","")
                channel = int(channel)
            elif txt[3] == '-r':
                role = txt[4]
                role = role.replace("<","")
                role = role.replace("@","")
                role = role.replace("&","")
                role = role.replace(">","")
                role = int(role)
            guild = ctx.message.guild.id
            status = False
            y = {"id": guild, "status": status, "channel": channel, "role": role}
            with open('data.json') as json_file: 
                data = json.load(json_file) 
            temp = data['solo']
            temp[value]['role'] = role
            temp[value]['channel'] = channel
            write_json(data)
            await ctx.channel.send("Channel and role updated successfully.")
        
    if txt[0] == 'start':
        if ctx.message.author.id == 685455946390044674:
            start_solo_reminder.start()
            await ctx.channel.send('Solo raid reminder started successfully!')
        else:
            await ctx.channel.send("You do not have the permission to start the reminder. You only have the permission to switch it on or off. Please ask Mando_The_Mercenary#9484 to start it.")

    if txt[0] == 'stop':
        if ctx.message.author.id == 685455946390044674:
            start_solo_reminder.cancel()
            await ctx.channel.send('Solo raid reminder stopped successfully!')
        else:
            await ctx.channel.send("You do not have the permission to stop the reminder. You only have the permission to switch it on or off. Please ask Mando_The_Mercenary#9484 to stop it.")

@solo.error
async def solo_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.channel.send("The command cannot be executed due to permission error. You need to have `Manage Server` and `Manage Channel` permissions in order to run this command. Kindly check and retry again with correct perms.")
    #await ctx.channel.send(f'\{txt[0]} \{txt[1]}')

@client.command()
@commands.has_permissions(administrator=True)
async def prefix(ctx,*, params: str = ""):
    global custom_prefixes
    if params == "":
        await ctx.channel.send(f"The prefix for this server is/ are: {custom_prefixes.get(str(ctx.guild.id), default_prefixes)}")
    else:
        stuff = params.split(" ")
        if stuff[0] == 'set':
            try:
                value = check_prefix_json(ctx.message.guild.id)
                if value == -1:
                    y = {"id": str(ctx.guild.id), "pre" : stuff[1]}
                    with open('prefix.json') as json_file: 
                        data = json.load(json_file) 
                    temp = data['prefix']
                    temp.append(y)
                    write_json_prefix(data)
                else:
                    with open('prefix.json') as json_file: 
                        data = json.load(json_file) 
                    temp = data['prefix']
                    temp[value]['id'] = str(ctx.guild.id)
                    temp[value]['pre'] = stuff[1]
                    write_json_prefix(data)
                await ctx.send(f"Prefixes set to {stuff[1]}.")
            except:
                value = check_prefix_json(ctx.message.guild.id)
                if value == -1:
                    y = {str(ctx.guild.id): default_prefixes}
                    with open('prefix.json') as json_file: 
                        data = json.load(json_file) 
                    temp = data['prefix']
                    temp.append(y)
                    write_json_prefix(data)
                else:
                    with open('prefix.json') as json_file: 
                        data = json.load(json_file) 
                    temp = data['prefix']
                    temp[value]['id'] = str(ctx.guild.id)
                    temp[value]['pre'] = default_prefixes
                    write_json_prefix(data)
                await ctx.send(f"Default prefixes set to {default_prefixes}.")
            
        if stuff[0] == 'reset':
            value = check_prefix_json(ctx.message.guild.id)
            if value == -1:
                await ctx.send(f"Prefix not set at all!")
            else:
                with open('prefix.json') as json_file: 
                    data = json.load(json_file) 
                temp = data['prefix']
                temp[value]['id'] = str(ctx.guild.id)
                temp[value]['pre'] = default_prefixes
                write_json_prefix(data)
                await ctx.send(f"Prefix reset to {default_prefixes}.")

@client.command(name='cooldown' , aliases = ['cd'])
async def cd(ctx, command: str):
    if command == 'start':
        value = check_jumpcd_json(ctx.message.author.id)
        if value == -1:
            y = {"id": ctx.message.author.id, "time_rem": 1900800}
            with open('jumpcd.json') as json_file: 
                data = json.load(json_file) 
            temp = data['jumpcd']
            temp.append(y)
            write_json_jumpcd(data)
            await ctx.channel.send('Cooldown reminder started successfully. Will DM you in 22 days!')
        else:
            with open('jumpcd.json') as json_file:
                data = json.load(json_file)

                temp = data['jumpcd']
                time_rem = []
                for t in temp:
                    time_rem.append(int(t['time_rem']))
                
                rem = time_rem[value]
            if rem == 0:
                value = check_jumpcd_json(ctx.message.author.id)
                with open('jumpcd.json') as json_file: 
                    data = json.load(json_file) 
                temp = data['jumpcd']
                temp[value]['time_rem'] = 1900800
                write_json_jumpcd(data)
                await ctx.channel.send('Cooldown reminder started successfully. Will DM you in 22 days!')
            else:
                await ctx.channel.send('Cooldown reminder already present! Type `i!cd status` to get the current status of cooldown.')
    if command == 'stop':
        value = check_jumpcd_json(ctx.message.author.id)
        if value == -1:
            await ctx.channel.send('**ERROR**! Cooldown reminder __not__ created. Check `i!cd start` to start the reminder.')
        else:
            value = check_jumpcd_json(ctx.message.author.id)
            with open('jumpcd.json') as json_file: 
                data = json.load(json_file) 
            temp = data['jumpcd']
            temp[value]['time_rem'] = 0
            write_json_jumpcd(data)
            await ctx.channel.send('Cooldown reminder stopped.')
    if command == 'status' or command == 'info':
        value = check_jumpcd_json(ctx.message.author.id)
        if value == -1:
            await ctx.channel.send('**ERROR**! Cooldown reminder __not__ created. Check `i!cd start` to start the reminder.')
        else:
            with open('jumpcd.json') as json_file:
                data = json.load(json_file)

                temp = data['jumpcd']
                time_rem = []
                for t in temp:
                    time_rem.append(int(t['time_rem']))
                
                rem = time_rem[value]
            
            days = rem // 86400
            hours = (rem - (days*86400)) // 3600
            minutes = (rem - (days*86400) - (hours*3600)) // 60
            
            await ctx.channel.send(f'I will remind you in {days} days, {hours} hours and {minutes} minutes.')

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