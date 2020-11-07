import discord
from discord.ext import commands
from random import choice

class CharBuild(commands.Cog):
    def __init__(self, client):
        self.Bot = client

    @commands.command(name='b', aliases=['build'])
    async def b(self, ctx, cmd: str= None):
        if cmd is None:
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""Currently, only the character builds on those lists below, are available as of now. We will add other builds soon. To use the command, type, ```i!b [character command]```""")
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
svbm - Silver Batman ```""")
            embed.add_field(name='🟨 Gold Characters (Part 1)', value="""```bb - Blue Beetle
asm - Armoured Superman
mvasg - Multiverse Armored Supergirl
epi - Entangling Poison Ivy
mvbw-1 - Multiverse Bat Woman
mvbw-2 - Multiverse Bat Woman
mtcw - Masterthief Catwoman
bmr - Blade Master Robin
aaam - Atlantean Armored Aquaman
egl - Emerald Green Lantern
grid - Grid
csm - Classic Superman 
cbm - Classic Batman
eb - Enraged Bane
koaamnc - King of Atlantis Aquaman (Non-Crit)
koaamc - King of Atlantis Aquaman (Crit)
atc - Atrocitus
mvf - Multiverse The Flash
hbhq - Heart Breaker Harley Quinn
jlc - Justice League Cyborg
jlf - Justice League Flash
jla - Justice League Aquaman
jlb - Justice League Batman
sc - Horrific Scarecrow 
llj - Last Laugh Joker 
pbm - Predator Batman
sb - Silver Banshee
nw - Nightwing
psg - Powered Supergirl
kbm - Knightmare Batman
szm - Shazam
rf - Reverse Flash
cth - Cheetah
sz - Subzero
sff - Speed Force the Flash
pg - Power Girl 
mww - Mythic Wonderwoman
bncw - Batman Ninja Catwoman
bnr - Batman Ninja Robin
bnlj - Batman Ninja Lord Joker
rdn - Raiden
bnbm - Batman Ninja Batman
bnhq - Batman Ninja Harley Quinn 
ssdf - Soul Stealer Doctor Fate 
ba - Black Adam
pst - Primal Swamp Thing
jsgl - John Stewart Green Lantern
tkgg - TeleKinetic Gorilla Grodd 
rh - Red Hood
fpi - Flora Poison Ivy 
mvbl - Multiverse Black Lightning
mvga - Multiverse Green Arrow 
mvwc - Multiverse White Canary 
cc2 - Captain Cold
sbc - Sonic Black Canary
ssds - Suicide Squad Deadshot
hb - Hellboy
dsg - Dark Super Girl
wqww - Warrior Queen Wonder Woman 
mvbw - Multiverse Batwoman
mvcc - Multiverse Captain Cold
mvsg - Multiverse Supergirl
ubc - Unbreakable Cyborg
fs - Firestorm
esf - Energized Starfire
uhq - Unhinged Harley Quinn```""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")
            embed.set_image(url="")
            await ctx.channel.send(embed=embed)
        elif cmd == 'aww':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Tank Build - G60]**""")
            embed.add_field(name="⚙STATS", value="""```Attack       2,465
Health       49,552 
Defense    75 
CAD           150 
CAC           22 
LAC            1
FAC            1 
Stun resist    75
DOT resist    75
CAC resist    70```""")
            embed.add_field(name="⚙TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```13 HEALTH, 2 DEF```""")
            embed.add_field(name="💎FACTS", value="""""")
            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Amazon Wonder Woman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        elif cmd == 'svbc' or cmd == 'sbc':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G60]**""")
            embed.add_field(name="⚙STATS", value="""```Attack            3,888
Health            23,285
Defense          70
CAD                294 
CAC                48 
LAC                 1 
FAC                46 
Stun resist     0 
DOT resist     0 
CAC resist     5 ```""")
            embed.add_field(name="⚙TALENTS", value="""```4 DEF, 1 CAC, 1 CAD```""")
            embed.add_field(name="⚙GEARS", value="""```3 CAD, 1 CAC, 5 ATTACK, 3 FAC, 3 HEALTH```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Sonic/ Silver Black Canary", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        elif cmd == 'svcw':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G60]**""")
            embed.add_field(name="⚙STATS", value="""```Attack       3,544
Health       23,500
Defense    66 
CAD           292 
CAC           73 
LAC            1
FAC            6 
Stun resist    0 
DOT resist    0
CAC resist    0```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAD, 3 CAC```""")
            embed.add_field(name="⚙GEARS", value="""```3 DEF, 2 CAD, 1 CAC, 5 ATTACK, 4 HEALTH```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Catwoman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        elif cmd == 'svam':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```Attack       6,222
Health       18,186
Defense     29 
CAD           300
CAC           75 
LAC            1
FAC            1
Stun resist    30 (passive) 
DOT resist    0
CAC resist    0 ```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAC, 3 CAD```""")
            embed.add_field(name="⚙GEARS", value="""```2 CAD, 1 CAC, 12 ATTACK```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Aquaman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        elif cmd == 'svc':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Tank Combo Build - G60]**""")
            embed.add_field(name="⚙STATS", value="""```Attack       2,129
Health       40,089
Defense    75 
CAD           150 
CAC           22 
LAC            1
FAC            61 
Stun resist    75
DOT resist    75
CAC resist    70```""")
            embed.add_field(name="⚙TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```2 DEF, 4 FAC, 9 HEALTH```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Cyborg", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        elif cmd == 'svf':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Tank Combo Build - G60]**""")
            embed.add_field(name="⚙STATS", value="""```Attack            3,534
Health            35,785
Defense         75 
CAD               150
CAC               22 
LAC                1
FAC                21 
Stun resist     75
DOT resist     75 
CAC resist     70 ```""")
            embed.add_field(name="⚙TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```2 DEF, 1 FAC, 4 ATTACk, 8 HEALTH```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Flash", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        elif cmd == 'svj':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G60]**""")
            embed.add_field(name="⚙STATS", value="""```Attack       4,331
Health       23,882
Defense    66 
CAD           300 
CAC           73 
LAC            1
FAC            1 
Stun resist    0 
DOT resist    0
CAC resist    0```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAD, 3 CAC```""")
            embed.add_field(name="⚙GEARS", value="""```3 DEF, 2 CAD, 1 CAC, 6 ATTACK, 3 HEALTH```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Joker", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)

        elif cmd == 'svhq':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G60]**""")
            embed.add_field(name="⚙STATS", value="""```Attack          3,344 (173 from her passive)
Health          16,787
Defense        69 
CAD              279
CAC              75 
LAC                1
FAC                61 
Stun resist    0
DOT resist    0
CAC resist    0```""")
            embed.add_field(name="⚙TALENTS", value="""```1 CAD, 1 CAC, 4 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```3 CAD, 3 CAC, 4 ATTACK, 4 FAC, 1 HEALTH```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Harley Quinn", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        elif cmd == 'svst':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Mix Build - G60]**""")
            embed.add_field(name="⚙STATS", value="""```Attack       3,543
Health       37,777
Defense    65 
CAD           150 
CAC           22 
LAC            1
FAC            1 
Stun resist    75
DOT resist    75
CAC resist    70```""")
            embed.add_field(name="⚙TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```1 DEF, 7 ATTACK, 7 DEF```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Swamp Thing", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        elif cmd == 'svgg':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Tank Build - G60]**""")
            embed.add_field(name="⚙STATS", value="""```Attack       1,937
Health       52,589
Defense    65 
CAD           150 
CAC           22 
LAC            1
FAC            1 
Stun resist    75
DOT resist    75
CAC resist    70```""")
            embed.add_field(name="⚙TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```1 DEF, 14 HEALTH```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Gorilla Grodd", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        elif cmd == 'svb':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Tank Combo Build - G60]**""")
            embed.add_field(name="⚙STATS", value="""```Attack      2,402
Health      40,673
Defense    75
CAD           150 
CAC           22
LAC            1 
FAC            61 
Stun resist  75 
DOT resist    75 
CAC resist 70```""")
            embed.add_field(name="⚙TALENTS", value="""``````""")
            embed.add_field(name="⚙GEARS", value="""``````""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Bane", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        elif cmd == 'svds':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G60]**""")
            embed.add_field(name="⚙STATS", value="""```Attack       4,198
Health       19,940
Defense    66 
CAD           292 
CAC           75 
LAC            1
FAC            1 
Stun resist    0
DOT resist    0
CAC resist    0```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAD, 3 CAC```""")
            embed.add_field(name="⚙GEARS", value="""```3 DEF, 1 CAC, 2 CAD, 7 ATTACK, 2 HEALTH```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Deadshot", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        elif cmd == 'svsc':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Tank Build - G60]**""")
            embed.add_field(name="⚙STATS", value="""```Attack       2,359
Health       46,787
Defense    75 
CAD           160 
CAC           22 
LAC            1
FAC            1 
Stun resist    75
DOT resist    75
CAC resist    70```""")
            embed.add_field(name="⚙TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```2 DEF, 13 HEALTH```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Scarecrow", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        elif cmd == 'svr':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Tank Combo Build - G60]**""")
            embed.add_field(name="⚙STATS", value="""```Attack      2,724
Health      42,480
Defense    75 
CAD       150
CAC        22 
LAC        1
FAC        71 
Stun resist   75 
DOT resist   75 
CAC resist   70```""")
            embed.add_field(name="⚙TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```9 HEALTH, 2 DEF, 4 FAC```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Robin", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        elif cmd == 'svdf':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Tank Combo Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```Attack      2,551
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
            embed.add_field(name="⚙TALENTS", value="""```2 BE, 4 RES```""")
            embed.add_field(name="⚙GEARS", value="""```4 FAC, 8 HEALTH, 3 DEF```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Doctor Fate", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        elif cmd == 'svga':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```Attack         6,901
Health        18,276
Defense     24 
CAD              300 
CAC              43 
LAC                1
FAC                1
Stun resist    0
DOT resist    0
CAC resist    0```""")
            embed.add_field(name="⚙TALENTS", value="""```5 CAD, 1 CAC```""")
            embed.add_field(name="⚙GEARS", value="""```15 ATTACK```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Green Arrow", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        elif cmd == 'svww':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Tank Build - G60]**""")
            embed.add_field(name="⚙STATS", value="""```Attack       2,379
Health       47,286
Defense    75 
CAD           160 
CAC           22 
LAC            1
FAC            1 
Stun resist    75
DOT resist    75
CAC resist    70```""")
            embed.add_field(name="⚙TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```2 DEF, 13 HEALTH```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Wonder Woman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        elif cmd == 'svsm':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Tank Combo Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```Attack  2,275
Health  49,203
Defense    75 
CAD    150
CAC     25
LAC     1
FAC     69
Stun resist   75
DOT resist   75
CAC resist   70```""")
            embed.add_field(name="⚙TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```10 HEALTH, 4 FAC, 1 DEF```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Superman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        elif cmd == 'svgl':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Tank Combo Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```Attack       2,659
Health       45,227
Defense    75 
CAD   150
CAC    25
LAC    1
FAC     61
Stun resist   75
DOT resist   75
CAC resist   70```""")
            embed.add_field(name="⚙TALENTS", value="""```4 RES, 2 DEF```""")
            embed.add_field(name="⚙GEARS", value="""```9 HEALTH, 2 DEF, 4 FAC```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Green Lantern", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        elif cmd == 'svbm':
            embed = discord.Embed(colour=discord.Colour(0xf8e71c),
                                  description="""⚡**[Damage Dealer Build - G70]**""")
            embed.add_field(name="⚙STATS", value="""```Attack       6,095
Health       17,284
Defense     24 
CAD           300 
CAC           58 (passive 20% maxes CAC) 
LAC            1
FAC            1
Stun resist    0
DOT resist    0
CAC resist    0 ```""")
            embed.add_field(name="⚙TALENTS", value="""```3 CAC, 3 CAD```""")
            embed.add_field(name="⚙GEARS", value="""```13 ATTACK, 1 CAC, 1 CAD```""")

            embed.set_footer(
                text="Check out the `credits` command to see the list of people who helped making this bot.")

            embed.set_author(name="Silver Batman", url="https://discordapp.com")
            embed.set_thumbnail(url="")
            await ctx.channel.send(embed=embed)
        elif cmd == 'akbm':
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