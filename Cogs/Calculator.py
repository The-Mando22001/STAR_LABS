import discord
from discord.ext import commands
import math

gear_cost = [0,0,20,60,120,200,300,420,560,740,960,1240,1560,1940,2380,2880,3520,4220,5000,5860,6820,7860,9000,10240,11580,13020,14580,16240,18020,19920,21960,24120,26420,28860,31440,34160,37040,40060,43240,46580,50100,54100,58280,62640,67200,71960,76900,82060,87420,92980,98760,104760,110980,117420,124100,131020,138160,145560,153200,161080,169220,177620,186280,195200,204380,213820,223520,233480,243700,254170,264900,]
artifact_silver = [0,0,5000,11500,20000,31000,45500,64000,88000,119500,160500]
artifact_gold = [0,0,8000,18000,32000,50000,73000,103000,142000,192000,257000]
artifact_legend = [0,0,12000,28000,48000,74000,108000,153000,211000,286000,384000]
xp_cost = [0,0,100,225,375,550,750,1000,1300,1650,2050,2500,3000,3550,4150,4800,5500,6250,7050,7900,8800,9750,10750,11800,12950,14200,15550,17000,18550,20200,22050,24200,26750,29800,33550,38300,44250,51700,60950,72200,85450,100700,117950,137200,158450,181700,206950,234200,263450,294700,327950,366200,409450,457700,510950,569200,637450,715700,803950,902200,1010450,1128700,1256950,1395200,1543450,1701700,1869950,2048200,2236450,2434700,2642950]
sp_cost_1 = [0,0,250,750,1500,2500,3750,5250,7000,9000,11250,13750,17050,21250,26450,32750,40250,48250,56750,65750,75250,85250,95750,106750,118250,130250,142750,155750,169250,183250,197750,212750,228250,244250,260750,277750,295250,313250,331750,350750,370250,390250,410750,431750,453250,475250,497750,520750,544250,568250,592750,617750,643250,669250,695750,722750,750250,778250,806750,835750,865250,895250,925750,956750,988250,1020250,1052750,1085750,1119250,1153250,1187750]
sp_cost_2 = [0,0,350,1050,2100,3500,5250,7350,9800,12600,15750,19250,23650,29050,35550,43250,52250,61850,72050,82850,94250,106250,118850,132050,145850,160250,175250,190850,207050,223850,241250,259250,277850,297050,316850,337250,358250,379850,402050,424850,448250,472250,496850,522050,547850,574250,601250,628850,657050,685850,715250,745250,775850,807050,838850,871250,904250,937850,972050,1006840,1042240,1078240,1114830,1152030,1189820,1228220,1267220,1306810,1347010,1387810,1429210]
sp_cost_3 = [0,0,500,1500,3000,5000,7500,10500,14000,18000,22500,27500,33600,40800,49300,59100,70400,82400,95200,108700,123000,138000,153800,170300,187590,205590,224380,243880,264170,285170,306960,329460,352750,376750,401540,427040,453330,480330,508120,536620,565910,595910,626700,658200,690490,723490,757280,791780,827070,863070,899860,937360,975650,1014650,1054440,1094940,1136230,1178230,1221020,1264520,1308810,1353810,1399600,1446100,1493390,1541390,1590180,1639680,1689970,1740970,1792760]


class Calculator(commands.Cog):
    def __init__(self, client):
        self.Bot = client

    @commands.command()
    async def gear(self, ctx, a: int = 0, b: int = 0):
        total = 0
        if a < b:
            total = gear_cost[b]-gear_cost[a]
            embed = discord.Embed(colour=discord.Colour(0x118d9e),
                                  description=f"""Here is the result.
```From level {a} to {b}\n\nAmount of gear material required:\n\nOne gear    - {total}\nTwo Gears   - {total*2}\nThree Gears - {total*3}\nFour Gears  - {total*4}\nFive Gears  - {total*5}```""")
            #embed.set_image(url="")
            embed.set_author(name="Gear Calculator", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)

            #await ctx.channel.send('first level is lower than second')
        elif (a==b) or (a==0 and b==0):
            embed = discord.Embed(colour=discord.Colour(0x118d9e),
                                  description=f"""Here is the result.
            ```From level {a} to {b}\n\nAmount of gear material required:\n\nOne gear    - {total}\nTwo Gears   - {total * 2}\nThree Gears - {total * 3}\nFour Gears  - {total * 4}\nFive Gears  - {total * 5}```""")
            # embed.set_image(url="")
            embed.set_author(name="Gear Calculator", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        else:
            embed = discord.Embed(colour=discord.Colour(0x118d9e),
                                  description=f"""Please make sure to check the 'from' and 'to' numbers provided. It should be,
            ```i!gear 1 20```\nNot,```i!gear 20 1```""")
            # embed.set_image(url="")
            embed.set_author(name="Gear Calculator", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)

    @commands.command()
    async def art(self, ctx, a: int = 0, b: int = 0):
        total = 0
        if a < b:
            total_silver = artifact_silver[b]-artifact_silver[a]
            total_gold = artifact_gold[b] - artifact_gold[a]
            total_legend = artifact_legend[b] - artifact_legend[a]
            embed = discord.Embed(colour=discord.Colour(0x118d9e),
                                  description="""Here are the results.""")
            embed.add_field(name="Silver Tier Artifacts",
                            value=f"Azure Artifacts```Amulet Of Tech, Amulet Of Might, Amulet Of Agility, Amulet Of Metahuman, Amulet Of Arcane\n\nAmount of azure material required is {total_silver}```Apokolips Artifacts```Mega Rod\n\nAmount of apokolips material required is {total_silver}```")
            embed.add_field(name="Gold Tier Artifacts",
                            value=f"Azure Artifacts```Claw Of Horus, Cosmic Staff, The All Blades\n\nAmount of azure material required is {total_gold}```Apokolips Artifacts```Electro Axe, Radion\n\nAmount of apokolips material required is {total_gold}```")
            embed.add_field(name="Legendary Tier Artifacts",
                            value=f"Azure Artifacts```Kryptonian Regeneration Matrix, Nth Metal Armor\n\nAmount of azure material required is {total_legend}```Apokolips Artifacts```Entropy Aegis, Heart Of Darkness, The Father Box\n\nAmount of apokolips material required is {total_legend}```")

            # embed.set_image(url="")
            embed.set_author(name="Artifact Calculator", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)

            # await ctx.channel.send('first level is lower than second')
        elif (a == b) or (a == 0 and b == 0):
            total_silver = artifact_silver[b] - artifact_silver[a]
            total_gold = artifact_gold[b] - artifact_gold[a]
            total_legend = artifact_legend[b] - artifact_legend[a]
            embed = discord.Embed(colour=discord.Colour(0x118d9e),
                                  description="""Here are the results.""")
            embed.add_field(name="Silver Tier Artifacts",
                            value=f"Azure Artifacts```Amulet Of Tech, Amulet Of Might, Amulet Of Agility, Amulet Of Metahuman, Amulet Of Arcane\n\nAmount of azure material required is {total_silver}```Apokolips Artifacts```Mega Rod\nAmount of apokolips material required is {total_silver}```")
            embed.add_field(name="Gold Tier Artifacts",
                            value=f"Azure Artifacts```Claw Of Horus, Cosmic Staff, The All Blades\n\nAmount of azure material required is {total_gold}```Apokolips Artifacts```Electro Axe, Radion\nAmount of apokolips material required is {total_gold}```")
            embed.add_field(name="Legendary Tier Artifacts",
                            value=f"Azure Artifacts```Kryptonian Regeneration Matrix, Nth Metal Armor\n\nAmount of azure material required is {total_legend}```Apokolips Artifacts```Entropy Aegis, Heart Of Darkness, The Father Box\nAmount of apokolips material required is {total_legend}```")

            # embed.set_image(url="")
            embed.set_author(name="Artifact Calculator", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)

        else:
            embed = discord.Embed(colour=discord.Colour(0x118d9e),
                                  description=f"""Please make sure to check the 'from' and 'to' numbers provided. It should be,
                    ```i!art 1 5```\nNot,```i!art 5 1```""")
            # embed.set_image(url="")
            embed.set_author(name="Artifact Calculator", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)

    @commands.command()
    async def xp(self, ctx, a: int = 0, b: int = 0):
        total_xp = 0
        t1, t2, t3, t4, t5, t6 = 0, 0, 0, 0, 0, 0
        m1, m2, m3, m4, m5, m6 = 0, 0, 0, 0, 0, 0
        if a < b:
            total_xp = xp_cost[b] - xp_cost[a]

            #Non Matching XP Calc
            if total_xp <= 450000:
                t6 = math.floor(total_xp / 1500)
            else:
                t6 = 300
            t5 = math.floor((total_xp - (t6 * 1500)) / 750)
            if t5 >= 300:
                t5 = 300
            t4 = math.floor((total_xp - (t6 * 1500) - (t5 * 750)) / 375)
            if t4 >= 300:
                t4 = 300
            t3 = math.floor((total_xp - (t6 * 1500) - (t5 * 750) - (t4 * 375)) / 100)
            if t3 >= 300:
                t3 = 300
            t2 = math.floor((total_xp - (t6 * 1500) - (t5 * 750) - (t4 * 375) - (t3 * 100)) / 50)
            if t2 >= 300:
                t2 = 300
            t1 = math.floor((total_xp - (t6 * 1500) - (t5 * 750) - (t4 * 375) - (t3 * 100) - (t2 * 50)) / 25)

            #Matching XP Calc
            if total_xp <= 900000:
                m6 = math.floor(total_xp / 3000)
            else:
                m6 = 300
            m5 = math.floor((total_xp - (m6 * 3000)) / 1500)
            if m5 >= 300:
                m5 = 300
            m4 = math.floor((total_xp - (m6 * 3000) - (m5 * 1500)) / 750)
            if m4 >= 300:
                m4 = 300
            m3 = math.floor((total_xp - (m6 * 3000) - (m5 * 1500) - (m4 * 750)) / 200)
            if m3 >= 300:
                m3 = 300
            m2 = math.floor((total_xp - (m6 * 3000) - (m5 * 1500) - (m4 * 750) - (m3 * 200)) / 100)
            if m2 >= 300:
                m2 = 300
            m1 = math.floor((total_xp - (m6 * 3000) - (m5 * 1500) - (m4 * 750) - (m3 * 200) - (m2 * 100)) / 50)

            embed = discord.Embed(colour=discord.Colour(0x118d9e),
                                  description=f"""Here is the result.
    ```From XP level {a} to {b}\n\nAmount of XP required: {total_xp}\n\nAmount of Non matching XP Capsules Required:\nTier 1 (25 XP per capsule)  : {t1}\nTier 2 (50 XP per capsule)  : {t2}\nTier 3 (100 XP per capsule) : {t3}\nTier 4 (375 XP per capsule) : {t4}\nTier 5 (750 XP per capsule) : {t5}\nTier 6 (1500 XP per capsule): {t6}\n\nAmount of Matching XP Capsules Required:\nTier 1 (50 XP per capsule)  : {m1}\nTier 2 (100 XP per capsule) : {m2}\nTier 3 (200 XP per capsule) : {m3}\nTier 4 (750 XP per capsule) : {m4}\nTier 5 (1500 XP per capsule): {m5}\nTier 6 (3000 XP per capsule): {m6}```""")
            # embed.set_image(url="")
            embed.set_author(name="XP Level Calculator", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)

            # await ctx.channel.send('first level is lower than second')
        else:
            embed = discord.Embed(colour=discord.Colour(0x118d9e),
                                  description=f"""Please make sure to check the 'from' and 'to' numbers provided. It should be,
                ```i!xp 1 20```\nNot,```i!xp 20 1```""")
            # embed.set_image(url="")
            embed.set_author(name="XP Level Calculator", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)

    @commands.command()
    async def sp(self, ctx, a: int = 0, b: int = 0):
        total_sp_1 = 0
        total_sp_2 = 0
        total_sp_3 = 0
        if a < b:
            total_sp_1 = sp_cost_1[b] - sp_cost_1[a]
            total_sp_2 = sp_cost_2[b] - sp_cost_2[a]
            total_sp_3 = sp_cost_3[b] - sp_cost_3[a]
            embed = discord.Embed(colour=discord.Colour(0x118d9e),
                                  description=f"""Here is the result.
        ```From Abilities Sp level {a} to {b}\n\nCost of the following are:\n\nSP1 - {total_sp_1}\nSP2 - {total_sp_2}\nSP3 - {total_sp_3}```""")
            # embed.set_image(url="")
            embed.set_author(name="SP Level Calculator", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)

            # await ctx.channel.send('first level is lower than second')
        else:
            embed = discord.Embed(colour=discord.Colour(0x118d9e),
                                  description=f"""Please make sure to check the 'from' and 'to' numbers provided. It should be,
                    ```i!sp 1 20```\nNot,```i!sp 20 1```""")
            # embed.set_image(url="")
            embed.set_author(name="SP Level Calculator", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)

def setup(client):
    client.add_cog(Calculator(client))