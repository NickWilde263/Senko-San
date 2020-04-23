# Work with Python 3.6
import os
import discord
from discord.ext import commands, timers

TOKEN = 'made you look'

bot = commands.Bot(command_prefix = "s$")
bot.remove_command('help')


  
#SERIOUS GUILD COMMANDS

bot.serious_guilds = []

@bot.command(name='guildIsSerious')
async def guildIsSerious(ctx):
    if not(ctx.guild.id in bot.serious_guilds):
        bot.serious_guilds.append(ctx.guild.id)
        await ctx.send("I will behave in this server.")
    else:
        await ctx.send("Guild is already serious!")

@bot.command(name='guildIsNotSerious')
async def guildIsNotSerious(ctx):
    if ctx.guild.id in bot.serious_guilds:
        bot.serious_guilds.remove(ctx.guild.id)
        await ctx.send("Tehehe")
    else:
        await ctx.send("This server is already not a serious server!")

@bot.command(name='getSeriousGuilds')
async def getSeriousGuilds(ctx):
    await ctx.send(bot.serious_guilds)

#CENSORED GUILD COMMANDS

bot.censored_guilds = []

@bot.command(name='guildIsCensored')
async def guildIsCensored(ctx):
    if not(ctx.guild.id in bot.censored_guilds):
        bot.censored_guilds.append(ctx.guild.id)
        await ctx.send("I will censor this server.")
    else:
        await ctx.send("Guild is already censored!")

@bot.command(name='guildIsNotCensored')
async def guildIsNotCensored(ctx):
    if ctx.guild.id in bot.censored_guilds:
        bot.censored_guilds.remove(ctx.guild.id)
        await ctx.send("Tehehe")
    else:
        await ctx.send("This server is already not censored!")

@bot.command(name='getCensoredGuilds')
async def getCensoredGuilds(ctx):
    await ctx.send(bot.censored_guilds)

#BRUH DETECTOR COMMANDS

bot.bruh_guilds = []

@bot.command(name='guildIsBruh')
async def guildIsBruh(ctx):
    if not(ctx.guild.id in bot.bruh_guilds):
        bot.bruh_guilds.append(ctx.guild.id)
        await ctx.send("I will not detect bruh moments in this server.")
    else:
        await ctx.send("Guild already does not detect bruh moments!")

@bot.command(name='guildIsNotBruh')
async def guildIsNotBruh(ctx):
    if ctx.guild.id in bot.serious_Bruh:
        bot.bruh_guilds.remove(ctx.guild.id)
        await ctx.send("Tehehe")
    else:
        await ctx.send("I already do not detect bruh moments on this server!")

@bot.command(name='getBruhGuilds')
async def getBruhGuilds(ctx):
    await ctx.send(bot.bruh_guilds)

#COMMANDS

@bot.command(name='hello')
async def hello(ctx):
    await ctx.channel.send("Hello there, {0}".format(ctx.author.mention))

@bot.command(name='spank')
async def spank(ctx):
    serious = False
    if ctx.guild.id in bot.serious_guilds:
        serious = True
    if not serious:
        await ctx.channel.send("Uhnnn, why would you spank me, Master? Did I do anything wrong?")

@bot.command(name='pat')
async def pat(ctx):
    patGIF = discord.File("C:\\Users\\AYOUB\\Pictures\\sPAT.gif")
    await ctx.channel.send(file=patGIF)

bot.the_hated = []
@bot.command(name='hate')
async def hate(ctx, person:discord.Member):
    serious = False
    if ctx.guild.id in bot.serious_guilds:
        serious = True
    if not serious:
        bot.the_hated.append(person)
        await ctx.send("Added!")
    else:
        pass
    

@bot.command(name='hate_remove')
async def hate_remove(ctx, person:discord.Member):
    serious = False
    if ctx.guild.id in bot.serious_guilds:
        serious = True
    if not serious:
        for hPerson in bot.the_hated:
            if person in bot.the_hated:
                bot.the_hated.remove(person)
                await ctx.send("Removed!")
                return
            else: 
                await ctx.channel.send("That person isn't hated (yet...)")
    else:
        pass

@bot.command(name='hate_list')
async def hate_list(ctx):
    serious = False
    if ctx.guild.id in bot.serious_guilds:
        serious = True
    if not serious:
        await ctx.send(bot.the_hated)
    else:
        pass

bot.number = 691010171828437025
@bot.command(name='love')
async def love(ctx, *, personM:discord.Member):
    serious = False
    if ctx.guild.id in bot.serious_guilds:
        serious = True
    if not serious:

        for register in bot.the_hated:
            if personM in bot.the_hated:
                loveGIF = discord.File("C:\\Users\\AYOUB\\Pictures\\sMAD.gif")
                await ctx.channel.send(f"Shut the fuck up, {personM.mention} does not deserve love", file=loveGIF)
                return

        if personM.id == bot.number:
            loveGIF = discord.File("C:\\Users\\AYOUB\\Pictures\\sLove.gif")
            await ctx.channel.send(f"I love you too, {ctx.author.mention}", file=loveGIF)

        elif personM.id == ctx.author.id:
            loveGIF == discord.File("C:\\Users\\AYOUB\\Pictures\\senkoLove.gif")
            await ctx.channel.send(f"You must love yourself a lot, {personM.mention}", file=loveGIF)

        else:
            loveGIF = discord.File("C:\\Users\\AYOUB\\Pictures\\senkoLove.gif")
            await ctx.channel.send(f"{ctx.author.mention} loves you, {personM.mention}", file=loveGIF)
    else:
        pass

    
#HELP
        
@bot.command(name='help')
async def help(ctx):
    gold = discord.Colour.gold()
    helper = discord.Embed(title='Senko-san', description='wh-what would you like to do with me uwu\n', colour=gold)
    commands = {}
    #Command help
    commands['s$hello'] = "Returns a greeting and mention"
    commands['s$remind <game> <day> <time>'] = "Sets a reminder for a game"
    commands['s$love <user>'] = "Send some love to another user"
    commands['s$hate <user>'] = "Add a user to the hate list"
    commands['s$hate_remove <user>'] = "Remove a user from the hate list"
    commands['s$pat'] = "Pat Senko"

    #Passive help
    commands['Passive: "Bruh Detector"'] = "Detects bruh moments"
    commands['Passive: "DadBot"'] = "It's our dad"
    commands['Passive: "Censor"'] = "Censors bad words"

    for command, description in commands.items():
        helper.add_field(name=command,value=(description + "\n"), inline=False)
    await ctx.channel.send(embed = helper)

#ON_MESSAGE COMMANDS

@bot.event
async def on_message(message): 
    if message.author == bot.user:
        return
        #so the bot doesn't respond to itself
    bad_words = {}
    bad_words[0] = "fuck"
    bad_words[1] = "faggot"
    bad_words[2] = "nigger"
    bad_words[3] = "shit"

    censor = False
    if message.guild.id in bot.censored_guilds:
        censor = True
    if censor:
        for word in bad_words:
            if bad_words[word] in message.content.lower():
                await message.delete()
                await message.channel.send("That's really funny bud.")
    if message.content.lower().startswith("k$"):
        await message.channel.send("My master changed the command prefix used to summon me. Try typing 's$' before your command!")
        #for updated command
    bruh = False
    if message.guild.id in bot.bruh_guilds:
        bruh = True
    if not bruh:
        if  "bruh" in message.content.lower():
            bruhImg=discord.File('C:\\Users\\AYOUB\\Pictures\\bruh.jpg')
            await message.channel.send(f"That's quite a bruh moment {message.author.mention}!", file=bruhImg)
            #bruh detector, sends msg and file

    serious = False
    if message.guild.id in bot.serious_guilds:
        serious = True
    if not serious:
            if ("i'm" in message.content.lower()) or ("i’m" in message.content.lower() or ("im" in message.content.lower())):
                msg = message.content
                if "i’m" in msg.lower():
                    if not("i’m" in msg):
                    #if it has a capital somewhere in "i'm" which would prevent the bot
                    #from replacing the "i'm"
                        if "I’m" in msg:
                            msg = msg.replace("I’m", "i’m")
                        if "I’M" in msg:
                            msg = msg.replace("I’M", "i’m")
                        if "i’M" in msg:
                            msg = msg.replace("i’M", "i’m")
                    msg = msg[(msg.index("i’m")):]
                    msg = msg.replace("i’m", "")
                    await message.channel.send("Hi{0}, I'm dad!".format(msg))
                elif "i'm" in msg.lower():
                    if not("i'm" in msg):
                        if "I'm" in msg:
                            msg = msg.replace("I'm", "i'm")
                        if "I'M" in msg:
                            msg = msg.replace("I'M", "i'm")
                        if "i'M" in msg:
                            msg = msg.replace("i'M", "i'm")
                    msg = msg[(msg.index("i'm")):]
                    msg = msg.replace("i'm", "")
                    await message.channel.send("Hi{0}, I'm dad!".format(msg))
                elif (" im " in msg.lower())  or (msg.lower().startswith("im ")):
                    if (not ("im" in msg)) or (not (msg.startswith("im"))):
                        if "Im" in msg:
                            msg = msg.replace("Im", "im")
                        if "IM" in msg:
                            msg = msg.replace("IM", "im")
                        if "iM" in msg:
                            msg = msg.replace("iM", "im")
                        if msg.startswith("Im"):
                            msg = "im" + msg[1:]
                        if msg.startswith("iM"):
                            msg = "im" + msg[1:]
                        if msg.startswith("IM"):
                            msg = "im" + msg[1:]
                    msg = msg[(msg.index("im")):]
                    msg = msg.replace("im", "")
                    await message.channel.send("Hi{0}, I'm dad!".format(msg))
    else:
        pass
    await bot.process_commands(message)

@bot.event
async def on_ready():
    print('\nLogged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(TOKEN)
