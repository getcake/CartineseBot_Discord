#!/usr/bin/python3

import discord
from cartify import translate

TOKEN = 'replace_with_yours'

client = discord.Client()

#Storage optmized for multiple servers
isCarti = {} #stores cartify mode by server
prev_msg = {} #stores previous message

help_message = "```----------ok !*+ HELP* *+_slatt! ----------```\Cartify previous messages with\n```!carti```\Cartiy all messages with\n```!cartify```\nand turn off with\n```!nocarti```"


@client.event
async def on_message(message):
    global prev_msg
    global isCarti

    with open('test.txt', 'r') as cartinese:
        
        if message.author == client.user:
            return
        if message.content.startswith('!help'):
            await message.channel.send(help_message) 
        #Disable 
        elif message.content.startswith('!nocarti'):
            isCarti[hash(message.guild)] = False
            await message.channel.send('damn bro :( *+slatt')
        if message.content.startswith('!cartify'):
            isCarti[hash(message.guild)] = True
            await message.channel.send('[Translating all messages] Use !nocarti to disable')
        elif hash(message.guild) in isCarti and isCarti[hash(message.guild)]:
            await message.delete()
            translate(message.content)
            messageFinal = cartinese.read()
            await message.channel.send(message.author.name + ':\n> ' + messageFinal)
        #cartify prev message
        elif message.content.startswith('!carti'):
            if hash(message.guild) not in prev_msg:
                await message.channel.send('Nothing !*+ to :( cartify!')
            else:
                carti_message = translate(prev_msg[hash(message.guild)])
                carti_message = cartinese.read()
                await message.channel.send(carti_message)
        else:
            prev_msg[hash(message.guild)] = message.content


@client.event
async def on_ready():
    print('CODEINE')

client.run(TOKEN)
