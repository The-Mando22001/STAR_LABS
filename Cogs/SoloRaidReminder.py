import discord
from discord.ext import commands, tasks

class SoloRaidReminder(commands.Cog):
    def __init__(self, client):
        self.Bot = client

    @commands.command(name='solo')
    async def solo_pip(self, ctx, cmd:str = None):
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
    async def start_spam_aftermath(self, channel):
        time_in = datetime.now(pytz.timezone('Asia/Kolkata'))
        count = time_in.strftime("%I.%M.%S")
        if count == '08.00.00':
            await channel.send('<@&776819305714810911> 30 mins early reminder pip refresh!! Play your pips before it expires!')
        if count == '08.30.00':
            await channel.send('<@&776819305714810911> pip refresh!! Enjoy your solo raid pips!')

    @tasks.loop(seconds=1)
    async def start_spam_rouge(self, channel):
        time_in = datetime.now(pytz.timezone('Asia/Kolkata'))
        count = time_in.strftime("%I.%M.%S")
        if count == '08.00.00':
            await channel.send('<@&776976184843698207> 30 mins early reminder pip refresh!! Play your pips before it expires!')
        if count == '08.30.00':
            await channel.send('<@&776976184843698207> pip refresh!! Enjoy your solo raid pips!')

    @tasks.loop(seconds=1)
    async def start_spam_eternity(self, channel):
        time_in = datetime.now(pytz.timezone('Asia/Kolkata'))
        count = time_in.strftime("%I.%M.%S")
        if count == '08.00.00':
            await channel.send('<@&694066334140465172> 30 min Solo Raid pip refresh reminder!!')
        if count == '08.30.00':
            await channel.send('<@&694066334140465172> Solo Raid pip refresh reminder!!')
    
    @tasks.loop(seconds=1)
    async def start_spam_haha(self, channel):
        time_in = datetime.now(pytz.timezone('Asia/Kolkata'))
        count = time_in.strftime("%I.%M.%S")
        if count == '08.00.00':
            await channel.send('<@&789562565071339561> 30 min Solo Raid pip refresh reminder!!')
        if count == '08.30.00':
            await channel.send('<@&789562565071339561> Solo Raid pip refresh reminder!!')

    @tasks.loop(seconds=1)
    async def start_spam_gotham(self, channel):
        time_in = datetime.now(pytz.timezone('Asia/Kolkata'))
        count = time_in.strftime("%I.%M.%S")
        if count == '08.00.00':
            await channel.send('<@&789533444328783892> 30 min Solo Raid pip refresh reminder!!')
        if count == '08.30.00':
            await channel.send('<@&789533444328783892> Solo Raid pip refresh reminder!!')

def setup(client):
    client.add_cog(SoloRaidReminder(client))