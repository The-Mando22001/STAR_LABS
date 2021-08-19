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

            embed.add_field(name="Advent of Chaos Artifacts",
            value="""These artifacts can be obtained from Solo Raids. When equipped, these artifacts provide boost in parameters while playing solo raids. Following are the list of artifacts under this category:
```Sword of Salvation - salvation
Crown of Horus - crown
Sword of Sin - sin
Book of Souls - bos
Rings of Azar - roa
Philosopher's Stone - stone
Ace of Winchesters - ace
Trigon's Power Staff - tps
Candle of Neron - con
Chakra - chakra 
```""")
            embed.add_field(name="Promethium Artifacts",
                            value="""Stun your enemies with Energy Lance, become unblockable with God Killer, and heal yourself with the Ikon Suit. Defeat The Last Contract bosses to earn the new Artifacts.. Following are the different artifacts present:
```**Silver Tier**
Promethium Nunchucks - nun
Premethium Grenades - grenade
Promethium Knife - knife
Rocket Boots - rb

**Gold Tier**
Promethium Sword - sword
Speedforce Battery - sfb
Energy Lance - el
Legacy Helmet - lh

**Legendary Tier**
God killer - gk
Ikon Suit - ikon```""")

            embed.add_field(name="Usage of Command",
                            value="To get more information on each artifact, for example, to get info about claw of horus, type, ```i!art coh``` and you will get the info. Similarly, you need to type the command as, ```i!art [Artifact command]``` to get info on the respective artifact. Where,\nArtifact command - written beside the artifacts in the artifacts list. To get the list, type, ```i!art```\n\n__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).")
            embed.set_author(name="Artifact Info", url="https://discordapp.com",
                             icon_url="https://cdn.discordapp.com/embed/avatars/3.png")
            await ctx.channel.send(embed=embed)
        if cmd == 'tech':
            embed = discord.Embed(colour=discord.Colour(0x0cf700),
                                  description="""**Effects**
-Gain a percentage in Health
-[Tech characters] Gain a percentage in Attack against Might Heroes

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Amulet of Tech", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/A_Tech.png", filename="A_Tech.png")
            embed.set_image(url="attachment://A_Tech.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'arcane':
            embed = discord.Embed(colour=discord.Colour(0x0cf700),
                                  description="""**Effects:**
-Additional percentage of Special attack Damage
-[Arcane Characters] Gain a percentage in Attack against Arcane Heroes

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Amulet of Arcane", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/A_Arcane.png", filename="A_Arcane.png")
            embed.set_image(url="attachment://A_Arcane.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'meta':
            embed = discord.Embed(colour=discord.Colour(0x0cf700),
                                  description="""**Effects:**
-Increase all healing effects on self by a percentage and teammates by a percentage.
-[Metahuman Characters] Gain a percentage in Attack against Tech Heroes

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Amulet of Metahuman", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/A_Meta.png", filename="A_Meta.png")
            embed.set_image(url="attachment://A_Meta.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'might':
            embed = discord.Embed(colour=discord.Colour(0x0cf700),
                                  description="""**Effects:**
-Gain a percentage of Damage for Basic, Tag, and Swipe attacks
-[Might Characters] Gain a percentage in Attack against Agility Heroes

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Amulet of Might", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/A_Might.png", filename="A_Might.png")
            embed.set_image(url="attachment://A_Might.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'agility':
            embed = discord.Embed(colour=discord.Colour(0x0cf700),
                                  description="""**Effects:**
-Plus a percentage DoT Damage
-[Agility Characters] Gain a percentage in Attack against Metahuman Heroes

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Amulet of Agility", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/A_Agility.png", filename="A_Agility.png")
            embed.set_image(url="attachment://A_Agility.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'tab':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""**Effects:**
-Gain a percentage in Attack on tag-in for a brief amount of time and inflict DoT on self, dealing 20% of current health in damage
-[Red Hood] Gain a percentage in Lethal Chance and reduces Supermove cost by 5

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="The All - Blades", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/tab.png", filename="tab.png")
            embed.set_image(url="attachment://tab.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'coh':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""**Effects:**
-Gain a percentage in Attack
-A percentage of chance to Stun on Swipe attack and Jump attacks.

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Claw of Horus", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/coh.png", filename="coh.png")
            embed.set_image(url="attachment://coh.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'cs':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""**Effects:**
-Whenever losing greater than 10% of max Health from a single attack, gain a shield that blocks a percentage of all incoming damage for a short amount of time.
-While shield is active, reflect a percentage of damage from Special attacks

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Cosmic Staff", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/cs.png", filename="cs.png")
            embed.set_image(url="attachment://cs.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'regen':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""**Effects:**
-Once per battle, revive with a percentage of health when knocked out
-[Superman] Gain a percentage of Attack when revived

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Kryptonian Regeneration Matrix", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/regen.png", filename="regen.png")
            embed.set_image(url="attachment://regen.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'nth':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""**Effects:**
-Gain a percentage in Health
-Gain a small percentage in Attack for each percent of currently missing Health
-[Legendary Characters] A percentage of damage dealt to the active Hero is split between all teammates

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Nth Metal Armor", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/nth.png", filename="nth.png")
            embed.set_image(url="attachment://nth.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'rod':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Apokolips Artifact
                                  
__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Mega Rod", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/ak_mega.jpg", filename="ak_mega.jpg")
            embed.set_image(url="attachment://ak_mega.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'radion':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Apokolips Artifact
                                  
__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Radion", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/ak_radion.jpg", filename="ak_radion.jpg")
            embed.set_image(url="attachment://ak_radion.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'axe':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Apokolips Artifact
                                  
__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Electro Axe", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/ak_axe.jpg", filename="ak_axe.jpg")
            embed.set_image(url="attachment://ak_axe.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'entropy':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Apokolips Artifact
                                  
__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Entropy Aegis", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/ak_entropy.jpg", filename="ak_entropy.jpg")
            embed.set_image(url="attachment://ak_entropy.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'hod':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Apokolips Artifact
                                  
__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Heart of Darkness", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/ak_hod.jpg", filename="ak_hod.jpg")
            embed.set_image(url="attachment://ak_hod.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'fb':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Apokolips Artifact
                                  
__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Father Box", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/ak_fb.jpg", filename="ak_fb.jpg")
            embed.set_image(url="attachment://ak_fb.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'spear':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Kryptonite Artifact
                                  
__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Kryptonite Spear", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/rok_spear.jpg", filename="rok_spear.jpg")
            embed.set_image(url="attachment://rok_spear.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'blade':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Kryptonite Artifact
                                  
__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Flashing Blade", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/rok_blade.jpg", filename="rok_blade.jpg")
            embed.set_image(url="attachment://rok_blade.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'harness':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Kryptonite Artifact
                                  
__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Astro-Harness", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/rok_harness.jpg", filename="rok_harness.jpg")
            embed.set_image(url="attachment://rok_harness.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'ring':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Kryptonite Artifact
                                  
__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Kryptonite Ring", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/rok_ring.jpg", filename="rok_ring.jpg")
            embed.set_image(url="attachment://rok_ring.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'gloves':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Kryptonite Artifact
                                  
__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Kryptonite Gloves", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/rok_gloves.jpg", filename="rok_gloves.jpg")
            embed.set_image(url="attachment://rok_gloves.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'suit':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Kryptonite Artifact
                                  
__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Lexcorp Warsuit", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/rok_warsuit.jpg", filename="rok_warsuit.jpg")
            embed.set_image(url="attachment://rok_warsuit.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'club':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Kryptonite Artifact
                                  
__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Beta Club", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/rok_club.jpg", filename="rok_club.jpg")
            embed.set_image(url="attachment://rok_club.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'mps':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Kryptonite Artifact
                                  
__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Metallo's Power Source", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/rok_powsource.jpg", filename="rok_powsource.jpg")
            embed.set_image(url="attachment://rok_powsource.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'knife':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Kryptonite Artifact
                                  
__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Kryptonite Knife", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/rok_knife.jpg", filename="rok_knife.jpg")
            embed.set_image(url="attachment://rok_knife.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)
        if cmd == 'bullets':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Kryptonite Artifact
                                  
__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Kryptonite Bullets", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/rok_bullets.jpg", filename="rok_bullets.jpg")
            embed.set_image(url="attachment://rok_bullets.jpg")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)

        if cmd == 'salvation':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""__Advent of Chaos Artifact__

- % chance to steal 3 power bars with a successful swipe attack.
- x Damage for each opponent's absent Power Bar.

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Sword of Salvation", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/aoc_salvation.jpg", filename="aoc_salvation.jpg")
            embed.set_image(url="attachment://aoc_salvation.jpg")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/655475178083581993/826137331094388776/Chaos_SwordOfSalvation.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)

        if cmd == 'crown':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""__Advent of Chaos Artifact__

- x Damage for Special 1, Special 2, and Special 3.
- % special attack damage
- % chance to resist Power Drain
- x Power Drain Resistance  

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Crown of Horns", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/aoc_crown.jpg", filename="aoc_crown.jpg")
            embed.set_image(url="attachment://aoc_crown.jpg")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/655475178083581993/826137331320750080/Chaos_CrownOfHorns.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)

        if cmd == 'sin':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""__Advent of Chaos Artifact__

- x seconds of Burn on succesful special
- Drain opponent for x Power bars every second after succesful Special for x seconds

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Sword of Sin", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/aoc_sin.jpg", filename="aoc_sin.jpg")
            embed.set_image(url="attachment://aoc_sin.jpg")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/655475178083581993/826137331525746707/Chaos_SwordOfSin.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)

        if cmd == 'bos':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""__Advent of Chaos Artifact__

- % duration of buffs applied to wearer
- % duration of Debuffs applied to opponent by the wearer

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Book of Souls", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/aoc_bos.jpg", filename="aoc_bos.jpg")
            embed.set_image(url="attachment://aoc_bos.jpg")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/655475178083581993/826137331739131954/Chaos_BookOfSouls.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)

        if cmd == 'roa':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""__Advent of Chaos Artifact__

- x incoming damage for Special Abilities
- % damage from incoming Specials
- % chance to gain 4 power bars after successfully blocking an incoming special

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Rings of Azar", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/aoc_roa.jpg", filename="aoc_roa.jpg")
            embed.set_image(url="attachment://aoc_roa.jpg")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/655475178083581993/826137331928268820/Chaos_RingsOfAzar.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)

        if cmd == 'stone':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""__Advent of Chaos Artifact__

- % chance to mitigate additional  x damage from Specials while blocking
- Heal for % of mitigated damage
                                  
__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Philosopher's Stone", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/aoc_stone.jpg", filename="aoc_stone.jpg")
            embed.set_image(url="attachment://aoc_stone.jpg")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/655475178083581993/826155117987889162/Chaos_PhilosophersStone.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)

        if cmd == 'ace':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""__Advent of Chaos Artifact__

- % chance to Armor Pierce on Ranged Attacks
- % chance for Ranged Attack to be unblockable
- % damage to an opponent with Health below %

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Ace of Winchesters", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/aoc_ace.jpg", filename="aoc_ace.jpg")
            embed.set_image(url="attachment://aoc_ace.jpg")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/655475178083581993/826137332310474762/Chaos_AceOfWinchesters.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)

        if cmd == 'tps':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""__Advent of Chaos Artifact__

- When blocking incoming special gain a shield with x capacity of wearer's max health for x seconds
- Shield gets weaker over time, transforming 5% of its max capacity into wearer's health every second
- x damage absorbed by shield reflects back to an opponent

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Trigon's Power Staff", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/aoc_tps.jpg", filename="aoc_tps.jpg")
            embed.set_image(url="attachment://aoc_tps.jpg")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/655475178083581993/826137332435910736/Chaos_TrigonsPowerStaff.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)

        if cmd == 'con':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""__Advent of Chaos Artifact__

- % power generation
- Random special is disabled upon tag-in. The rest of specials have + x damage
- x power generation for x time
- Cannot be triggered if all the Specials are disabled

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Candle of Neron", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/aoc_con.jpg", filename="aoc_con.jpg")
            embed.set_image(url="attachment://aoc_con.jpg")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/655475178083581993/826137332612333629/Chaos_CandleofNeron.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)

        if cmd == 'chakra':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""__Advent of Chaos Artifact__

- When health drops below % enter possessed state for x seconds. % attack while possessed
- While possessed heal for x of damage dealt with Specials Attacks.

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Chakra", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/aoc_chakra.jpg", filename="aoc_chakra.jpg")
            embed.set_image(url="attachment://aoc_chakra.jpg")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/655475178083581993/826137332134576138/Chaos_ChakraGem.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)

        if cmd == 'el':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""__The Last Contract Artifacts__

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Energy Lance", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/pro_el.jpg", filename="pro_el.jpg")
            embed.set_image(url="attachment://pro_el.jpg")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/655475178083581993/869244592661344386/image1.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",
                icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)

        if cmd == 'gk':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""__The Last Contract Artifacts__

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="God Killer", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/pro_gk.jpg", filename="pro_gk.jpg")
            embed.set_image(url="attachment://pro_gk.jpg")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/655475178083581993/869244593311449098/image3.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",
                icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)

        if cmd == 'grenade':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""__The Last Contract Artifacts__

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Promethium Grenades", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/pro_grenades.jpg", filename="pro_grenades.jpg")
            embed.set_image(url="attachment://pro_grenades.jpg")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/655475178083581993/869244592950771743/image2.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",
                icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)

        if cmd == 'ikon':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""__The Last Contract Artifacts__

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Ikon Suit", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/pro_ikon.jpg", filename="pro_ikon.jpg")
            embed.set_image(url="attachment://pro_ikon.jpg")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/655475178083581993/869244593638633512/image4.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",
                icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)

        if cmd == 'knife':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""__The Last Contract Artifacts__

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Promethium Knife", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/pro_knife.jpg", filename="pro_knife.jpg")
            embed.set_image(url="attachment://pro_knife.jpg")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/655475178083581993/869244592325795940/image0.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",
                icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)

        if cmd == 'lh':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""__The Last Contract Artifacts__

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Legacy Helmet", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/pro_lh.jpg", filename="pro_lh.jpg")
            embed.set_image(url="attachment://pro_lh.jpg")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/655475178083581993/869244593986748456/image5.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",
                icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)

        if cmd == 'nun':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""__The Last Contract Artifacts__

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Promethium Nunchucks", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/pro_nun.jpg", filename="pro_nun.jpg")
            embed.set_image(url="attachment://pro_nun.jpg")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/655475178083581993/869244594372628570/image6.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",
                icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)

        if cmd == 'rb':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""__The Last Contract Artifacts__

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Rocket Boots", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/pro_rb.jpg", filename="pro_rb.jpg")
            embed.set_image(url="attachment://pro_rb.jpg")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/655475178083581993/869244594674622504/image7.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",
                icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)

        if cmd == 'sfb':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""__The Last Contract Artifacts__

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Speedforce Battery", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/pro_sfb.jpg", filename="pro_sfb.jpg")
            embed.set_image(url="attachment://pro_sfb.jpg")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/655475178083581993/869244594934657074/image8.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",
                icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)

        if cmd == 'sword':
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""__The Last Contract Artifacts__

__**Note**__: If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Promethium Sword", url="https://discordapp.com")
            file = discord.File("./Images_Artifacts/pro_sword.jpg", filename="pro_sword.jpg")
            embed.set_image(url="attachment://pro_sword.jpg")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/655475178083581993/869244595215667230/image9.png")
            embed.set_footer(
                text=f"Requested by: {ctx.message.author.name} at {ctx.message.guild.name}",
                icon_url=ctx.guild.icon_url)
            await ctx.channel.send(embed=embed, file=file)

def setup(client):
    client.add_cog(ArtifactInfo(client))