# This example requires the 'message_content' intent.
import config

import discord

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.event
async def on_member_join(member):
    channel = client.get_channel(1073167438042120204)
    await channel.send("Welcome " + member.name)

client.run(config.TOKEN)
