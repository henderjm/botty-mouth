# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
import os

TOKEN = os.environ['TOKEN']
BUZZWORD = '!gravestone'
GRAVESTONES = {'rory': '/Users/henderjm/Desktop/rory.png',
        'ois': '/Users/henderjm/Desktop/alois.png',
        'alois': '/Users/henderjm/Desktop/alois.png',
        'les': '/Users/henderjm/Desktop/les.png',
        }

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!gravestone'):
        user = message.content.split(BUZZWORD)[1]
        print(user)
        if user in GRAVESTONES:
            await client.send_file(message.channel, GRAVESTONES[user])
        else:
            await client.send_message(message.channel, "Sorry, I can't rep {} right now".format(user))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)

