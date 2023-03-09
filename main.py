import discord
from discord.ext import commands
from discord import app_commands
import Iresponses

async def send_message(message, user_message, is_private):
    try:
        responses = Iresponses.handle_response(user_message)
        await message.author.send(responses) if is_private else await message.channel.send(responses)
    except Exception as e:
        print(e)


TOKEN =  'DeezLigma1234'
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents = intents)

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
    
@client.event
async def on_ready():
    print(f'{client.user} is now running')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
        
    print(f"{username} said:'{user_message}'({channel})")
        
    if user_message[0] == '?':
        user_message = user_message[1:]
        await send_message(message, user_message, is_private=True)
    else:
        await send_message(message, user_message, is_private=False)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member, *, reason=None):
    if reason == None:
        reason="L bozo"
    await ctx.guild.kick(member)
    await ctx.send(f"User {member.mention} has been sent to touch grass for {reason}")
client.run(TOKEN)
