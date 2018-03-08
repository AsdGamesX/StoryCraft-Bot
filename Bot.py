import discord
import time
from discord.ext import commands

client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print('---------------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('---------------')

@client.command(pass_context=True)
async def ping(ctx):
	channel = ctx.message.channel
	t1 = time.perf_counter()
	await bot.send_typing(channel)
	t2 = time.perf_counter()
	embed=discord.Embed(title=None, description='Ping: {}'.format(round((t2-t1)*1000)), color=0x2874A6)
	await bot.say(embed=embed)

@client.event
async def on_message(message):
    if message.content.startswith('$help'):
        await client.send_message(message.channel,'help')
        await client.send_message(message.channel,'ping')
        await client.send_message(message.channel,'report')

client.run("NDE1MTYwOTg2NDE3MjMzOTIw.DXMhmw.DW1hRiuISLDkiD8R17jcH-lFF0Q")
