import discord
from discord.ext import commands

class ArtifactInfo(commands.Cog):
    def __init__(self, client):
        self.Bot = client

    @commands.command()
    async def art(self, ctx, cmd: str = None):
        if cmd is None:
            embed = discord.Embed(colour=discord.Colour(0x0cf700),
                                  description="Artifacts can be equipped on any Hero but some grant additional bonuses when used on specific Heroes or Classes. Artifacts are very rare but they can be earned through Raid Rewards. Artifacts can be upgraded like normal Gear, but use a new unique material called Azure Artifact Fragments. The max Artifact level is 10. Earn Azure Artifact Fragments in Raids 5, 6, 7, or 8. There are two types of artifacts after the recent addition of Solo Raids. They are:\n1. Normal Artifacts\n2. Apokolips Artifact")
            embed.add_field(name="Normal Artifacts",
                            value="""Normal artifacts can be obtained from league raids. Following are the different artifacts present:
```**Silver Tier**
Amulet of Tech - tech
Amulet of Arcane - arcane
Amulet of Metahuman - meta
Amulet of Might - might
Amulet of Agility - agility

**Gold Tier**
The All - Blades - tab
Claw of Horus - coh
Cosmic Staff - cs

**Legendary Tier**
Kryptonian Regenration Matrix - regen
Nth Metal Armor - nth```""")
            embed.add_field(name="Apokolips Artifacts",
                            value="""These artifacts can be obtained from Solo Raids. When equipped, these artifacts provide boost in parameters while playing solo raids. Following are the different artifacts present:
```**Silver Tier**
Mega Rod - rod

**Gold Tier**
Radion - radion
Electro Axe - axe

**Legendary Tier**
Entropy Aegis - entropy
Heart of Darkness - hod
Father Box - fb```""")
            embed.add_field(name="Kryptonite Artifacts",
                            value="""These artifacts can be obtained from Solo Raids. When equipped, these artifacts provide boost in parameters while playing solo raids. Following are the different artifacts present:
```**Silver Tier**
Kryptonite Ring - ring
Kryptonite Knife - knife
Kryptonite gloves - gloves
Kryptonite Bullets - bullets

**Gold Tier**
Metallo's Power Source - mps
Astro-Harness - harness
Flashing Blade - blade
Beta Club - club

**Legendary Tier**
Lexcorp Warsuit - suit
Kryptonite Spear - spear```""")
            embed.add_field(name="Usage of Command",
                            value="To get more information on each artifact, for example, to get info about claw of horus, type, ```i!art coh``` and you will get the info. Similarly, you need to type the command as, ```i!art [Artifact command]``` to get info on the respective artifact. Where,\nArtifact command - written beside the artifacts in the artifacts list. To get the list, type, ```i!art```")
            embed.set_author(name="Artifact Info", url="https://discordapp.com",
                             icon_url="https://cdn.discordapp.com/embed/avatars/3.png")
            await ctx.channel.send(embed=embed)
        if cmd == 'tech':
            embed = discord.Embed(colour=discord.Colour(0x0cf700),
                                  description="""**Effects**
-Gain a percentage in Health
-[Tech characters] Gain a percentage in Attack against Might Heroes""")
            embed.set_author(name="Amulet of Tech", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/A_Tech.png", filename="A_Tech.png")
            embed.set_image(url="attachment://A_Tech.png")
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'arcane':
            embed = discord.Embed(colour=discord.Colour(0x0cf700),
                                  description="""**Effects:**
-Additional percentage of Special attack Damage
-[Arcane Characters] Gain a percentage in Attack against Arcane Heroes""")
            embed.set_author(name="Amulet of Arcane", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/A_Arcane.png", filename="A_Arcane.png")
            embed.set_image(url="attachment://A_Arcane.png")
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'meta':
            embed = discord.Embed(colour=discord.Colour(0x0cf700),
                                  description="""**Effects:**
-Increase all healing effects on self by a percentage and teammates by a percentage.
-[Metahuman Characters] Gain a percentage in Attack against Tech Heroes""")
            embed.set_author(name="Amulet of Metahuman", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/A_Meta.png", filename="A_Meta.png")
            embed.set_image(url="attachment://A_Meta.png")
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'might':
            embed = discord.Embed(colour=discord.Colour(0x0cf700),
                                  description="""**Effects:**
-Gain a percentage of Damage for Basic, Tag, and Swipe attacks
-[Might Characters] Gain a percentage in Attack against Agility Heroes""")
            embed.set_author(name="Amulet of Might", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/A_Might.png", filename="A_Might.png")
            embed.set_image(url="attachment://A_Might.png")
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'agility':
            embed = discord.Embed(colour=discord.Colour(0x0cf700),
                                  description="""**Effects:**
-Plus a percentage DoT Damage
-[Agility Characters] Gain a percentage in Attack against Metahuman Heroes""")
            embed.set_author(name="Amulet of Agility", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/A_Agility.png", filename="A_Agility.png")
            embed.set_image(url="attachment://A_Agility.png")
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'tab':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""**Effects:**
-Gain a percentage in Attack on tag-in for a brief amount of time and inflict DoT on self, dealing 20% of current health in damage
-[Red Hood] Gain a percentage in Lethal Chance and reduces Supermove cost by 5""")
            embed.set_author(name="The All - Blades", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/tab.png", filename="tab.png")
            embed.set_image(url="attachment://tab.png")
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'coh':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""**Effects:**
-Gain a percentage in Attack
-A percentage of chance to Stun on Swipe attack and Jump attacks.""")
            embed.set_author(name="Claw of Horus", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/coh.png", filename="coh.png")
            embed.set_image(url="attachment://coh.png")
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'cs':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""**Effects:**
-Whenever losing greater than 10% of max Health from a single attack, gain a shield that blocks a percentage of all incoming damage for a short amount of time.
-While shield is active, reflect a percentage of damage from Special attacks""")
            embed.set_author(name="Cosmic Staff", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/cs.png", filename="cs.png")
            embed.set_image(url="attachment://cs.png")
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'regen':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""**Effects:**
-Once per battle, revive with a percentage of health when knocked out
-[Superman] Gain a percentage of Attack when revived""")
            embed.set_author(name="Kryptonian Regeneration Matrix", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/regen.png", filename="regen.png")
            embed.set_image(url="attachment://regen.png")
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'nth':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""**Effects:**
-Gain a percentage in Health
-Gain a small percentage in Attack for each percent of currently missing Health
-[Legendary Characters] A percentage of damage dealt to the active Hero is split between all teammates""")
            embed.set_author(name="Nth Metal Armor", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/nth.png", filename="nth.png")
            embed.set_image(url="attachment://nth.png")
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'rod':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Apokolips Artifact""")
            embed.set_author(name="Mega Rod", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/ak_mega.jpg", filename="ak_mega.jpg")
            embed.set_image(url="attachment://ak_mega.jpg")
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'radion':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Apokolips Artifact""")
            embed.set_author(name="Radion", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/ak_radion.jpg", filename="ak_radion.jpg")
            embed.set_image(url="attachment://ak_radion.jpg")
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'axe':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Apokolips Artifact""")
            embed.set_author(name="Electro Axe", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/ak_axe.jpg", filename="ak_axe.jpg")
            embed.set_image(url="attachment://ak_axe.jpg")
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'entropy':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Apokolips Artifact""")
            embed.set_author(name="Entropy Aegis", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/ak_entropy.jpg", filename="ak_entropy.jpg")
            embed.set_image(url="attachment://ak_entropy.jpg")
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'hod':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Apokolips Artifact""")
            embed.set_author(name="Heart of Darkness", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/ak_hod.jpg", filename="ak_hod.jpg")
            embed.set_image(url="attachment://ak_hod.jpg")
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'fb':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Apokolips Artifact""")
            embed.set_author(name="Father Box", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/ak_fb.jpg", filename="ak_fb.jpg")
            embed.set_image(url="attachment://ak_fb.jpg")
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'spear':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Kryptonite Artifact""")
            embed.set_author(name="Kryptonite Spear", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/rok_spear.jpg", filename="rok_spear.jpg")
            embed.set_image(url="attachment://rok_spear.jpg")
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'blade':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Kryptonite Artifact""")
            embed.set_author(name="Flashing Blade", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/rok_blade.jpg", filename="rok_blade.jpg")
            embed.set_image(url="attachment://rok_blade.jpg")
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'harness':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Kryptonite Artifact""")
            embed.set_author(name="Astro-Harness", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/rok_harness.jpg", filename="rok_harness.jpg")
            embed.set_image(url="attachment://rok_harness.jpg")
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'ring':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Kryptonite Artifact""")
            embed.set_author(name="Kryptonite Ring", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/rok_ring.jpg", filename="rok_ring.jpg")
            embed.set_image(url="attachment://rok_ring.jpg")
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'gloves':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Kryptonite Artifact""")
            embed.set_author(name="Kryptonite Gloves", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/rok_gloves.jpg", filename="rok_gloves.jpg")
            embed.set_image(url="attachment://rok_gloves.jpg")
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'suit':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Kryptonite Artifact""")
            embed.set_author(name="Lexcorp Warsuit", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/rok_warsuit.jpg", filename="rok_warsuit.jpg")
            embed.set_image(url="attachment://rok_warsuit.jpg")
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'club':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Kryptonite Artifact""")
            embed.set_author(name="Beta Club", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/rok_club.jpg", filename="rok_club.jpg")
            embed.set_image(url="attachment://rok_club.jpg")
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'mps':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Kryptonite Artifact""")
            embed.set_author(name="Metallo's Power Source", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/rok_powsource.jpg", filename="rok_powsource.jpg")
            embed.set_image(url="attachment://rok_powsource.jpg")
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'knife':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Kryptonite Artifact""")
            embed.set_author(name="Kryptonite Knife", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/rok_knife.jpg", filename="rok_knife.jpg")
            embed.set_image(url="attachment://rok_knife.jpg")
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'bullets':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Kryptonite Artifact""")
            embed.set_author(name="Kryptonite Bullets", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/rok_bullets.jpg", filename="rok_bullets.jpg")
            embed.set_image(url="attachment://rok_bullets.jpg")
            await ctx.channel.send(embed=embed, file=file)

def setup(client):
    client.add_cog(ArtifactInfo(client))