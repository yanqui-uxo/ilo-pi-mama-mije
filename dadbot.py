import discord
import re

client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    match = re.search(r"(\s|^)mi ([\w\s]+)", message.content)
    if match:
        await message.channel.send(f"toki, {match.group(2)} o! mi mama mije.")

with open("token.txt") as f:
    token = f.read()
client.run(token)