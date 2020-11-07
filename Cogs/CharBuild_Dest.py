import discord
from discord.ext import commands
from random import choice

class CharBuild(commands.Cog):
    def __init__(self, client):
        self.Bot = client

    @commands.guild_only()
    @commands.command(name='b', aliases=['build'])
    async def b(self, ctx, cmd: str= None):
        if cmd is None:
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
ssds - Suicide Squad Deadshot
```""")
            embed.add_field(name='🟨 Gold Characters (Others Part 2)', value="""```
grid - Grid
cbm - Classic Batman
eb - Enraged Bane
nw - Nightwing
psg - Powered Supergirl
cth - Cheetah
rdn - Raiden
ssdf - Soul Stealer Doctor Fate 
pst - Primal Swamp Thing
cc2 - Captain Cold
sbc - Sonic Black Canary
ubc - Unbreakable Cyborg
fs - Firestorm
uhq - Unhinged Harley Quinn```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")
            embed.set_image(url="")
            await ctx.channel.send(embed=embed)

        #Silvers
        if cmd == 'aww':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Tank Build - G60]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack       2,465
Health       49,552 
Defense    75 
CAD           150 
CAC           22 
LAC            1
FAC            1 
Stun resist    75
DOT resist    75
CAC resist    70```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙ GEARS", value="""```13 HEALTH, 2 DEF```""")
            embed.add_field(name="💎 FACTS", value="""```She gives 5% health to all female heroes in your roster```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Amazon Wonder Woman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'svbc' or cmd == 'sbc':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer Build - G60]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack            3,888
Health            23,285
Defense          70
CAD                294 
CAC                48 
LAC                 1 
FAC                46 
Stun resist     0 
DOT resist     0 
CAC resist     5 ```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 DEF, 1 CAC, 1 CAD```""")
            embed.add_field(name="⚙ GEARS", value="""```3 CAD, 1 CAC, 5 ATTACK, 3 FAC, 3 HEALTH```""")
            embed.add_field(name="💎 FACTS", value="""```Pair her with Silver Green Arrow for max FAC and silver bane for max CAC. It is necessary to have fast attack chance on her since she deals 150% fast attack damage.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Sonic/ Silver Black Canary", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'svcw':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer Build - G60]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack       3,544
Health       23,500
Defense    66 
CAD           292 
CAC           73 
LAC            1
FAC            6 
Stun resist    0 
DOT resist    0
CAC resist    0```""")
            embed.add_field(name="⚙ TALENTS", value="""```3 CAD, 3 CAC```""")
            embed.add_field(name="⚙ GEARS", value="""```3 DEF, 2 CAD, 1 CAC, 5 ATTACK, 4 HEALTH```""")
            embed.add_field(name="💎 FACTS", value="""```Her special 1 is DOT. You can also build her as a combo builder since she has great basics. Never use her down swipe attack!```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Catwoman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'svam':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack       6,222
Health       18,186
Defense     29 
CAD           300
CAC           75 
LAC            1
FAC            1
Stun resist    30 (passive) 
DOT resist    0
CAC resist    0 ```""")
            embed.add_field(name="⚙ TALENTS", value="""```3 CAC, 3 CAD```""")
            embed.add_field(name="⚙ GEARS", value="""```2 CAD, 1 CAC, 12 ATTACK```""")
            embed.add_field(name="💎 FACTS", value="""```Damage dealer for raids. He has a strong special 3 and can do good damage. You can have 3 defense effects in gears if you want. His passive gives 30% stun resist for team per might teammate and 20% team defense per metahuman teammate; thus when you use him with 2 might opponents the whole team will have max stun resist and when used with 2 metahuman teammates the whole team will have 40% defense.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Aquaman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'svc':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Tank Combo Build - G60]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack       2,129
Health       40,089
Defense    75 
CAD           150 
CAC           22 
LAC            1
FAC            61 
Stun resist    75
DOT resist    75
CAC resist    70```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙ GEARS", value="""```2 DEF, 4 FAC, 9 HEALTH```""")
            embed.add_field(name="💎 FACTS", value="""```Silver cyborg is one of the best tanks in the game. His passive allows him to heal slowly after tagging out and to maximize his healing we have him as a tank. Use the metahuman artifact on him to improve his healing further. We have fast attack chance on him since he has good basics. You can also build him as a full tank.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Cyborg", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'svf':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Tank Combo Build - G60]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack            3,534
Health            35,785
Defense         75 
CAD               150
CAC               22 
LAC                1
FAC                21 
Stun resist     75
DOT resist     75 
CAC resist     70 ```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙ GEARS", value="""```2 DEF, 1 FAC, 4 ATTACk, 8 HEALTH```""")
            embed.add_field(name="💎 FACTS", value="""```Silver flash gives 20% fast attack chance to himself and his teammates. He also gains fast attack chance on tag in so we don't need to have extra effects in gears.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Flash", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'svj':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer Build - G60]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack       4,331
Health       23,882
Defense    66 
CAD           300 
CAC           73 
LAC            1
FAC            1 
Stun resist    0 
DOT resist    0
CAC resist    0```""")
            embed.add_field(name="⚙ TALENTS", value="""```3 CAD, 3 CAC```""")
            embed.add_field(name="⚙ GEARS", value="""```3 DEF, 2 CAD, 1 CAC, 6 ATTACK, 3 HEALTH```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Joker", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)

        if cmd == 'svhq':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer Build - G60]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack          3,344 (173 from her passive)
Health          16,787
Defense        69 
CAD              279
CAC              75 
LAC                1
FAC                61 
Stun resist    0
DOT resist    0
CAC resist    0```""")
            embed.add_field(name="⚙ TALENTS", value="""```1 CAD, 1 CAC, 4 DEF```""")
            embed.add_field(name="⚙ GEARS", value="""```3 CAD, 3 CAC, 4 ATTACK, 4 FAC, 1 HEALTH```""")
            embed.add_field(name="💎 FACTS", value="""```She gives 10% attack to herself and teammates. She also deals 100% damage on swipe attacks so we have fast attack chance to take advantage of it.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Harley Quinn", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'svst':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Mix Build - G60]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack       3,543
Health       37,777
Defense    65 
CAD           150 
CAC           22 
LAC            1
FAC            1 
Stun resist    75
DOT resist    75
CAC resist    70```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙ GEARS", value="""```1 DEF, 7 ATTACK, 7 DEF```""")
            embed.add_field(name="💎 FACTS", value="""```Silver Swamp Thing healing is based on how much attack he has. Use him with all blades or metahuman artifact to improve his healing.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Swamp Thing", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'svgg':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Tank Build - G60]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack       1,937
Health       52,589
Defense    65 
CAD           150 
CAC           22 
LAC            1
FAC            1 
Stun resist    75
DOT resist    75
CAC resist    70```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙ GEARS", value="""```1 DEF, 14 HEALTH```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Gorilla Grodd", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'svb':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Tank Combo Build - G60]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack      2,402
Health      40,673
Defense    75
CAD           150 
CAC           22
LAC            1 
FAC            61 
Stun resist  75 
DOT resist    75 
CAC resist 70```""")
            embed.add_field(name="⚙ TALENTS", value="""``````""")
            embed.add_field(name="⚙ GEARS", value="""``````""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Bane", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'svds':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer Build - G60]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack       4,198
Health       19,940
Defense    66 
CAD           292 
CAC           75 
LAC            1
FAC            1 
Stun resist    0
DOT resist    0
CAC resist    0```""")
            embed.add_field(name="⚙ TALENTS", value="""```3 CAD, 3 CAC```""")
            embed.add_field(name="⚙ GEARS", value="""```3 DEF, 1 CAC, 2 CAD, 7 ATTACK, 2 HEALTH```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Deadshot", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'svsc':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Tank Build - G60]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack       2,359
Health       46,787
Defense    75 
CAD           160 
CAC           22 
LAC            1
FAC            1 
Stun resist    75
DOT resist    75
CAC resist    70```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙ GEARS", value="""```2 DEF, 13 HEALTH```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Scarecrow", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'svr':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Tank Combo Build - G60]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack      2,724
Health      42,480
Defense    75 
CAD       150
CAC        22 
LAC        1
FAC        71 
Stun resist   75 
DOT resist   75 
CAC resist   70```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙ GEARS", value="""```9 HEALTH, 2 DEF, 4 FAC```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Robin", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'svdf':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Tank Combo Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack      2,551
Health      41,386
Defense      75 
CAD         150
CAC          25
LAC           1
FAC          69
Stun resist  75
DOT resist   75
CAC resist   70
BE           49```""")
            embed.add_field(name="⚙ TALENTS", value="""```2 BE, 4 RES```""")
            embed.add_field(name="⚙ GEARS", value="""```4 FAC, 8 HEALTH, 3 DEF```""")
            embed.add_field(name="💎 FACTS", value="""```One of the best support characters in the game, silver doctor fate is a good combo builder and support. We have 2 block effectiveness talents to reduce damage from armor-piercing specials of brainiac in phase 3.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Doctor Fate", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'svga':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack         6,901
Health        18,276
Defense     24 
CAD              300 
CAC              43 
LAC                1
FAC                1
Stun resist    0
DOT resist    0
CAC resist    0```""")
            embed.add_field(name="⚙ TALENTS", value="""```5 CAD, 1 CAC```""")
            embed.add_field(name="⚙ GEARS", value="""```15 ATTACK```""")
            embed.add_field(name="💎 FACTS", value="""```Use silver bane as a combo builder and to max his critical attack chance. You can also use black canary as she provides 25% CAC to green arrow. He has a high damage special 3.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Green Arrow", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'svww':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Tank Build - G60]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack       2,379
Health       47,286
Defense    75 
CAD           160 
CAC           22 
LAC            1
FAC            1 
Stun resist    75
DOT resist    75
CAC resist    70```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙ GEARS", value="""```2 DEF, 13 HEALTH```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Wonder Woman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'svsm':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Tank Combo Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack  2,275
Health  49,203
Defense    75 
CAD    150
CAC     25
LAC     1
FAC     69
Stun resist   75
DOT resist   75
CAC resist   70```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙ GEARS", value="""```10 HEALTH, 4 FAC, 1 DEF```""")
            embed.add_field(name="💎 FACTS", value="""```Silver Superman has a 50% chance to ignore opponent basic attacks. Recommended artifacts: Nth Metal Armor, Kryptonian Regeneration Matrix, and Cosmic Staff.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Superman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'svgl':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Tank Combo Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack       2,659
Health       45,227
Defense    75 
CAD   150
CAC    25
LAC    1
FAC     61
Stun resist   75
DOT resist   75
CAC resist   70```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙ GEARS", value="""```9 HEALTH, 2 DEF, 4 FAC```""")
            embed.add_field(name="💎 FACTS", value="""```Silver lantern is a good combo builder and tank as his passive gives a shield of 25%; hence, the more health he has the more his shield can withstand.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Green Lantern", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'svbm':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack       6,095
Health       17,284
Defense     24 
CAD           300 
CAC           58 (passive 20% maxes CAC) 
LAC            1
FAC            1
Stun resist    0
DOT resist    0
CAC resist    0 ```""")
            embed.add_field(name="⚙ TALENTS", value="""```3 CAC, 3 CAD```""")
            embed.add_field(name="⚙ GEARS", value="""```13 ATTACK, 1 CAC, 1 CAD```""")
            embed.add_field(name="💎 FACTS", value="""```Silver Batman has the highest special 3 damage in the game. He's an excellent damage dealer. You can also drop the CAD and add one more attack when you use MVF as a combo builder. The best team for him in raids would be Justice League Superman and another batman (AKBM or JLBM preferably).```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Batman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)

        #Legendaries
        if cmd == 'akbm':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack       7,689
Health       27,652
Defense     24 
CAD           300 
CAC           73
LAC            1
FAC            1
Stun resist    0
DOT resist    0
CAC resist    0 ```""")
            embed.add_field(name="⚙ TALENTS", value="""```3 CAC, 2 CAD, 1 ATTACK```""")
            embed.add_field(name="⚙ GEARS", value="""```2 CAD, 13 ATTACK```""")
            embed.add_field(name="⚡ [Tank Combo Build - G70]\n⚙ STATS", value="""```Attack       4,666
Health       50,852
Defense     24 
CAD           175 
CAC           37 
LAC            1
FAC            69 
Stun resist    75 
DOT resist    75
CAC resist    70
BE            49```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 RES, 2 BE```""")
            embed.add_field(name="⚙ GEARS", value="""```8 HEALTH, 3 ATTACK, 4 FAC```""")
            embed.add_field(name="💎 FACTS", value="""```Since AKBM passive gives max defense and a ton of health he can be easily built as a damage dealer. If you use him in raids the best team for him would be justice League Superman and Justice League Batman. He also gets 20% attack and 20% health from classic Batman.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Arkham Knight Batman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'bm':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack 4,564
Health  26,639
Defense  34%
CAD    300%
CAC     69%
FAC     75%
AP       96%
Stun resist  0%
DOT resist  0%
CAC resist  0%```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 AP, 2 CAC```""")
            embed.add_field(name="⚙ GEARS", value="""```4 ATTACK, 5 FAC, 2 CAC, 4 CAD```""")
            embed.add_field(name="💎 FACTS", value="""```The best team for BM is Brainiac & Justice League Flash (this team does well vs GG and HSC). However, another great pip for BM is vs P4 (it’s loads of fun) and your team with him should be: Brainiac and AGA. With this pip, BM has TAB equipped and AGA tagging in and out to power drain/lock P4 Brainiac.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Black Manta", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'bnc':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Tank/Support Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack     3,523 ♞
Health     60,600 ♥️
Defense    75%
CAD        150
CAC        25
LAC         49  (1.5x LAC contributed to legendary and hacked teammates)
FAC        11
Stun resist   60
DOT resist    60
CAC resist    60```""")
            embed.add_field(name="⚙ TALENTS", value="""```3 RES, 3 DEF```""")
            embed.add_field(name="⚙ GEARS", value="""```12 HEALTH, 2 LAC, 1 DEF```""")
            embed.add_field(name="💎 FACTS", value="""```The Brainiac is only useful as support to other legendary characters, or as a Tank for the arena. 
Side note: teamed with manta be sure to add 3 slots of lethal to brainiacs gear so manta gets 75% of it. 
Suggested teammates: Black Manta, DS, AKBM.
Suggested artifact: NTH Armor.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Brainiac", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'bngg':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack     4,673
Health     33,496
Defense    44 - Defense is not strictly needed as he reduces incoming damage and heals with health below 30%! 
CAD        300
CAC        75
LAC         56
FAC         69
Stun resist   0
DOT resist    0
CAC resist    0```""")
            embed.add_field(name="⚙ TALENTS", value="""```5 CAD, 1 LAC```""")
            embed.add_field(name="⚙ GEARS", value="""```5 ATTACK, 4 FAC, 2 LAC, 3 CAC, 1 CAD```""")
            embed.add_field(name="💎 FACTS", value="""```In the Batman Ninja Team, BNR can be used to not only build combo (tag-in combo too) but also blind his enemies; moreover, BNC can be used for obtaining health, lethal boost, and attack. BNGG's first special deals +150.05% damage to blinded opponents at level 70! Also, BNGGe can be one of the best combo builders outside of the BN team legendary team, or on a SHAZAM, KOA team because he can build up the power bar while building a combo because of his passive.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Batman Ninja Gorilla Grodd", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'ds':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Tank Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack    3235
Health    76,854
Defense    75%
LAC 15% (Base)
Stun resist   72%
DOT resist   60%
CAC resist    60%```""")
            embed.add_field(name="⚙ TALENTS", value="""```3 DEF, 3 RES```""")
            embed.add_field(name="⚙ GEARS", value="""```15 HEALTH```""")
            embed.add_field(name="⚡ [Damage Dealer Build - G70]\n⚙ STATS", value="""```Attack    5,555
Health    33,355
DEF 39% (Base)
CAD 300%
CAC 75%
FAC 69%
LAC 15% (Base)```""")
            embed.add_field(name="⚙ TALENTS", value="""```3 CAC, 3 CAD```""")
            embed.add_field(name="⚙ GEARS", value="""```8 ATTACK, 4 FAC, 2 CAD, 1 CAC```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Darkseid", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'jls':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack   5119
Health  26,500
CAD        294%
CAC        71%
FAC        69%
AP          96%```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 AP, 1 CAC, 1 CAD```""")
            embed.add_field(name="⚙ GEARS", value="""```6 ATTACK, 4 FAC, 3 CAD, 2 CAC```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Justice League Superman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'sshq':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer/Support Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack  5,550
Health  41,990
Defense  75%
CAD  270%
CAC  37%
LAC  11% 
FAC  52%
Stun resist 40%
DOT resist  40%
CAC resist  40%```""")
            embed.add_field(name="⚙ TALENTS", value="""```2 RES, 2 AP, 1 CAC, 1 ATTACK```""")
            embed.add_field(name="⚙ GEARS", value="""```3 CAD, 7 ATTACK, 3 CAC, 2 DEF```""")
            embed.add_field(name="💎 FACTS", value="""```SSHQ can be very dangerous when teamed up with her other SS teammates. The Suicide Squad is mainly an arena team, but her passives that strip multiple percentages of opponents stats can allow you to decimate a team. Additionally, she does not need much CAC as her other passive when teamed with SSDS it gives her +50% CAC.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Suicide Squad Harley Quinn", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'sse':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Support Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack  6,280
Health  26,074
Defense  75
CAD  190
CAC   75
LAC   13
FAC   35
Stun resist   10
DOT resist    20
CAC resist    20```""")
            embed.add_field(name="⚙ TALENTS", value="""```2 AP, 2 CAC, 1 ATTACK, 1 LAC```""")
            embed.add_field(name="⚙ GEARS", value="""```8 ATTACK, 3 DEF, 1 CAC, 1 CAD, 2 FAC```""")
            embed.add_field(name="💎 FACTS", value="""```Suicide Squad Enchantress (SSE) can be a multi-useful character though she's more an Arena-based character that's best used with her team: The Suicide Squad (SSDS, SSHQ) as the main damage dealer (DD). However, she can also be very useful when she is teamed up with other legendary characters as a support/healer/combo builder due to the fact that she is the fastest charter in the game.```""")

            embed.add_field(name="⚡ [Damage Dealer Build - G70]\n⚙ STATS", value="""```Attack  6,860
Health  26,074
Defense  24
CAD  300
CAC   75
LAC   13
FAC   1
Stun resist   10
DOT resist    20
CAC resist    20```""")
            embed.add_field(name="⚙ TALENTS", value="""```2 AP, 2 CAC, 1 ATTACK, 1 LAC```""")
            embed.add_field(name="⚙ GEARS", value="""```10 ATTACK, 4 CAD, 1 CAC```""")
            embed.add_field(name="💎 FACTS", value="""```When SSE is paired with her team, The Suicide Squad, she can be a very dangerous character if built this way. Using her passives that heal her and her SP3 gives her an immortality "dome" which allows her to deal lots of damage safely if used correctly in battle.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Suicide Squad Enchantress", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'mmh':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Coming Soon```""")
            embed.add_field(name="⚙ TALENTS", value="""```Coming Soon```""")
            embed.add_field(name="⚙ GEARS", value="""```Coming Soon```""")
            embed.add_field(name="💎 FACTS", value="""```Coming Soon```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Martian Manhunter", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)

        #Gold Batman Ninjas
        if cmd == 'bnbm':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer Build - G60]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack       4,702 
Health       29,880 
Defense    74 
BE              49 
CAD         270 
CAC         35
FAC          61 
Stun resist   0
DOT resist    0
CAC resist    0```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 DEF, 2 BE```""")
            embed.add_field(name="⚙ GEARS", value="""```5 ATTACK, 4 FAC, 3 CAD, 3 HEALTH```""")
            embed.add_field(name="💎 FACTS", value="""```Batman Ninja Batman gets full critical attack chance and armor Pierce on basics and specials when he's hit by crit or AP attack. So we don't have CAC on him since we are utilizing his passive. We also have fast attack chance for higher combos and utilize his ap passive. Block effectiveness is to reduce damage from AP attacks. He's not an ideal damage dealer for raids.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Batman Ninja Batman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'bnhq':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Tank Combo Build - G60]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack       2,849
Health       38,688
Defense     65 
CAD           150 
CAC           22
LAC            60 
FAC            61 
Stun resist    75 
DOT resist    75 
CAC resist    70```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙ GEARS", value="""```6 HEALTH, 4 FAC, 4 LAC, 1 DEF```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Batman Ninja Harley Quinn", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'bncw':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack  5346
Health 25252
Defense 29
CAD 300
CAC  70
FAC  75
LAC  18
Stun resist   0
DOT resist    0
CAC resist    0```""")
            embed.add_field(name="⚙ TALENTS", value="""```3 CAC, 3 CAD```""")
            embed.add_field(name="⚙ GEARS", value="""```8 ATTACK, 4 FAC, 2 CAD, 1 LAC```""")
            embed.add_field(name="💎 FACTS", value="""```Bncw is a very good character to play on her own with claws of horus. When partnered with bngg, and bnr, she can do a massive amount of damage. It is very important to keep her attacks going, and stopping as little as possible. This is to maximize the bnr stack. I added a lethal attack roll to the build, so that she gains a small edge in arena, but if u want to build her solely for raids, build her with attack rather than lethal. She is meant to spam combos and sp3s, and keep an ongoing sp2 dot going throughout the game. (roughly one sp2 per 3-5 sp3s)```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Batman Ninja Catwoman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'bnr':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack 5465(4716+30% from bnhq)
Health  24196
Defense 29
CAD  300
CAC   73
LAC   59
FAC   62
Stun resist   0
DOT resist    0
CAC resist    10 ```""")
            embed.add_field(name="⚙ TALENTS", value="""```2 LAC, 4 CAC```""")
            embed.add_field(name="⚙ GEARS", value="""```6 ATTACK, 4 CAD, 3 FAC, 2 LAC```""")
            embed.add_field(name="💎 FACTS", value="""```BNR, or Batman Ninja Robin, is key to the ninja team. He gives various buffs to his teammates like a combo meter which starts at 7 hits, lethal attack damage per lethal hit, and 30% lac when the opponent is blinded and misses a basic attack on you. Robin's main damage comes from his 30% LAD every 14 seconds and it stacks; hence, it is essential to build him and his fellow teammates with LAC and FAC to take full advantage of his passives and deal massive damage in raids. This build serves as both a damage dealer and a combo builder for BNGG when he is built as a damage dealer.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Batman Ninja Robin", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'bnlj':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack       4,841
Health       22,660
Defense     24 
CAD           300 
CAC           75 
LAC            60
FAC            69 
Stun resist    0
DOT resist    15 
CAC resist    0 ```""")
            embed.add_field(name="⚙ TALENTS", value="""```3 CAC, 3 CAD```""")
            embed.add_field(name="⚙ GEARS", value="""```5 ATTACK, 4 FAC, 3 CAD, 3 LAC```""")
            embed.add_field(name="💎 FACTS", value="""```Pair with BNR & BNGG. His special 3 costs only 4 power bars and does great damage. ```""")
            embed.add_field(name="⚡ [Support Build - G60]\n⚙ STATS", value="""```Attack       3,341
Health       44,160
Defense     75 
CAD           150 
CAC           22 
LAC            10
FAC            61
Stun resist    75
DOT resist    75 
CAC resist    70```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙ GEARS", value="""```9 HEALTH, 4 FAC, 2 DEF```""")
            embed.add_field(name="💎 FACTS", value="""```BNLJ is a great support character as well and can revive your teammates and himself twice when the opposite team has a Batman. Hence, he is very handy in any team, especially against Arkham Knight Batman. We have FAC since he has good basic attacks. You can replace them with health if you want.```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Batman Ninja Lord Joker", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)

        #Multiverse Gang
        if cmd == 'mvbw':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Non-MV Team Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack  6,001
Health  22,660
Defense  24%
CAD  290%
CAC  75%
LAC  1%
FAC  1%
Stun resist 60%
DOT resist 60%
CAC resist 60%```""")
            embed.add_field(name="⚙ TALENTS", value="""```3 AP, 3 RES```""")
            embed.add_field(name="⚙ GEARS", value="""```3 CAD, 3 CAC, 9 ATTACK```""")
            embed.add_field(name="💎 FACTS", value="""```Suggested to team with AKBM to cover her defense and healing/power boosts, and MVCC for his buffers to power up her attack
 
MVBW is a very dangerous and fun character to use in the arenas with this build. She has a lot going for her. Start by doing a few of MVCCs spls and get his buffers going. She does added damage for each MV team buffer. her SP3 fully powered up can reach 3mil this way. also take advantage of her SP1 for a chance for free SP3s.```""")
            embed.add_field(name="⚡ [Damage Dealer/Support Build - G70]\n⚙ STATS", value="""```Attack  8,375
Health  22,660
Defense  24%
CAD  170%
CAC  25%
LAC  1%
FAC  1%
Stun resist 0%
DOT resist 0%
CAC resist 0%```""")
            embed.add_field(name="⚙ TALENTS", value="""```6 ATTACK```""")
            embed.add_field(name="⚙ GEARS", value="""```15 ATTACK```""")
            embed.add_field(name="💎 FACTS", value="""```Suggested Team: mvbw, mvf and mvasg
Suggested Artifacts: The All-Blades or Claw of Horus

MVBW when teamed with these 2 teammates is when she's at her most dangerous! She makes an excellent 2nd/alternate DD/Support to ASG.  A lot of players sleep on her potential. Don't be one of them. Give her a try she's dangerous and fun to use in the arenas, and raids with this build.

MVF will add all the CAC, and CAD she needs, and ASG with her SP2, and SP3 not only adds to her defensive/offensive stats but they will also increase her special moves damage for each active MV buffer. Her other passives also are extremely helpful. A chance to keep your combo if broken by getting hit, a unique buffer slowing passive, and her SP1 gives you a chance at a free SP3. Very versatile! ```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Multiverse Batwoman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'mvf':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[High Damage Combo Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack     5500
Health     23428
Defense    75
CAD        230
CAC        25
FAC        75
Stun resist   60
DOT resist    60
CAC resist    70```""")
            embed.add_field(name="⚙ TALENTS", value="""```3 DEF, 3 RES```""")
            embed.add_field(name="⚙ GEARS", value="""```8 ATTACK, 2 CAD, 1 DEF, 4 FAC```""")
            embed.add_field(name="💎 FACTS", value="""```MVF is a very good combo builder, especially when paired with MVASG against CC. Aside from the Justice League team, he has some of the strongest basics in the game! He is one of the only characters who can have maxed out crit, fast attack, and defense, all while keeping a high attack! Newer players might want to play him with claws of hours, while more experienced players can use all blades.```""")
            embed.add_field(name="⚡ [Damage Dealer Build - G70]\n⚙ STATS", value="""```Attack       7,933
Health       23,428
Defense    24
CAD           270 
CAC           25 
LAC            1 
FAC            1 
Stun resist    0
DOT resist    0
CAC resist    0```""")
            embed.add_field(name="⚙ TALENTS", value="""```5 CAD, 1 ATTACK```""")
            embed.add_field(name="⚙ GEARS", value="""```15 ATTACK```""")
            embed.add_field(name="💎 FACTS", value="""```Damage dealer build for raids. You can have defense in gears if you want. His passive maxes his critical attack chance and also gives 45% critical attack damage.```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Multiverse Flash", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'mvbl':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Tank Support Build - G60]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack      4,375
Health      41,224
Defense    75 
CAD       150
CAC        22
LAC        1
FAC        1 
Stun resist   75
DOT resist   75
CAC resist   70```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙ GEARS", value="""```7 HEALTH, 6 ATTACK, 2 DEF```""")
            embed.add_field(name="💎 FACTS", value="""```Mixed build for arena and champions arena. He's an annoying character in the defensive team. We have some attack to deal good damage with his special 2 and 3. Use all blades or claw of horus to deal good damage. If you're using him in a defensive team equip cosmic staff on him.```""")
            embed.add_field(name="⚡ [Damage Dealer Build - G70]\n⚙ STATS", value="""```Attack       6,695
Health       24,724
Defense    75 
CAD       262 
CAC       25 
LAC        1
FAC        1
Stun resist    0
DOT resist    0
CAC resist    0 ```""")
            embed.add_field(name="⚙ TALENTS", value="""```3 DEF, 3 CAD```""")
            embed.add_field(name="⚙ GEARS", value="""```13 ATTACK, 1 CAD, 1 DEF```""")
            embed.add_field(name="💎 FACTS", value="""```Damage dealer build for raids. Pair with MVF for max critical attack chance and damage. He has a great special 2 and armor-piercing special 3. Defense effect on gear is just for maxing defense, you can switch it to attack if you want.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Multiverse Black Lightning", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'mvga':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack       7,583
Health       25,252
Defense     24 
CAD           270 
CAC           44 
LAC            1
FAC            1
Stun resist    0
DOT resist    0
CAC resist    0 ```""")
            embed.add_field(name="⚙ TALENTS", value="""```5 CAD, 1 ATTACK```""")
            embed.add_field(name="⚙ GEARS", value="""```15 ATTACK```""")
            embed.add_field(name="💎 FACTS", value="""```Damage dealer build for raids. Pair with MVF for max CAC and CAD.```""")
            embed.add_field(name="⚡ [Support Build - G70]\n⚙ STATS", value="""```Attack       4,827
Health       39,252
Defense     75 
CAD           150 
CAC           44 
LAC            1
FAC            1
Stun resist    75 
DOT resist    75 
CAC resist    70```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙ GEARS", value="""```7 ATTACK, 6 HEALTH, 2 DEF```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Multiverse Green Arrow", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'mvwc':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack       7,824
Health       21,664
Defense    24
CAD           270 
CAC           36 
LAC            1 
FAC            1 
Stun resist    0
DOT resist    0
CAC resist    10```""")
            embed.add_field(name="⚙ TALENTS", value="""```5 CAD, 1 ATTACK```""")
            embed.add_field(name="⚙ GEARS", value="""```15 ATTACK```""")
            embed.add_field(name="💎 FACTS", value="""```Damage dealer build for raids. Pair with MVF for max critical attack chance and damage.```""")
            embed.add_field(name="⚡ [Support Build - G60]\n⚙ STATS", value="""```Attack       5,202
Health       35,664
Defense    75 
CAD           150 
CAC           36 
LAC            1 
FAC            1 
Stun resist    75
DOT resist    75 
CAC resist    70 ```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙ GEARS", value="""```7 ATTACK, 6 HEALTH, 2 DEF```""")
            embed.add_field(name="💎 FACTS", value="""```Mixed build for arena and champions arena. If u use her with akbm remove defense and some health and add CAC and CAD.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Multiverse White Canary", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'mvcc':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack    7,187
Health   24,988
Defense    65
CAD       262 
CAC       25 
LAC        1
FAC        1
Stun resist    10 
DOT resist    0
CAC resist    0 ```""")
            embed.add_field(name="⚙ TALENTS", value="""```3 DEF, 3 CAD```""")
            embed.add_field(name="⚙ GEARS", value="""```1 CAD, 14 ATTACK```""")
            embed.add_field(name="💎 FACTS", value="""```Damage dealer build for raids. Pair with MVF for max critical attack chance and damage. ```""")
            embed.add_field(name="⚡ [Tank Support Build - G60]\n⚙ STATS", value="""```Attack    4,577
Health   43,988
Defense     72( +5% base defense) 
CAD       150
CAC        25 
LAC        1
FAC        1 
Stun resist   75
DOT resist   75
CAC resist   70```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙ GEARS", value="""```8 HEALTH, 6 ATTACK, 1 DEF```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Multiverse Captain Cold", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'mvsg':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack       6,947
Health       24,196
Defense    68 (53% + 15% from passive) 
CAD        250 
CAC        25 
LAC        1
FAC        1
Stun resist    75 
DOT resist    75 
CAC resist    70```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙ GEARS", value="""```13 ATTACK, 2 CAD```""")
            embed.add_field(name="💎 FACTS", value="""```Damage dealer build for raids. Pair with MVF for max critical attack chance and damage. You can also have attack talents if you want. ```""")
            embed.add_field(name="⚡ [Support Build - G60]\n⚙ STATS", value="""```Attack       4,627
Health       40,696
Defense    71(51+5% base+15% passive) 
CAD       170 
CAC        22 
LAC        1
FAC        1
Stun resist    72 
DOT resist    72 
CAC resist    70```""")
            embed.add_field(name="⚙ TALENTS", value="""```6 RES```""")
            embed.add_field(name="⚙ GEARS", value="""```6 ATTACK, 7 HEALTH, 2 DEF```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Multiverse Supergirl", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'mvasg':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack   7,577
Health   26,308
Defense   70%
CAD    170%
CAC     25%
FAC     1%
Stun resist   60%
DOT resist   70%
CAC resist    70%```""")
            embed.add_field(name="⚙ TALENTS", value="""```3 RES, 3 DEF```""")
            embed.add_field(name="⚙ GEARS", value="""```15 ATTACK```""")
            embed.add_field(name="💎 FACTS", value="""```One of the great damage dealers in raids.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Multiverse Armored Supergirl", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)

        #The Justice League
        if cmd == 'jlc':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[CB/Damage Dealer Build W/ JLF- G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack      4881
Health     23108
Defense    48 
CAD        294
CAC         75
FAC        75
Stun resist   0 - 100% (passive)
DOT resist    10
CAC resist    0```""")
            embed.add_field(name="⚙ TALENTS", value="""```3 CAC, 2 DEF, 1 CAD```""")
            embed.add_field(name="⚙ GEARS", value="""```7 ATTACK, 3 CAD, 4 FAC, 1 CAC```""")
            embed.add_field(name="💎 FACTS", value="""```JLC is meant to be played alongside JLF and JLAM for maximum damage. When playing this way, both JLC and JLF are the dmg dealers as well as the combo builders. when shear power is needed, it is best to use JLF's SP3. When power drain is needed, it is best to use JLC SP2.```""")
            embed.add_field(name="⚡ [P2 Damage Dealer - G70]\n⚙ STATS", value="""```Attack        5,461
Health        29,108
Defense     73 
CAD           150
CAC           25 
LAC            1
FAC            75 
Stun resist    0
DOT resist    0
CAC resist    0 
BE                   49 ```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 DEF, 2 BE```""")
            embed.add_field(name="⚙ GEARS", value="""```9 ATTACK, 4 FAC, 2 HEALTH```""")
            embed.add_field(name="💎 FACTS", value="""```JLC can do decent damage in phase 2 and can be a useful cleanup pip especially in tier 7/8 raids. To be used with claw of horus artifact. Suggested teams would be with JLF and DF/PG. You can also use silver or speedforce the flash for FAC and have extra attack in gears.```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Justice League Cyborg", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'jlf':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[CB/Damage Dealer Build w/ JLC - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack     5395
Health     22420
Defense    48
CAD        294
CAC        75
FAC        75
Stun resist   0
DOT resist    0
CAC resist    0```""")
            embed.add_field(name="⚙ TALENTS", value="""```2 DEF, 1 CAD, 3 CAC```""")
            embed.add_field(name="⚙ GEARS", value="""```7 ATTACK, 3 CAC, 4 FAC, 1 CAD```""")
            embed.add_field(name="💎 FACTS", value="""```JLF is meant to be played alongside JLC and JLAM for maximum dmg. When playing this way, both JLC and JLF are the dmg dealers as well as the combo builders. when shear power is needed, it is best to use JLF sp3. When power drain is needed, it is best to use JLC sp2```""")
            embed.add_field(name="⚡ [Damage Dealer Build - G70]\n⚙ STATS", value="""```Attack            5,685
Health            22,420
Defense         24 
CAD               300 
CAC               75 
LAC                1
FAC                75 
Stun resist     0
DOT resist     0
CAC resist     0 ```""")
            embed.add_field(name="⚙ TALENTS", value="""```3 CAD, 3 CAC```""")
            embed.add_field(name="⚙ GEARS", value="""```8 ATTACK, 3 CAC, 4 FAC```""")
            embed.add_field(name="💎 FACTS", value="""```Damage dealer build for raids. You can also have 3 defense effects in gear if you want (his attack will be 4815 with max defense). Pair him with Justice League Cyborg and Justice League Aquaman to deal massive damage.```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Justice League Flash", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'jla':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Support Build - G60]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack      4,301
Health     34,898
Defense    75 
CAD       150
CAC        22 
LAC        1
FAC        61 
Stun resist   75 
DOT resist   75 
CAC resist   70```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙ GEARS", value="""```5 ATTACK, 5 HEALTH, 4 FAC, 1 DEF```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Justice League Aquaman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'jlb':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Support Build - G60]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack       4,029
Health      36,876
Defense    75 
CAD       150
CAC        26 
LAC        1
FAC        61 
Stun resist   75 
DOT resist   75 
CAC resist   70```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙ GEARS", value="""```5 HEALTH, 4 ATTACK, 4 FAC, 2 DEF```""")
            embed.add_field(name="💎 FACTS", value="""```When used with Justice League Superman as a combo builder, you can replace all attack effects with health. We have some attack so his basics can hit hard with cyborg or Superman. He also gets 20% attack and 20% health from classic Batman.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Justice League Batman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'mww':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[TAB Hybrid Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack  4,661
Health  19,972
Defense  70
CAD    298 
CAC     75
LAC     1 
FAC      69
Stun resist  60 
DOT resist    60 
CAC resist 60 ```""")
            embed.add_field(name="⚙ TALENTS", value="""```2 CAD, 3 RESIST, 1 DEF```""")
            embed.add_field(name="⚙ GEARS", value="""```4 ATTACK, 5 FAC, 2 DEF, 2 CAD, 2 CAC```""")
            embed.add_field(name="💎 FACTS", value="""```Recommended Team: JLA, JLC and MWW. 

An all-purpose MWW build. A solid DD option for those who use JLF with LOA on GG/P1, and have JLA/JLC/JLB/MWW leftover. 

MWW is a good primary DD for TAB tag-ins due to a shorter time-duration basic attack combo chain, power block, and armor-piercing on SP1 in comparison to JLA. This build is designed to take some hits for 3 minutes and survive tech class changes without losing too much health. The 60% DOT resist is use to make hp management from TAB DOT easier.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Mythic Wonder Woman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)

        #League of Anarchy
        if cmd == 'epi':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Tank Combo Builder - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack       3,417
Health       33,424
Defense    75 
CAD           270 
CAC           73 
LAC            1
FAC            69 
Stun resist    75
DOT resist    75
CAC resist    70```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙ GEARS", value="""```3 CAD, 2 CAC, 4 FAC, 3 HEALTH, 2 DEF, 1 ATTACK```""")
            embed.add_field(name="💎 FACTS", value="""```EPI is the key to the LOA team as she provides DOT on basic attacks for herself and LOA teammates. When she dies the DOT will go away; hence, it is necessary to make sure she's built as a hybrid so she can heal and as well as survive the match. Her healing is based on how much damage she does; hence, it is ideal to have a critical attack chance and damage and fast attack chance to heal faster. Use all blades or claw of horus to boost her attack and healing. You can also use a metahuman or agility artifact on her.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Entangling Poison Ivy", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'hbhq':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack   4,831
Health  26,896
Defense  24
CAD    300
CAC    75
FAC    75
Stun resist  0
DOT resist  0
CAC resist  10```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 AP, 2 CAC```""")
            embed.add_field(name="⚙ GEARS", value="""```6 ATTACK, 4 FAC, 4 CAD, 1 CAC```""")
            embed.add_field(name="💎 FACTS", value="""```Heartbreaker Harley Quinn (HBHQ) Is one of INJ2s top 10 damage dealing characters (DDs). All damage is done to stunned opponents. She is ideally teamed up w/AKBM, and EPI. Also she's always good as a support character on her original LOA team. Most effective vs GG, P1, P3. A must have for solo raids.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Heart Breaker Harley Quinn", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'llj':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer Build (P1) - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack     6167
Health     23620
Defense    24
CAD        300
CAC        75
FAC        69
Stun resist   0
DOT resist    0
CAC resist    15```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 CAD, 2 CAC```""")
            embed.add_field(name="⚙ GEARS", value="""```9 ATTACK, 4 FAC, 1 CAC, 1 CAD```""")
            embed.add_field(name="💎 FACTS", value="""```LLJ is the single most effective character against Phase 1 in raids. This character is meant to be paired with EPI and JLF. LLJ should have The All Blades equipped for maximum damage.```""")
            embed.add_field(name="⚡ [Damage Dealer Build (GG) - G70]\n⚙ STATS", value="""```Attack     5007
Health     23620
Defense    24
CAD        300
CAC        75
FAC        75
Stun resist   0
DOT resist    0
CAC resist    15```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 AP, 2 CAC```""")
            embed.add_field(name="⚙ GEARS", value="""```5 FAC, 4 CAD, 5 ATTACK, 1 CAC```""")
            embed.add_field(name="💎 FACTS", value="""```96% Armor-piercing LLJ build. Especially effective on GG in T7/T8 with EPI & JLF.```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Last Laugh Joker", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)

        #gold part one
        if cmd == 'bb':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer Build - G60]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack      4,498 
Health      27,680 
Defense    21 
CAD         300
CAC         73 
FAC          61 
Stun resist   0
DOT resist    0
CAC resist    0```""")
            embed.add_field(name="⚙ TALENTS", value="""```5 CAD, 1 CAC```""")
            embed.add_field(name="⚙ GEARS", value="""```2 HEALTH, 6 ATTACK, 4 FAC, 2 CAC, 1 CAD```""")
            embed.add_field(name="💎 FACTS", value="""```100% damage on basics for limited time after using either of his 3 specials. So we have him offensively built to take advantage of his passive. His sp3 gives 90% defense and hence we don't need to have defense in his gears or talents. Do not use his special 1.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Blue Beetle", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'asm':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Tank Combo Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack      2,611
Health      51,064
Defense    58(passive gives 20%) 
CAD   150
CAC    25
LAC     1
FAC     69
Stun resist   75
DOT resist   75
CAC resist   70
BE   49 ```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 RES, 2 BE```""")
            embed.add_field(name="⚙ GEARS", value="""```9 HEALTH, 4 FAC, 2 DEF```""")
            embed.add_field(name="💎 FACTS", value="""```Armored Superman has a chance to ignore the first special attack (1/2/3) of the opponent and provides 20% team defense which also applies to himself. He's a great tank and decent combo builder.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Armored Superman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'koaam':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer Build (Crit) - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack        5,632
Health       24,580
Defense    44
CAD       300
CAC       75
FAC       69 
Stun resist   0
DOT resist    0
CAC resist    0```""")
            embed.add_field(name="⚙ TALENTS", value="""```3 CAC, 3 CAD```""")
            embed.add_field(name="⚙ GEARS", value="""```8 ATTACK, 4 FAC, 2 CAD, 1 CAC```""")
            embed.add_field(name="💎 FACTS", value="""```King of Atlantis Aquaman is the raid master and best damage dealer for raids irrespective of whatever sub-boss or phase you fight. You can have a defense in place of some attack if you are a regular HSC player.```""")
            embed.add_field(name="⚡ [Damage Dealer Build (Non-Crit) - G70]\n⚙ STATS", value="""```Attack        6,502
Health         24,580
Defense         68%
CAD             150%
CAC             25%
FAC             69%
Stun resist   0
DOT resist    0
CAC resist    0```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 AP, 2 DEF```""")
            embed.add_field(name="⚙ GEARS", value="""```11 ATTACK, 4 FAC```""")
            embed.add_field(name="💎 FACTS", value="""```Non-crit KOAAM is for Phase 2 and Captain Cold since P2 is immune to crit and CC is highly crit resistant. We have armor pierce talents to bypass defense and high attack to deal raw damage. The recommended team for phase 2 would be shazam and doctor fate. You can also use Nightwing or Atrocitus. For captain cold, use shazam and doctor fate.```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="King of Atlantis Aquaman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'sb' or cmd == 'sbn':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack     6456
Health     16130
Defense    75%
CAD        300%
CAC        75%
FAC        10%
Stun resist   0%
DOT resist    0%
CAC resist    10%```""")
            embed.add_field(name="⚙ TALENTS", value="""```5 CAD, 1 CAC```""")
            embed.add_field(name="⚙ GEARS", value="""```12 ATTACK, 2 CAC, 1 CAD```""")
            embed.add_field(name="💎 FACTS", value="""```SB is perhaps the best damage dealer for DF Boss. It can be paired with PBM or RF. Begin the match with an sp2 to apply torment then proceed to disable DF with SB sp1, or PBM sp1, before building combo for SB sp3.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Banshee", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'shz' or cmd == 'szm':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡ **[Tank Combo/ Support Build - G70]**""")
            embed.add_field(name="⚙ STATS", value="""```Attack  3091
Health  52,048
Defense  75
CAD   150 
CAC    22
LAC    1 
FAC     69 
Stun resist  75 
DOT resist  75 
CAC resist   70 ```""")
            embed.add_field(name="⚙ TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙ GEARS", value="""```9 HEALTH, 4 FAC, 2 DEF```""")
            embed.add_field(name="💎 FACTS", value="""```Shazam is a great tank and combo builder. If you're not willing to have FAC on him then replace them with health. Recommended artifacts are the Nth Metal Armor, Kryptonian Regeneration Matrix, and Metahuman to boost healing for the entire team with his SP3.```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Shazam", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'aaam':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```Attack     5422
Health     21028
Defense    70
CAD        300
CAC        75
FAC        1
Stun resist   0
DOT resist    0
CAC resist    0 ```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAC, 3 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```10 ATTACK, 1 CAC, 4 CAD```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Atlantean Armor Aquaman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'egl':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Tank Build - G60]**""")
            embed.add_field(name="⚙STATS", value="""```Attack     2375
Health     34755
Defense    75
CAD        150
CAC        34
FAC        75
Stun resist   68
DOT resist    68
CAC resist    68  ```""")
            embed.add_field(name="⚙TALENTS", value="""```4 RES, 1 AP, 1 CAC```""")
            embed.add_field(name="⚙GEARS", value="""```6 HEALTH, 4 DEF, 5 FAC```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Emerald Green Lantern", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'mtcw':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G60]**""")
            embed.add_field(name="⚙STATS", value="""```Attack       4,426
Health       25,900
Defense    66 
CAD           292 
CAC           73 
LAC            1
FAC            11
Stun resist    0 
DOT resist    0
CAC resist    0```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAD, 3 CAC```""")
            embed.add_field(name="⚙GEARS", value="""```5 ATTACK, 4 HEALTH, 3 DEF, 2 CAD, 1 CAC```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Master Thief Catwoman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'bmr':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Tank Combo Build - G60]**""")
            embed.add_field(name="⚙STATS", value="""```Attack      3,176
Health      44,400
Defense    75 
CAD       150
CAC        22 
LAC        1
FAC        71 
Stun resist   75 
DOT resist   75 
CAC resist   70```""")
            embed.add_field(name="⚙TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```9 HEALTH, 4 FAC, 2 DEF```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Blade Master Robin", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'atc' or cmd == 'atr':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Tank Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```TTV     460845
Attack     2947        
Health     66116        
Defense    75        
CAD        150        
CAC        25        
FAC        1        
Stun resist   75        
DOT resist    75        
CAC resist    70 ```""")
            embed.add_field(name="⚙TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```14 HEALTH, 1 DEF```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Atrocitus", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'ba':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```Attack     5816
Health     24234
Defense    75    
CAD        294    
CAC        75    
FAC        1    
Stun resist   0
DOT resist    0        
CAC resist    0 ```""")
            embed.add_field(name="⚙TALENTS", value="""```3 DEF, 2 CAC, 1 CAD```""")
            embed.add_field(name="⚙GEARS", value="""```9 ATTACK, 3 CAD, 2 CAC, 1 DEF```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Black Adam", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'csm':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Tank/ Support Build - G60]**""")
            embed.add_field(name="⚙STATS", value="""```Attack     3526
Health     26954 (More can be added)        
Defense    75    
CAD        150
CAC        34        
FAC        75        
Stun resist   60        
DOT resist    60        
CAC resist    70```""")
            embed.add_field(name="⚙TALENTS", value="""```3 RES, 1 AP, 1 DEF, 1 CAC```""")
            embed.add_field(name="⚙GEARS", value="""```3 DEF, 3 HEALTH, 3 ATTACK, 6 FAC```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Classic Superman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'dsg':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```Attack     6015        
Health     21700        
Defense    53
CAD        298    
CAC        75
FAC        1        
Stun resist   40        
DOT resist    40        
CAC resist    40  ```""")
            embed.add_field(name="⚙TALENTS", value="""```2 RES, 2 DEF, 2 CAD```""")
            embed.add_field(name="⚙GEARS", value="""```10 ATTACK, 2 CAD, 3 CAC```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Dark Supergirl", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'esf':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```Attack     5531        
Health     17860        
Defense    24        
CAD        300        
CAC        71        
FAC        69        
Stun resist   0        
DOT resist    0        
CAC resist    0        
            ```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAD, 1 CAC, 2 AP```""")
            embed.add_field(name="⚙GEARS", value="""```10 ATTACK, 5 FAC, 2 CAC, 1 CAD```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Energized Starfire", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'fpi':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```Attack     6557        
Health     19602        
Defense    36
CAD        254    
CAC        75
FAC        1    
LAC        33    
Stun resist   0        
DOT resist    0        
CAC resist    0  ```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAC, 1 CAD, 1 DEF, 1 LETHAL```""")
            embed.add_field(name="⚙GEARS", value="""```12 ATTACK, 2 CAD, 1 CAC```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Flora Poison Ivy", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'hb':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Balanced Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```Attack     5157
Health     22428
Defense    75
CAD        294
CAC        75
FAC        35
Stun resist   0
DOT resist    0    
CAC resist    0 ```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAC, 2 DEF, 1 CAD```""")
            embed.add_field(name="⚙GEARS", value="""```8 ATTACK, 3 CAD, 1 CAC, 2 FAC, 1 DEF```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Hell Boy", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'hsc':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Balanced Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```Attack     4864
Health     18358    
Defense    75
CAD        299
CAC        73
FAC        1
Stun resist   0        
DOT resist    0        
CAC resist    0```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAC, 2 DEF, 1 CAD```""")
            embed.add_field(name="⚙GEARS", value="""```9 ATTACK, 2 DEF, 4 CAD```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Horrific Scarecrow", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'jsgl':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Balanced Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```Attack     3915        
Health     23860        
Defense    75        
CAD        300        
CAC        75        
FAC        69        
Stun resist   20        
DOT resist    20        
CAC resist    20 ```""")
            embed.add_field(name="⚙TALENTS", value="""```2 CAD, 1 CAC, 1 AP, 1 DEF, 1 RES```""")
            embed.add_field(name="⚙GEARS", value="""```4 ATTACK, 2 DEF, 3 CAD, 4 FAC, 2 CAC```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="John Stewart Green Lantern", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'kbm':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Tank Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```Attack     3667        
Health     59400        
Defense    75        
CAD        175        
CAC        35        
FAC        1        
Stun resist   75        
DOT resist    75        
CAC resist    70  ```""")
            embed.add_field(name="⚙TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```13 HEALTH, 2 DEF```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Knightmare Batman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'pg':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```Attack     6502        
Health     22924        
Defense    24    
CAD        294    
CAC        75
FAC        1        
Stun resist   70        
DOT resist    60        
CAC resist    60 ```""")
            embed.add_field(name="⚙TALENTS", value="""```3 RES, 2 CAC, 1 CAD```""")
            embed.add_field(name="⚙GEARS", value="""```11 ATTACK, 1 CAC, 3 CAD```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Power Girl", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'pbm':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```Attack     7372        
Health     21412        
Defense    24    
CAD        262        
CAC        71        
FAC        1
Stun resist   0
DOT resist    0        
CAC resist    0 ```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAC, 3 CAD```""")
            embed.add_field(name="⚙GEARS", value="""```14 ATTACK, 1 CAD```""")
            embed.add_field(name="💎 FACTS", value="""```Pair with MVF to get full CAD```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Predator Batman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'rh':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Tank/ Support Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```Attack     3071
Health     49154
Defense    75
CAD        150
CAC        51
FAC        69
Stun resist   40        
DOT resist    40        
CAC resist    40  ```""")
            embed.add_field(name="⚙TALENTS", value="""```2 DEF, 2 RES, 1 CAC, 1 LAC```""")
            embed.add_field(name="⚙GEARS", value="""```9 HEALTH, 2 DEF, 4 FAC```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Red Hood", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'rf':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Tank/ Combo Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```Attack     3523        
Health     47316        
Defense    75        
CAD        150        
CAC        25        
FAC        75        
Stun resist   60        
DOT resist    60        
CAC resist    60 ```""")
            embed.add_field(name="⚙TALENTS", value="""```3 RES, 1 BE, 2 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```9 HEALTH, 2 DEF, 4 FAC```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Reverse Flash", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'stsf' or cmd == 'sff':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```Attack     5526
Health     18396
Defense    51    
CAD        300
CAC        70        
FAC        11        
Stun resist   0        
DOT resist    0        
CAC resist    0  ```""")
            embed.add_field(name="⚙TALENTS", value="""```4 CAC, 2 CAD```""")
            embed.add_field(name="⚙GEARS", value="""```10 ATTACK, 2 DEF, 3 CAD```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Speed Force The Flash", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'tgg' or cmd == 'tkgg':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Tank Build - G60]**""")
            embed.add_field(name="⚙STATS", value="""```Attack     2237
Health     55875
Defense    75
CAD        150
CAC        22
FAC        1
Stun resist   75        
DOT resist    75        
CAC resist    70 ```""")
            embed.add_field(name="⚙TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```14 HEALTH, 1 DEF```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Telekinetic Gorilla Grodd", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'wqww':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Balanced Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```Attack     4762        
Health     20404        
Defense    75    
CAD        274    
CAC        71    
FAC        69    
LAC      13    
Stun resist   20        
DOT resist    20        
CAC resist    20 ```""")
            embed.add_field(name="⚙TALENTS", value="""```2 DEF, 1 RES, 1 CAD, 1 CAC, 1 LETHAL```""")
            embed.add_field(name="⚙GEARS", value="""```5 ATTACK, 2 DEF, 4 FAC, 2 CAD, 2 CAC```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Warrior Queen Wonder Woman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'rdn':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Attack Build - G60]**""")
            embed.add_field(name="⚙STATS", value="""```Attack     5066
Health     26876
Defense    75
CAD        150
CAC        37
FAC        1
Stun resist   40
DOT resist    40
CAC resist    40```""")
            embed.add_field(name="⚙TALENTS", value="""```2 RES, 2 BE, 1 DEF, 1 ATTACK```""")
            embed.add_field(name="⚙GEARS", value="""```9 ATTACK, 3 DEF, 2 HEALTH, 1 CAC```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Raiden", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'sz':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Tank Build - G60]**""")
            embed.add_field(name="⚙STATS", value="""```Attack     3301
Health     40652
Defense    75
CAD        150
CAC        58
FAC        16
Stun resist   60
DOT resist    60
CAC resist    70  ```""")
            embed.add_field(name="⚙TALENTS", value="""```3 RES, 3 CAC```""")
            embed.add_field(name="⚙GEARS", value="""```8 HEALTH, 4 DEF, 2 ATTACK, 1 FAC```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Sub Zero", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == 'ssds':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```Attack     5517
Health     23001
Defense    75
CAD        300
CAC        75
FAC        1
LAC        11
Stun resist   0        
DOT resist    0        
CAC resist    0 ```""")
            embed.add_field(name="⚙TALENTS", value="""```2 CAC, 4 CAD```""")
            embed.add_field(name="⚙GEARS", value="""```9 ATTACK, 3 DEF, 2 CAD, 1 CAC```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Suicide Squad Deadshot", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == '':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[G70 BUILD]**""")
            embed.add_field(name="⚙STATS", value="""``````""")
            embed.add_field(name="⚙TALENTS", value="""``````""")
            embed.add_field(name="⚙GEARS", value="""``````""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == '':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[G70 BUILD]**""")
            embed.add_field(name="⚙STATS", value="""``````""")
            embed.add_field(name="⚙TALENTS", value="""``````""")
            embed.add_field(name="⚙GEARS", value="""``````""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == '':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[G70 BUILD]**""")
            embed.add_field(name="⚙STATS", value="""``````""")
            embed.add_field(name="⚙TALENTS", value="""``````""")
            embed.add_field(name="⚙GEARS", value="""``````""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == '':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[G70 BUILD]**""")
            embed.add_field(name="⚙STATS", value="""``````""")
            embed.add_field(name="⚙TALENTS", value="""``````""")
            embed.add_field(name="⚙GEARS", value="""``````""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == '':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[G70 BUILD]**""")
            embed.add_field(name="⚙STATS", value="""``````""")
            embed.add_field(name="⚙TALENTS", value="""``````""")
            embed.add_field(name="⚙GEARS", value="""``````""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == '':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[G70 BUILD]**""")
            embed.add_field(name="⚙STATS", value="""``````""")
            embed.add_field(name="⚙TALENTS", value="""``````""")
            embed.add_field(name="⚙GEARS", value="""``````""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == '':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[G70 BUILD]**""")
            embed.add_field(name="⚙STATS", value="""``````""")
            embed.add_field(name="⚙TALENTS", value="""``````""")
            embed.add_field(name="⚙GEARS", value="""``````""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == '':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[G70 BUILD]**""")
            embed.add_field(name="⚙STATS", value="""``````""")
            embed.add_field(name="⚙TALENTS", value="""``````""")
            embed.add_field(name="⚙GEARS", value="""``````""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == '':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[G70 BUILD]**""")
            embed.add_field(name="⚙STATS", value="""``````""")
            embed.add_field(name="⚙TALENTS", value="""``````""")
            embed.add_field(name="⚙GEARS", value="""``````""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == '':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[G70 BUILD]**""")
            embed.add_field(name="⚙STATS", value="""``````""")
            embed.add_field(name="⚙TALENTS", value="""``````""")
            embed.add_field(name="⚙GEARS", value="""``````""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == '':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[G70 BUILD]**""")
            embed.add_field(name="⚙STATS", value="""``````""")
            embed.add_field(name="⚙TALENTS", value="""``````""")
            embed.add_field(name="⚙GEARS", value="""``````""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == '':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[G70 BUILD]**""")
            embed.add_field(name="⚙STATS", value="""``````""")
            embed.add_field(name="⚙TALENTS", value="""``````""")
            embed.add_field(name="⚙GEARS", value="""``````""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == '':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[G70 BUILD]**""")
            embed.add_field(name="⚙STATS", value="""``````""")
            embed.add_field(name="⚙TALENTS", value="""``````""")
            embed.add_field(name="⚙GEARS", value="""``````""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        if cmd == '':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[G70 BUILD]**""")
            embed.add_field(name="⚙STATS", value="""``````""")
            embed.add_field(name="⚙TALENTS", value="""``````""")
            embed.add_field(name="⚙GEARS", value="""``````""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(CharBuild(client))