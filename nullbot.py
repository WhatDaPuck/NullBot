#!/usr/bin/env python3
"""
discord bot in python for a friends server
"""
import logging
import asyncio
import discord
from discord.ext import commands

client = discord.Client()
logging.basicConfig(level=logging.INFO)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print()
    await client.change_presence(game=discord.Game(name='0x90'), status=None, afk=False)


@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'welcome {0.mention} to {1.name} , type `!null` to join us.'
    await client.send_message(client.get_channel("338387290936311819"), fmt.format(member, server))

@client.event
async def on_message(message):
    if message.content.startswith("!null"):
        role = discord.utils.get(message.server.roles, name="0xNULL")
        await client.add_roles(message.author, role)
        await client.change_nickname(message.author, "null")
        await client.send_message(message.channel, "welcome to null")
        await asyncio.sleep(5)
        async for msg in client.logs_from(message.channel):
            await client.delete_message(msg)
    elif message.content.startswith("^test"):
        await client.send_message(message.channel, "i'm working")

client.run(';)')