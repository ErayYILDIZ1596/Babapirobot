import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix=">>", intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} olarak giriş yapıldı!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(client.command_prefix):
        await client.process_commands(message)
    else:
        await message.channel.send(message.content)

@client.command()
async def command1(ctx):
    await ctx.send("command confirmed!")

client.run("token")
