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

#initialise discord bot
intents = discord.Intents.default()
intents.message_content = True
bingBongBot = commands.Bot(intents=intents)

@bingBongBot.event
async def on_ready():
	print("logged in successfully")
bingBongBot.run(discordBotToken)
