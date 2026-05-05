import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True  # needed for prefix commands

bot = commands.Bot(command_prefix="!", intents=intents)

# Bot ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# 1️⃣ Test command (loop example)
@bot.command()
async def test(ctx):
    for i in range(5):
        await ctx.send(f"Test message {i+1}")
        await asyncio.sleep(0.5)

# 2️⃣ Say command (bot repeats your message)
@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)

# 3️⃣ Create channel command
@bot.command()
@commands.has_permissions(manage_channels=True)
async def createchannel(ctx, name):
    guild = ctx.guild
    await guild.create_text_channel(name)
    await ctx.send(f"Channel `{name}` created!")

# Error handling (for permissions)
@createchannel.error
async def createchannel_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to do that!")

# Run bot
bot.run("YOUR_BOT_TOKEN")
