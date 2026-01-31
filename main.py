#!/bin/python3


import discord
import random
import os
from dotenv import load_dotenv
from discord.ext import commands

# constants - a list of all possible answers accurate to the game
responsesPositive = ["i guess so...", "i think it's fine...", "if you wanna...", "okay...", "s...sure...", "y..yeah...", "y-yeah, definitely!", "yes!"]
responsesNegative = ["    d-definitely not...","don't do it...","i think that's a bad idea...","nah...","no.","NO!!!!!!","no no no no no","n-nuh uh...","p...please don't..."]
responsesUncertain = [    "i dunno","if i say yes, will you take me with you?","i'm not comfortable answering that...","i'm... not sure...","maaaaaaaaybe","uh...uhhhhh...","you should ask your friends for help!"]
responsesIrrelevant = ["i miss my wife", "i am bingbong"]

# setup .env files to import Discord app credentials
load_dotenv()
discordBotToken = os.getenv("BOTTOKEN")
discordAppId = os.getenv("APPID")

#choose a response
def response():
	responseOptions = [responsesPositive,responsesNegative,responsesUncertain,responsesIrrelevant,responsesIrrelevant]
	responseType = random.choice(responseOptions)
	response = random.choice(responseType)
	print(response)
	return response

#initialise discord bot
intents = discord.Intents.default()
intents.message_content = True
bingBongBot = commands.Bot(command_prefix="",intents=intents)

@bingBongBot.event
async def on_ready():
	print("y-yeah, definitely! I'm ready to rumble!")


#runs on ping
@bingBongBot.event
async def on_message(message):
	if f"<@{discordAppId}>" in message.content:
		await message.channel.send(response())


bingBongBot.run(discordBotToken)