import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
  
Client = discord.Client()
bot_prefix= "/"
client = commands.Bot(command_prefix=bot_prefix)
  
@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    #Extra 1
    await client.change_presence(game=discord.Game(name='/help'))
  
@client.command(pass_context=True)
async def rules(ctx):
    await client.say("""RULES:
1. Be respectful - Be respectful to everyone in this discord. 
2. No NSFW - PG13, people of all ages run servers. (Mature Content Filter: ALL)
3. No trolling - Acting stupid, trashy posts missbehaving will be seen as such. 
4. No spam - We don't spam you, so don't spam. 
5. Clean usernames - Keep your name clean and respectful. 
6. No illegal material 
7. No piracy links of any kind. 
8. No bots allowed - Only our bots. Any unauthorised bots will be banned. 
9. No ban evading - Just move on. 
10. No selling - This isn't a marketplace. Find somewhere else. 
11. No impersonation - No matter who you are trying to impersonate, don't do it. 
12. Minimal advertising - Keep it in #ads (Post only ONE advertisement - Not for chatter)
13. Private Information - DO NOT share client information or MultiCraft logins here. Keep that for support tickets.
14. Griefing and or stealing items from other RB members will lead to an immediate expulsion from every RB island!
15. Obey all staff! They're the law in the RB community.""")
#command1
@client.command(pass_context = True)
async def invite(ctx):
    x = await client.invites_from(ctx.message.server)
    x = ["<" + y.url + ">" for y in x]
    print(x)
    embed = discord.Embed(title = "Invite Links", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)
  
#command2
@client.command(pass_context = True)
async def getbans(ctx):
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of Banned Members", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)
  
#command3
@client.command(pass_context=True)
async def connect(ctx):
    if client.is_voice_connected(ctx.message.server):
        return await client.say("I am already connected to a voice channel. Do not disconnect me if I am in use!")
    author = ctx.message.author
    voice_channel = author.voice_channel
    vc = await client.join_voice_channel(voice_channel)
  
#command4
@client.command(pass_context = True)
async def disconnect(ctx):
    for x in client.voice_clients:
        if(x.server == ctx.message.server):
            return await x.disconnect()
  
#command5
@client.command(pass_context=True)       
async def clear(ctx, number):
    mgs = []
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)
 
#command6
@client.command(pass_context = True)
async def ban(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.administrator:
        return
 
    if not member:
        return await client.say(ctx.message.author.mention + "Specify a user to ban!")
    try:
        await client.ban(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            return await client.say(":x: Privilege too low!")
 
    embed = discord.Embed(description = "**%s** has been banned!"%member.name, color = 0xFF0000)
    return await client.say(embed = embed)
 
#command7
@client.command(pass_context = True)
async def kick(ctx, *, member : discord.Member = None):
    if not ctx.message.author.server_permissions.administrator:
        return
 
    if not member:
        return await client.say(ctx.message.author.mention + "Specify a user to kick!")
    try:
        await client.kick(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            return await client.say(":x: Privilege too low!")
 
    embed = discord.Embed(description = "**%s** has been kicked!"%member.name, color = 0xFF0000)
    return await client.say(embed = embed)
 
#command8
@client.command(pass_context = True)
async def listservers(ctx):
    x = '\n'.join([str(server) for server in client.servers])
    print(x)
    embed = discord.Embed(title = "Servers", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)
 
#command9
@client.command(pass_context = True)
async def info(ctx):
    await client.say("""**Useful Links:**
Discord Invite: https://discord.gg/p72sjBG
 
Roles:
@Owner - Official FV Founders
@Admin  - Offical FV Staff


client.run("NDkwNTc3NTM2Njg2NzUxODA0.Dn7V8g.OoglKRzOGxLfnyWGZAFs82OyZ-I")
