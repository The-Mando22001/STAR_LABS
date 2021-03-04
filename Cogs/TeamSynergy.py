import discord
from discord.ext import commands
from discord.ext.commands import CheckFailure
from random import choice
import Bot


class SynergyToggleError(commands.CheckFailure):
    pass


v_status = True
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


def check_toggle():
    async def predicate(ctx):
        if not Bot.synergy_feature[ctx.message.guild.id]:
            raise SynergyToggleError('Team Synergy Feature is switched off. Ask your Admin or Mod to enable it!')
        return True

    return commands.check(predicate)


class TeamSynergy(commands.Cog):
    def __init__(self, bot):
        self.Bot = bot

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def toggle_syn(self, ctx, cmd: str = None):
        if cmd == 'status':
            if Bot.synergy_feature[ctx.guild.id]:
                feature = "on"
            else:
                feature = "off"
            await ctx.channel.send(f"Current status of Synergy command is {feature}")
        if cmd == 'on':
            global v_status
            v_status = True
            Bot.synergy_feature[ctx.message.guild.id] = v_status
            await ctx.channel.send("Synergy commands enabled")
        if cmd == 'off':
            v_status = False
            Bot.voice_feature[ctx.message.guild.id] = v_status
            await ctx.channel.send("Synergy commands disabled")

    @toggle_syn.error
    async def prefix_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""You don't have the right permissions to toggle the synergy commands feature! Ask a moderator or admin to do it.""")
            embed.set_author(name=choice(bruh), url="https://discordapp.com")
            embed.set_image(url=choice(gifs))
            await ctx.channel.send(embed=embed)


    @commands.command(name='syn')
    @commands.guild_only()
    async def syn(self, ctx, cmd: str = None):
        if cmd is None:
            embed = discord.Embed(colour=discord.Colour(0x10e0a5),
                                  description="This command will show how to create team synergy by grouping together specific sets of characters from your roster. These characters can share and receive bonuses from their passive abilities with their teammates, benefiting your team and weakening your opponents.\n\nYou can see each character’s passives in detail by opening the abilities section when selecting the hero card from your roster.")
            embed.add_field(name="Team Synergy List",
                            value="The following list shows the teams available for creating team synergy:```1. Suicide Squad - ssq\n2. Justice League - jl\n3. Batman Ninja - bn\n4. League of Anarchy - loa\n5. Multiverse Team - mv```")
            embed.add_field(name="Command Usage",
                            value="Each team has it's own command. So, to check team synergy of any team, type ```i!syn [team command]```For Example, ```i!syn bn```For Batman Ninja Team Synergy details.\n\nIf you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: Support server link - [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).")
            embed.set_author(name="Team Synergy Command", url="https://discordapp.com")
            embed.set_footer(
                text=f"Last used by: {ctx.message.author.name} | Wanna find out who helped in moulding this bot into a successful one? Type i!credits to get the answer.")
            await ctx.channel.send(embed=embed)

        if cmd == 'ssq':
            embed = discord.Embed(colour=discord.Colour(0x10e0a5),
                                  description="""Enchantress can be used as a strong counter to opponents that have a focus on critical attacks. With each instance of resisting a critical attack, the SSQ team member is healed for 10 seconds. This is intensified by Harley Quinn being immune to Critical Attacks and having the ability to steal a random stat from your opponent.

In addition to a successful Ranged Attack from Deadshot having a chance to disable the movement of his opponent, there is the possibility for Enchantress' passive to steal part of the opponent's current power.

Finally, Harley reduces the cost of the Suicide Squad's team's Power bar cost.

*"So that's it, huh? We're some kind of Suicide squad?"* - Suicide Squad Team

If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: Support server link - [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Suicide Squad Team Synergy", url="https://discordapp.com")
            embed.set_footer(
                text=f"Last used by: {ctx.message.author.name} | Wanna find out who helped in moulding this bot into a successful one? Type i!credits to get the answer.")
            file = discord.File("./Images_Syn/ssq.jpg", filename="ssq.jpg")
            embed.set_image(url="attachment://ssq.jpg")
            await ctx.channel.send(embed=embed, file=file)

        if cmd == 'jl':
            embed = discord.Embed(colour=discord.Colour(0x10e0a5),
                                  description="""Cyborg’s team damage boost is a common staple for a Justice League team. When stacked with the temporary attack boost for Mythic Wonder Woman when she defeats an opponent, momentum can pick up quickly.

For an offensive focused team, The Flash will grant you an unblockable special ability or you can benefit from Aquaman adding armor piercing to all basic attacks.

Defensive-minded players will gravitate towards teams that include Batman so all teammates can ignore damage from one special ability per battle. The Legendary Justice League Superman improves the defense of your entire Justice League team and benefits from being paired with and against any Batman or Wonder Woman.  Finally, Aquaman can revive a knocked-out teammate when he uses his Supermove.

*"People said the age of heroes would never come again."* - Justice League Team

If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: Support server link - [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Justice League Team Synergy", url="https://discordapp.com")
            embed.set_footer(
                text=f"Last used by: {ctx.message.author.name} | Wanna find out who helped in moulding this bot into a successful one? Type i!credits to get the answer.")
            file = discord.File("./Images_Syn/jl.jpg", filename="jl.jpg")
            embed.set_image(url="attachment://jl.jpg")
            await ctx.channel.send(embed=embed, file=file)

        if cmd == 'bn':
            embed = discord.Embed(colour=discord.Colour(0x10e0a5),
                                  description="""The core of this team really revolves around Robin and Catwoman. Robin’s “Combo Kid “ passive keeps your combo meter up, which makes your abilities more effective. Catwoman’s “Blinding Strike “passive allows you to keep pressure on after using an ability by blinding the opponent to prevent attacks against your BN teammates. These passives in tandem create a well-balanced team.

Offensive-minded players will benefit from adding Batman to their third slot. Batman’s second special has a chance to utilize his third ability at no cost, which pairs well with Robin’s passives. As the latest member of the Batman Ninja team, Legendary Gorilla Grodd is also a great offensive option. His “Active Shield’ special will allow you reflect incoming damage back on your opponent. Grodd’s “Master Plan” passive rewards each BN teammate for landing a lethal attack with additional power bars as well.

For those who want to add staying power to their team, Ninja Lord Joker’s passive can revive up to two teammates against a team that has a Batman character. Gorilla Grodd’s “Dramatic Reversal” passive can feed into his “Mind Force” special ability which will share it’s healing effects among the whole team. Catwoman’s “9 Lives“ passive will allow for your BN team to become temporarily immortal at low health. All of these benefits can give you an edge in any prolonged fight.

Harley Quinn is unique in that just having her on your roster will provide a benefit to all of your BN characters! Even if she is not included on your team, your character will get a bonus to their attack and health.

*"And You Thought You Knew Every Batman Story..."* - Batman Ninja Team

If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: Support server link - [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Batman Ninja Team Synergy", url="https://discordapp.com")
            embed.set_footer(
                text=f"Last used by: {ctx.message.author.name} | Wanna find out who helped in moulding this bot into a successful one? Type i!credits to get the answer.")
            file = discord.File("./Images_Syn/bn.jpg", filename="bn.jpg")
            embed.set_image(url="attachment://bn.jpg")
            await ctx.channel.send(embed=embed, file=file)

        if cmd == 'loa':
            embed = discord.Embed(colour=discord.Colour(0x10e0a5),
                                  description="""One of this team’s strengths is damage-over-time (DoT), which makes them especially strong against teams with high defense and crit resist. They also control the fight by keeping opponents stunned, including being able to reflect stuns back at an opponent.

If The Joker is active and an opponent tags-in a teammate, which his special 3 can force them to do, there is a chance they will be stunned. The team has numerous abilities that can place a DoT on the opponent, which are boosted in strength from The Joker, as well as any basic attack thanks to Poison Ivy’s passive. With your opponent’s resistance to stun and DoT reduced from Harley Quinn, she and Ivy can truly wreak havoc. While active, Poison Ivy heals herself and her LOA teammates for a percent of DoT dealt.

*"Introduce a little anarchy, upset the established order and everything becomes... chaos..."* - League of Anarchy Team

If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: Support server link - [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="League of Anarchy Team Synergy", url="https://discordapp.com")
            embed.set_footer(
                text=f"Last used by: {ctx.message.author.name} | Wanna find out who helped in moulding this bot into a successful one? Type i!credits to get the answer.")
            file = discord.File("./Images_Syn/loa.jpg", filename="loa.jpg")
            embed.set_image(url="attachment://loa.jpg")
            await ctx.channel.send(embed=embed, file=file)

        if cmd == 'mv':
            embed = discord.Embed(colour=discord.Colour(0x10e0a5),
                                  description="""Green Arrow’s Power Drain has a chance to steal power from your enemy and give it to your team, which reduces being on the receiving end of your enemies’ offensive abilities. He is a popular pairing with White Canary, who can add to your equipment’s base critical attack chance and maybe even get you a zero power cost Electric Arrow ability use for Green Arrow.

Both versions of Supergirl have great support benefits which add a lot of longevity to an MV team through their defensive abilities:  Armored Supergirl gives her team an edge in battle by providing a starting amount of power and can provide critical attack immunity; while Multiverse Supergirl shores up her team’s defenses if they are moderately wounded.

Black Lightning can make things tough for opponents who have a tendency to use abilities far too often.

Batwoman’s increased special attack damage from each MV team buff paired with Captain Cold’s shield will ensure an aggressive, but safe, start to any fight for the team. She is another good candidate to team up with White Canary, who has the ability to make Batwoman’s Special 1 free, which, when used, provides Batwoman with a chance to perform a zero power cost Special 3. Bam! Domino effect!

The Flash provides great offensive benefits to his teammates and can be a great 3rd member on any Multiverse-centric team, allowing MV teammates to fire off their specials often.

*"There are all types of universe in the Multiverse, but never the same universe twice.."* - Mutliverse Team

If you have any ideas, suggestions or you faced a problem, you can join the support server by clicking this link: Support server link - [S. T. A. R. LABS Support](https://discord.gg/S7MvBVh4Hy).""")
            embed.set_author(name="Multiverse Team Synergy", url="https://discordapp.com")
            embed.set_footer(
                text=f"Last used by: {ctx.message.author.name} | Wanna find out who helped in moulding this bot into a successful one? Type i!credits to get the answer.")
            file = discord.File("./Images_Syn/mv.jpg", filename="mv.jpg")
            embed.set_image(url="attachment://mv.jpg")
            await ctx.channel.send(embed=embed, file=file)

    @syn.error
    async def syn_error(self, ctx, error):
        if isinstance(error, SynergyToggleError):
            embed = discord.Embed(colour=discord.Colour(0x2b8bf5),
                                  description="""Synergy commands are disabled! Ask a moderator or admin to do it.""")
            embed.set_author(name=choice(bruh), url="https://discordapp.com")
            embed.set_image(url=choice(gifs))
            await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(TeamSynergy(bot))
