import discord
from discord.ext import commands
from random import choice

class CharPassive(commands.Cog):
    def __init__(self, client):
        self.Bot = client

    @commands.command(name='p', aliases=['passive'])
    async def p(self, ctx, cmd=None):

        if cmd is None:
            embed = discord.Embed(colour=discord.Colour(0xEE82EE),
                                  description="There are passives for each and every character, which get enabled during battle or at the start of the battle. To know the character's passive, type, ```i!p [character name]``` Where, we type the character's name without the brackets []. For Example, ```i!p jsgl```The following list of characters have their respective passives.")

            embed.set_author(name="Character Passives", url="https://discordapp.com")
            embed.add_field(name="🟪 Legendary Characters", value="""```akbm - Arkham Knight Batman
bm   - Black Manta
bnc  - Brainiac
bngg - Batman Ninja Gorilla Grodd
ds   - Darkseid
dtk  - Deathstroke
gaww - Golden Armor Wonder Woman
jls  - Justice League Superman
mmh  - Martian Manhunter
raven- Raven
sshq - Suicide Squad Harley Quinn 
sse  - Suicide Squad Enchantress```""")
            embed.add_field(name="⬜ Silver Characters", value="""```aww  - Amazon Wonder Woman
svam - Silver Aquaman 
svb  - Silver Bane
svbm - Silver Batman
svbc - Silver Black Canary
svc  - Silver Cyborg
svcw - Silver Catwoman 
svdf - Silver Doctor Fate
svds - Silver Deadshot
svf  - Silver Flash
svga - Silver Green Arrow
svgg - Silver Gorilla Grodd
svgl - Silver Green Lantern
svhq - Silver Harley Quinn
svj  - Silver Joker 
svr  - Silver Robin
svsc - Silver Scarecrow
svsm - Silver Superman
svst - Silver Swamp Thing
svww - Silver Wonder Woman ```""")
            embed.add_field(name="🟨 Gold Characters (Batman Ninjas)", value="""```bnbm - Batman Ninja Batman
bncw - Batman Ninja Catwoman
bnhq - Batman Ninja Harley Quinn
bnlj - Batman Ninja Lord Joker
bnr  - Batman Ninja Robin```""")
            embed.add_field(name="🟨 Gold Characters (Multiverse Gang)", value="""```mvasg - Multiverse Armored Supergirl
mvbl  - Multiverse Black Lightning
mvbw  - Multiverse Bat Woman
mvcc  - Multiverse Captain Cold
mvf   - Multiverse The Flash
mvga  - Multiverse Green Arrow 
mvsg  - Multiverse Supergirl
mvwc  - Multiverse White Canary```""")
            embed.add_field(name="🟨 Gold Characters (The Justice League)", value="""```jla - Justice League Aquaman
jlc - Justice League Cyborg
jlf - Justice League Flash
jlb - Justice League Batman
mww - Mythic Wonder woman```""")
            embed.add_field(name="🟨 Gold Characters (League of Anarchy)", value="""```epi  - Entangling Poison Ivy
hbhq - Heart Breaker Harley Quinn
llj  - Last Laugh Joker ```""")

            embed.add_field(name='🟨 Gold Characters (Others Part 1)', value="""```aaam  - Atlantean Armored Aquaman
aga   - Ace Green Arrow
atc   - Atrocitus
asm   - Armoured Superman
ba    - Black Adam
bb    - Blue Beetle
bmr   - Blade Master Robin
cbm   - Classic Batman
cc    - Captain Cold
csm   - Classic Superman 
cth   - Cheetah
dsg   - Dark Super Girl
eb    - Enraged Bane
egl   - Emerald Green Lantern
esf   - Energized Starfire
fpi   - Flora Poison Ivy 
fs    - Firestorm
grid  - Grid
hb    - Hellboy
hsc   - Horrific Scarecrow 
jsgl  - John Stewart Green Lantern
kbm   - Knightmare Batman
koaam - King of Atlantis Aquaman
mtcw  - Masterthief Catwoman
nw    - Nightwing
pbm   - Predator Batman
pg    - Power Girl
psg   - Powered Supergirl
pst   - Primal Swamp Thing```""")
            embed.add_field(name='🟨 Gold Characters (Others Part 2)', value="""```rdn   - Raiden
rf    - Reverse Flash
rh    - Red Hood
sb    - Silver Banshee
sbc   - Sonic Black Canary
sff   - Speed Force the Flash
ssdf  - Soul Stealer Doctor Fate 
ssds  - Suicide Squad Deadshot
sz    - Subzero
szm   - Shazam 
tkgg  - TeleKinetic Gorilla Grodd 
ubc   - Unbreakable Cyborg
uhq   - Unhinged Harley Quinn
vxn   - Vixen
wqww  - Warrior Queen Wonder Woman```

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: Support server link - [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            # await ctx.channel.send(embed=embed)
            await ctx.channel.send(embed=embed)
        elif cmd == 'mando':
            embed = discord.Embed(colour=discord.Colour(0x800080),
                                  description="""Passive 1: This is The Way: Power Generation Boosted, Lethal Damage bonus.
Passive 2: I got your back: When teammates use any sp ability, Mando does sniper strike from behind, dealing lethal damage.
Passive 3: Lone Mercenary: Attack and Crit increased for teammates during the match.""")
            #file = discord.File("./Images_Passive/mto_passives/jlsm_full.jpg", filename="jlsm_full.jpg")
            #embed.set_image(url="attachment://jlsm_full.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 The Mandalorian", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        
        elif cmd == 'raven':
            embed = discord.Embed(colour=discord.Colour(0x800080),
                                  description="""Passive 1: Darkness Fall
Passive 2: Demonic Rage
Passive 3: Dark Energy""")
            file = discord.File("./Images_Passive/raven.jpg", filename="raven.jpg")
            embed.set_image(url="attachment://raven.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Raven", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)

        elif cmd == 'raven':
            embed = discord.Embed(colour=discord.Colour(0x800080),
                                  description="""Passive 1: Darkness Fall
    Passive 2: Demonic Rage
    Passive 3: Dark Energy""")
            file = discord.File("./Images_Passive/raven.jpg", filename="raven.jpg")
            embed.set_image(url="attachment://raven.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",
                icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Raven", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)

        elif cmd == 'jlsm':
            embed = discord.Embed(colour=discord.Colour(0x800080),
                                  description="""Passive 1: Batman Versus Superman
Passive 2: Do you Bleed?
Passive 3: Protector""")
            file = discord.File("./Images_Passive/mto_passives/jlsm_full.jpg", filename="jlsm_full.jpg")
            embed.set_image(url="attachment://jlsm_full.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Justice League Superman", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'ect':
            embed = discord.Embed(colour=discord.Colour(0x800080),
                                  description="""Passive 1: Mortal Host
Passive 2: Outworldly Nature
Passive 3: Unlimited Power""")
            file = discord.File("./Images_Passive/mto_passives/ssect_full.jpg", filename="ssect_full.jpg")
            embed.set_image(url="attachment://ssect_full.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Suicide Squad Enchantress", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'mmh':
            embed = discord.Embed(colour=discord.Colour(0x800080),
                                  description="""Passive 1: Martian Arts
Passive 2: Telepathic Might
Passive 3: Inhuman Physiology""")
            file = discord.File("./Images_Passive/mmh.jpg", filename="mmh.jpg")
            embed.set_image(url="attachment://mmh.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Martian Manhunter", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'svam':
            embed = discord.Embed(colour=discord.Colour(0xC0C0C0),
                                  description="""""")
            file = discord.File("./Images_Passive/Sil_Am.jpg", filename="Sil_Am.jpg")
            embed.set_image(url="attachment://Sil_Am.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Silver Aquaman", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'svb':
            embed = discord.Embed(colour=discord.Colour(0xC0C0C0),
                                  description="""""")
            file = discord.File("./Images_Passive/Silve_Bane.jpg", filename="Silve_Bane.jpg")
            embed.set_image(url="attachment://Silve_Bane.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Silver Bane", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'sbm':
            embed = discord.Embed(colour=discord.Colour(0xC0C0C0),
                                  description="""""")
            file = discord.File("./Images_Passive/Sil_Batman.jpg", filename="Sil_Batman.jpg")
            embed.set_image(url="attachment://Sil_Batman.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Silver Batman", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'svbc':
            embed = discord.Embed(colour=discord.Colour(0xC0C0C0),
                                  description="""""")
            file = discord.File("./Images_Passive/Silve_Black_Canary.jpg", filename="Silve_Black_Canary.jpg")
            embed.set_image(url="attachment://Silve_Black_Canary.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Silver Black Canary", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'svcw':
            embed = discord.Embed(colour=discord.Colour(0xC0C0C0),
                                  description="""""")
            file = discord.File("./Images_Passive/Sil_CW.jpg", filename="Sil_CW.jpg")
            embed.set_image(url="attachment://Sil_CW.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Silver Catwoman", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'svc':
            embed = discord.Embed(colour=discord.Colour(0xC0C0C0),
                                  description="""""")
            file = discord.File("./Images_Passive/Sil_Cyborg.jpg", filename="Sil_Cyborg.jpg")
            embed.set_image(url="attachment://Sil_Cyborg.jpg")
            embed.set_author(name="👑 Silver Cyborg", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'sds':
            embed = discord.Embed(colour=discord.Colour(0xC0C0C0),
                                  description="""""")
            file = discord.File("./Images_Passive/Sil_Deadshot.jpg", filename="Sil_Deadshot.jpg")
            embed.set_image(url="attachment://Sil_Deadshot.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Silver Deadshot", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'akbm':
            embed = discord.Embed(colour=discord.Colour(0x800080),
                                  description="""Passive 1: Wayne Tech
Passive 2: Fear Multi-Takedown
Passive 3: Freeflow Counter""")
            file = discord.File("./Images_Passive/mto_passives/akbm_full.jpg", filename="akbm_full.jpg")
            embed.set_image(url="attachment://akbm_full.jpg")
            embed.set_author(name="👑 Arkham Knight Batman", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'df' or cmd == 'svdf':
            embed = discord.Embed(colour=discord.Colour(0xC0C0C0),
                                  description="""""")
            file = discord.File("./Images_Passive/Sil_Doctor_Fate.jpg", filename="Sil_Doctor_Fate.jpg")
            embed.set_image(url="attachment://Sil_Doctor_Fate.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Silver Doctor Fate", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'svgg':
            embed = discord.Embed(colour=discord.Colour(0xC0C0C0),
                                  description="""""")
            file = discord.File("./Images_Passive/Sil_gg.jpg", filename="Sil_gg.jpg")
            embed.set_image(url="attachment://Sil_gg.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Silver Gorilla Grodd", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'svga':
            embed = discord.Embed(colour=discord.Colour(0xC0C0C0),
                                  description="""""")
            file = discord.File("./Images_Passive/Sil_Green_Arrow.jpg", filename="Sil_Green_Arrow.jpg")
            embed.set_image(url="attachment://Sil_Green_Arrow.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Silver Green Arrow", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'sgl':
            embed = discord.Embed(colour=discord.Colour(0xC0C0C0),
                                  description="""""")
            file = discord.File("./Images_Passive/Sil_Green_Lantern.jpg", filename="Sil_Green_Lantern.jpg")
            embed.set_image(url="attachment://Sil_Green_Lantern.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Silver Green Lantern", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'svhq':
            embed = discord.Embed(colour=discord.Colour(0xC0C0C0),
                                  description="""""")
            file = discord.File("./Images_Passive/Sil_hq.jpg", filename="Sil_hq.jpg")
            embed.set_image(url="attachment://Sil_hq.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Silver Harley Quinn", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'svr':
            embed = discord.Embed(colour=discord.Colour(0xC0C0C0),
                                  description="""""")
            file = discord.File("./Images_Passive/Sil_Robin.jpg", filename="Sil_Robin.jpg")
            embed.set_image(url="attachment://Sil_Robin.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Silver Robin", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'svsc':
            embed = discord.Embed(colour=discord.Colour(0xC0C0C0),
                                  description="""Image coming soon..""")
            file = discord.File("./Images_Passive/Sil_Robin.jpg", filename="Sil_Robin.jpg")
            embed.set_image(url="attachment://Sil_Robin.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Silver Scarecrow", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        elif cmd == 'ssm':
            embed = discord.Embed(colour=discord.Colour(0xC0C0C0),
                                  description="""""")
            file = discord.File("./Images_Passive/Sil_Superman.jpg", filename="Sil_Superman.jpg")
            embed.set_image(url="attachment://Sil_Superman.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Silver Superman", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'svst':
            embed = discord.Embed(colour=discord.Colour(0xC0C0C0),
                                  description="""""")
            file = discord.File("./Images_Passive/Sil_Swampy.jpg", filename="Sil_Swampy.jpg")
            embed.set_image(url="attachment://Sil_Swampy.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Silver Swamp Thing", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'svf':
            embed = discord.Embed(colour=discord.Colour(0xC0C0C0),
                                  description="""""")
            file = discord.File("./Images_Passive/Sil_Flash.jpg", filename="Sil_Flash.jpg")
            embed.set_image(url="attachment://Sil_Flash.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Silver Flash", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'svj':
            embed = discord.Embed(colour=discord.Colour(0xC0C0C0),
                                  description="""""")
            file = discord.File("./Images_Passive/Sil_Joker.jpg", filename="Sil_Joker.jpg")
            embed.set_image(url="attachment://Sil_Joker.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Silver Joker", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'svww':
            embed = discord.Embed(colour=discord.Colour(0xC0C0C0),
                                  description="""""")
            file = discord.File("./Images_Passive/Sil_WW.jpg", filename="Sil_WW.jpg")
            embed.set_image(url="attachment://Sil_WW.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Silver Wonder Woman", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'aww':
            embed = discord.Embed(colour=discord.Colour(0xC0C0C0),
                                  description="""Amazon Wonder Woman:

    Women in your roster gain +1% health""")
            embed.set_image(url="")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Amazon Wonder Woman", url="https://discordapp.com")
            await ctx.channel.send(embed=embed)
        elif cmd == 'aaam':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: The Waterbearer""")
            file = discord.File("./Images_Passive/aaam1.jpg", filename="aaam1.jpg")
            embed.set_image(url="attachment://aaam1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Atlantean Armor Aquaman", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'aga':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Power Lock Arrow""")
            file = discord.File("./Images_Passive/aga1.jpg", filename="aga1.jpg")
            embed.set_image(url="attachment://aga1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Ace Green Arrow", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'asm':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Kryptonian Armor""")
            file = discord.File("./Images_Passive/asm1.jpg", filename="asm1.jpg")
            embed.set_image(url="attachment://asm1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Armored Superman", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'ats':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Dex-Starr""")
            file = discord.File("./Images_Passive/ats1.jpg", filename="ats1.jpg")
            embed.set_image(url="attachment://ats1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Atrocitus", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'ba':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Power of Aton""")
            file = discord.File("./Images_Passive/ba1.jpg", filename="ba1.jpg")
            embed.set_image(url="attachment://ba1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Black Adam", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'bb':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Power Blades""")
            file = discord.File("./Images_Passive/bb1.jpg", filename="bb1.jpg")
            embed.set_image(url="attachment://bb1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Blue Beetle", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'bmr':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Perfect Son""")
            file = discord.File("./Images_Passive/bmr1.jpg", filename="bmr1.jpg")
            embed.set_image(url="attachment://bmr1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Blade Master Robin", url="https://discordapp.com")
            await ctx.channel.send(embed=embed, file=file)
        elif cmd == 'bnbm':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Aikido""")

            file = discord.File("./Images_Passive/bnbm1.jpg", filename="bnbm1.jpg")
            embed.set_image(url="attachment://bnbm1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            embed.set_author(name="👑 Batman Ninja Batman", url="https://discordapp.com")
            await ctx.channel.send(embed=embed,file=file)
        elif cmd == 'bnhq':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Ninja Sidekick""")
            embed.set_author(name="👑 Batman Ninja Harley Quinn", url="https://discordapp.com")
            file = discord.File("./Images_Passive/bnhq1.jpg", filename="bnhq1.jpg")
            embed.set_image(url="attachment://bnhq1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.send(file=file, embed=embed)
        elif cmd == 'bnlj':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Eternal Foe""")
            embed.set_author(name="👑 Batman Ninja Lord Joker", url="https://discordapp.com")
            file = discord.File("./Images_Passive/bnlj1.jpg", filename="bnlj1.jpg")
            embed.set_image(url="attachment://bnlj1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'cc':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Absolute Zero""")
            embed.set_author(name="👑 Captain Cold", url="https://discordapp.com")
            file = discord.File("./Images_Passive/cc1.jpg", filename="cc1.jpg")
            embed.set_image(url="attachment://cc1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'csm':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Titanic Strength""")
            embed.set_author(name="👑 Classic Superman", url="https://discordapp.com")
            file = discord.File("./Images_Passive/csm1.jpg", filename="csm1.jpg")
            embed.set_image(url="attachment://csm1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'cth':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Claws of Death""")
            embed.set_author(name="👑 Cheetah", url="https://discordapp.com")
            file = discord.File("./Images_Passive/cth1.jpg", filename="cth1.jpg")
            embed.set_image(url="attachment://cth1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'dsg':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Kryptonian Slam""")
            embed.set_author(name="👑 Dark Supergirl", url="https://discordapp.com")
            file = discord.File("./Images_Passive/dsg1.jpg", filename="dsg1.jpg")
            embed.set_image(url="attachment://dsg1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'eb':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Antivenom""")
            embed.set_author(name="👑 Enraged Bane", url="https://discordapp.com")
            file = discord.File("./Images_Passive/ebane1.jpg", filename="ebane1.jpg")
            embed.set_image(url="attachment://ebane1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'egl':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: For the Corps""")
            embed.set_author(name="👑 Emerald Green Lantern", url="https://discordapp.com")
            file = discord.File("./Images_Passive/egl1.jpg", filename="egl1.jpg")
            embed.set_image(url="attachment://egl1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'esf':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Energy Absorption""")
            embed.set_author(name="👑 Energized Starfire", url="https://discordapp.com")
            file = discord.File("./Images_Passive/esf1.jpg", filename="esf1.jpg")
            embed.set_image(url="attachment://esf1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'fpi':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Poison Vines""")
            embed.set_author(name="👑 Flora Poison Ivy", url="https://discordapp.com")
            file = discord.File("./Images_Passive/fpi1.jpg", filename="fpi1.jpg")
            embed.set_image(url="attachment://fpi1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'fs':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: DoT (Damage Over Time) Resistance""")
            embed.set_author(name="👑 Firestorm", url="https://discordapp.com")
            file = discord.File("./Images_Passive/fs1.jpg", filename="fs1.jpg")
            embed.set_image(url="attachment://fs1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'grid':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Circuit Breaker""")
            embed.set_author(name="👑 Grid", url="https://discordapp.com")
            file = discord.File("./Images_Passive/grid1.jpg", filename="grid1.jpg")
            embed.set_image(url="attachment://grid1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'hb':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Box of Evil""")
            embed.set_author(name="👑 HellBoy", url="https://discordapp.com")
            file = discord.File("./Images_Passive/hb1.jpg", filename="hb1.jpg")
            embed.set_image(url="attachment://hb1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'hsc':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Fear Aura""")
            embed.set_author(name="👑 Horrific Scarecrow", url="https://discordapp.com")
            file = discord.File("./Images_Passive/hsc1.jpg", filename="hsc1.jpg")
            embed.set_image(url="attachment://hsc1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'jla':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Primordial Power""")
            embed.set_author(name="👑 Justice League Aquaman", url="https://discordapp.com")
            file = discord.File("./Images_Passive/jla1.jpg", filename="jla1.jpg")
            embed.set_image(url="attachment://jla1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'jlb':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Tactical Batsuit""")
            embed.set_author(name="👑 Justice League Batman", url="https://discordapp.com")
            file = discord.File("./Images_Passive/jlbm1.jpg", filename="jlbm1.jpg")
            embed.set_image(url="attachment://jlbm1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'jlc':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1:Cybernetic Body""")
            embed.set_author(name="👑 Justice League Cyborg", url="https://discordapp.com")
            file = discord.File("./Images_Passive/jlc1.jpg", filename="jlc1.jpg")
            embed.set_image(url="attachment://jlc1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'jlf':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Hyperspeed Assault""")
            embed.set_author(name="👑 Justice League Flash", url="https://discordapp.com")
            file = discord.File("./Images_Passive/jlf1.jpg", filename="jlf1.jpg")
            embed.set_image(url="attachment://jlf1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'jsgl':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Reinforced Constructs""")
            embed.set_author(name="👑 John Stewart Green Lantern", url="https://discordapp.com")
            file = discord.File("./Images_Passive/jsgl1.jpg", filename="jsgl1.jpg")
            embed.set_image(url="attachment://jsgl1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'kbm':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Knightmare Ambush""")
            embed.set_author(name="👑 Knightmare Batman", url="https://discordapp.com")
            file = discord.File("./Images_Passive/kbm1.jpg", filename="kbm1.jpg")
            embed.set_image(url="attachment://kbm1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'mtcw':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Finders Keepers""")
            embed.set_author(name="👑 Master Thief Catwoman", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mtcw1.jpg", filename="mtcw1.jpg")
            embed.set_image(url="attachment://mtcw1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'mvbl':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Overload""")
            embed.set_author(name="👑 Multiverse Black Lightning", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mvba.jpg", filename="mvba.jpg")
            embed.set_image(url="attachment://mvba.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'mvcc':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Cold Barrier""")
            embed.set_author(name="👑 Multiverse Captain Cold", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mvcc.jpg", filename="mvcc.jpg")
            embed.set_image(url="attachment://mvcc.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'mvsg':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Multiverse Tenacity""")
            embed.set_author(name="👑 Multiverse Supergirl", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mvsg1.jpg", filename="mvsg1.jpg")
            embed.set_image(url="attachment://mvsg1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'mvwc':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Multiverse Weapon Master""")
            embed.set_author(name="👑 Multiverse White Canary", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mvwc1.jpg", filename="mvwc1.jpg")
            embed.set_image(url="attachment://mvwc1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'mww':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: God Killer Sword""")
            embed.set_author(name="👑 Mythic Wonder Woman", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mww1.jpg", filename="mww1.jpg")
            embed.set_image(url="attachment://mww1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'nw':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Staff of Grayson""")
            embed.set_author(name="👑 Nightwing", url="https://discordapp.com")
            file = discord.File("./Images_Passive/nw1.jpg", filename="nw1.jpg")
            embed.set_image(url="attachment://nw1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'pbm':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Batwing Airstrike""")
            embed.set_author(name="👑 Predator Batman", url="https://discordapp.com")
            file = discord.File("./Images_Passive/pbm1.jpg", filename="pbm1.jpg")
            embed.set_image(url="attachment://pbm1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'pg':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Solar Energy Absorption""")
            embed.set_author(name="👑 Power Girl", url="https://discordapp.com")
            file = discord.File("./Images_Passive/pg1.jpg", filename="pg1.jpg")
            embed.set_image(url="attachment://pg1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'psg':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Powered Heat Vision""")
            embed.set_author(name="👑 Powered Supergirl", url="https://discordapp.com")
            file = discord.File("./Images_Passive/psg1.jpg", filename="psg1.jpg")
            embed.set_image(url="attachment://psg1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'pst':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Force of Nature""")
            embed.set_author(name="👑 Primal Swamp Thing", url="https://discordapp.com")
            file = discord.File("./Images_Passive/pst1.jpg", filename="pst1.jpg")
            embed.set_image(url="attachment://pst1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'rdn':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Chain Lighting""")
            embed.set_author(name="👑 Raiden", url="https://discordapp.com")
            file = discord.File("./Images_Passive/rdn1.jpg", filename="rdn1.jpg")
            embed.set_image(url="attachment://rdn1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'rf':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Reverse Time""")
            embed.set_author(name="👑 The Reverse Flash", url="https://discordapp.com")
            file = discord.File("./Images_Passive/rf1.jpg", filename="rf1.jpg")
            embed.set_image(url="attachment://rf1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'rh':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Time Extension""")
            embed.set_author(name="👑 Redhood", url="https://discordapp.com")
            file = discord.File("./Images_Passive/rh1.jpg", filename="rh1.jpg")
            embed.set_image(url="attachment://rh1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'sb':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Torment's Grasp""")
            embed.set_author(name="👑 Silver Banshee", url="https://discordapp.com")
            file = discord.File("./Images_Passive/sb1.jpg", filename="sb1.jpg")
            embed.set_image(url="attachment://sb1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'sbc':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Sonic Attack""")
            embed.set_author(name="👑 Sonic Black Canary", url="https://discordapp.com")
            file = discord.File("./Images_Passive/sbc1.jpg", filename="sbc1.jpg")
            embed.set_image(url="attachment://sbc1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'ssdf':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Reversal of Fate""")
            embed.set_author(name="👑 Soul Stealer Doctor Fate", url="https://discordapp.com")
            file = discord.File("./Images_Passive/ssdf1.jpg", filename="ssdf1.jpg")
            embed.set_image(url="attachment://ssdf1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'sff':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Lightning Reflexes""")
            embed.set_author(name="👑 Speed Force Flash", url="https://discordapp.com")
            file = discord.File("./Images_Passive/ssf1.jpg", filename="ssf1.jpg")
            embed.set_image(url="attachment://ssf1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'sz':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Klone Kombatant""")
            embed.set_author(name="👑 Sub-Zero", url="https://discordapp.com")
            file = discord.File("./Images_Passive/sz1.jpg", filename="sz1.jpg")
            embed.set_image(url="attachment://sz1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'tkgg':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Telekinesis""")
            embed.set_author(name="👑 Telekinetic Gorilla Grodd", url="https://discordapp.com")
            file = discord.File("./Images_Passive/tgg1.jpg", filename="tgg1.jpg")
            embed.set_image(url="attachment://tgg1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'ubc':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Resurrection""")
            embed.set_author(name="👑 Unbreakable Cyborg", url="https://discordapp.com")
            file = discord.File("./Images_Passive/ubc1.jpg", filename="ubc1.jpg")
            embed.set_image(url="attachment://ubc1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'uhq':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Psychotic Charm""")
            embed.set_author(name="👑 Unhinged Harley Quinn", url="https://discordapp.com")
            file = discord.File("./Images_Passive/uhq1.jpg", filename="uhq1.jpg")
            embed.set_image(url="attachment://uhq1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'wqww':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Amazon Warriors""")
            embed.set_author(name="👑 Warrior Queen Wonder Woman", url="https://discordapp.com")
            file = discord.File("./Images_Passive/wqww1.jpg", filename="wqww1.jpg")
            embed.set_image(url="attachment://wqww1.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'bm':
            embed = discord.Embed(colour=discord.Colour(0x800080),
                                  description="""Passive 1: Open Wounds\nPassive 2: Revenge Mission\nPassive 3: Black Manta Suit""")
            embed.set_author(name="👑 Black Manta", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/bm_full.jpg", filename="bm_full.jpg")
            embed.set_image(url="attachment://bm_full.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'bnc':
            embed = discord.Embed(colour=discord.Colour(0x800080),
                                  description="""Passive 1: Force Field\nPassive 2: Living Metal\nPassive 3: 12th Level Intellect""")
            embed.set_author(name="👑 Brainiac", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/brainy_full.jpg", filename="brainy_full.jpg")
            embed.set_image(url="attachment://brainy_full.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'bncw':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Blinding Strikes\nPassive 2: 9 Lives\nPassive 3: Are You Kitten Me?""")
            embed.set_author(name="👑 Batman Ninja Catwoman", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/bncw_full.jpg", filename="bncw_full.jpg")
            embed.set_image(url="attachment://bncw_full.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'bngg':
            embed = discord.Embed(colour=discord.Colour(0x800080),
                                  description="""Passive 1: Crippling Blow\nPassive 2: Dramatic Reversal\nPassive 3: Master Plan""")
            embed.set_author(name="👑 Batman Ninja Gorilla Grodd", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/bngg_full.jpg", filename="bngg_full.jpg")
            embed.set_image(url="attachment://bngg_full.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'bnr':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Combo Kid\nPassive 2: Ninja Lethality\nPassive 3: Monkey Style Swordplay""")
            embed.set_author(name="👑 Batman Ninja Robin", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/bnr_full.jpg", filename="bnr_full.jpg")
            embed.set_image(url="attachment://bnr_full.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'cbm':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Batman Inc.\nPassive 2: Classically Trained\nPassive 3: Power Seize""")
            embed.set_author(name="👑 Classic Batman", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/cbm_full.jpg", filename="cbm_full.jpg")
            embed.set_image(url="attachment://cbm_full.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'ds':
            embed = discord.Embed(colour=discord.Colour(0x800080),
                                  description="""Passive 1: Parademons\nPassive 2: Sacrifices Are Necessary\nPassive 3: Apokolips Bombardment""")
            embed.set_author(name="👑 Darkseid", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/ds_full.jpg", filename="ds_full.jpg")
            embed.set_image(url="attachment://ds_full.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'epi':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Entangling Vines\nPassive 2: Toxins\nPassive 3: Regrowth""")
            embed.set_author(name="👑 Entangling Poison Ivy", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/epi_full.jpg", filename="epi_full.jpg")
            embed.set_image(url="attachment://epi_full.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'hbhq':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: It's Not Me, It's You\nPassive 2: Let Your Guard Down\nPassive 3: Straight To The Heart""")
            embed.set_author(name="👑 Heart Breaker Harley Quinn", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/hbhq_full.jpg", filename="hbhq_full.jpg")
            embed.set_image(url="attachment://hbhq_full.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'koaam':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Building Tsunami\nPassive 2: Ocean's Retribution\nPassive 3: Waters of Life""")
            embed.set_author(name="👑 King of Atlantis Aquaman", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/koaam_full.jpg", filename="koaam_full.jpg")
            embed.set_image(url="attachment://koaam_full.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'llj':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Killing Joker\nPassive 2: Joker Venom\nPassive 3: Caught You Off Guard""")
            embed.set_author(name="👑 Last Laugh Joker", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/llj_full.jpg", filename="llj_full.jpg")
            embed.set_image(url="attachment://llj_full.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'mvasg':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Multiverse Power\nPassive 2: Fueled By Might\nPassive 3: Interruption""")
            embed.set_author(name="👑 Multiverse Armored Supergirl", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/mvasg_full.jpg", filename="mvasg_full.jpg")
            embed.set_image(url="attachment://mvasg_full.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'mvbw':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Tactical Strikes\nPassive 2: Tactical Rep\nPassive 3: Combat Focus""")
            embed.set_author(name="👑 Multiverse Batwoman", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/mvbw_full.jpg", filename="mvbw_full.jpg")
            embed.set_image(url="attachment://mvbw_full.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'mvf':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Multiverse Critical\nPassive 2: Multiverse Haste\nPassive 3: S. T. A. R. LABS""")
            embed.set_author(name="👑 Multiverse The Flash", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/mvf_full.jpg", filename="mvf_full.jpg")
            embed.set_image(url="attachment://mvf_full.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'mvga':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Multiverse Power Drain\nPassive 2: Multiverse Incendiaries\nPassive 3: Endurance Training""")
            embed.set_author(name="👑 Multiverse Green Arrow", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/mvga_full.jpg", filename="mvga_full.jpg")
            embed.set_image(url="attachment://mvga_full.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'shz' or cmd =='szm':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Courage of Achilles\nPassive 2: Retribution of Zeus\nPassive 3: Stamina of Atlas""")
            embed.set_author(name="👑 Shazam", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/shz_full.jpg", filename="shz_full.jpg")
            embed.set_image(url="attachment://shz_full.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'ssds':
            embed = discord.Embed(colour=discord.Colour(0xFFD700),
                                  description="""Passive 1: Sniper\nPassive 2: Suppressive Fire\nPassive 3: Assassin""")
            embed.set_author(name="👑 Suicide Squad Deadshot", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/ssds_full.jpg", filename="ssds_full.jpg")
            embed.set_image(url="attachment://ssds_full.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'sshq':
            embed = discord.Embed(colour=discord.Colour(0x800080),
                                  description="""Passive 1: The Suicide Squad\nPassive 2: Psychoanalyze\nPassive 3: Twisted Love""")
            embed.set_author(name="👑 Suicide Squad Harley Quinn", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/sshq_full.jpg", filename="sshq_full.jpg")
            embed.set_image(url="attachment://sshq_full.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'gaww':
            embed = discord.Embed(colour=discord.Colour(0x800080),
                                  description="""Passive 1: Athena's Power\nPassive 2: Divine Protection\nPassive 3: Offensive Guard""")
            embed.set_author(name="👑 Golden Armor Wonder Woman", url="https://discordapp.com")
            file = discord.File("./Images_Passive/gaww.jpg", filename="gaww.jpg")
            embed.set_image(url="attachment://gaww.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'dtk':
            embed = discord.Embed(colour=discord.Colour(0x800080),
                                  description="""Passive 1: Athena's Power\nPassive 2: Divine Protection\nPassive 3: Offensive Guard""")
            embed.set_author(name="👑 Deathstroke", url="https://discordapp.com")
            file = discord.File("./Images_Passive/mto_passives/dtk_full.png", filename="dtk_full.png")
            embed.set_image(url="attachment://dtk_full.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        elif cmd == 'vixen':
            embed = discord.Embed(colour=discord.Colour(0x800080),
                                  description="""Passive 1: Wolf Pack\nPassive 2: Steel Claws\nPassive 3: Chameleon""")
            embed.set_author(name="👑 Vixen", url="https://discordapp.com")
            file = discord.File("./Images_Passive/vixen.jpg", filename="vixen.jpg")
            embed.set_image(url="attachment://vixen.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(file=file, embed=embed)
        else:
            embed = discord.Embed(colour=discord.Colour(0xEE82EE), url="https://discordapp.com",
                                  description="You have typed a command which is not present in the command list, to know the passive commands, type ```i!p``` or ```i!passive```")
            embed.set_author(name="Something wrong with Passive command..", url="https://discordapp.com")
            error = ['https://media.giphy.com/media/3oEjHERaTIdeuFQrXq/giphy.gif',
                     'https://media.giphy.com/media/3osxY9kuM2NGUfvThe/giphy.gif',
                     'https://media.giphy.com/media/8L0Pky6C83SzkzU55a/giphy.gif',
                     'https://media.giphy.com/media/fV1yHo8YyoKjzvMCKr/giphy.gif',
                     'https://media.giphy.com/media/TqiwHbFBaZ4ti/giphy.gif',
                     'https://media.giphy.com/media/ifdPjn6m4WyNlnXMTj/giphy.gif']
            embed.set_image(url=choice(error))
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)

            await ctx.channel.send(embed=embed)


def setup(client):
    client.add_cog(CharPassive(client))