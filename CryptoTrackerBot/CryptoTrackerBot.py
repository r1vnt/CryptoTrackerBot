from http.client import responses
import discord
import json
import requests
import time

from discord.ext import commands
from discord import Intents

key = "https://api.binance.com/api/v3/ticker/price?symbol="
USDT = "USDT"
isworth = "is worth $"
token = "MTA2OTU5MTI0NDQwNzMxMjQ4NA.Gb7YTI.j09h_LGTxARfC-09yxcEPa1ZTWk5tIFRYclPzU"

client = commands.Bot(command_prefix = '>', intents=Intents.all())

@client.event
async def on_ready():
    print("Bot Connected")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = "the Market"))

@client.command()
async def Convert(ctx, coin1, coin2):
    if coin2 == "USD":
        url = key + coin1 + "USDT"
        data = requests.get(url)
        data = data.json()
        message = coin1 + " is worth " + coin2 + data['price']
        await ctx.send(message)
    else:
        url = key + coin1 + coin2
        data = requests.get(url)
        data = data.json()
        message = coin1 + " is worth " + coin2 + data['price']
        await ctx.send(message)

    print("Command Sent")

@client.command()
async def ConvertAmount(ctx, amount, coin1, coin2):
    if coin2 == "USD":
        url = key + coin1 + "USDT"
        data = requests.get(url)
        data = data.json()
        total = float(amount) * float(data['price'])
        message = amount + " " + coin1 + " is worth " + coin2 + " " + str(total)
        await ctx.send(message)
    else:
        url = key + coin1 + coin2
        data = requests.get(url)
        data = data.json()
        message = amount + " " + coin1 + " is worth " + coin2 + " " + total        
        print(message)
        await ctx.send(message)

@client.command()
async def CryptoToCrypto(ctx, coin1, coin2):
     url = key + coin1 + "USDT"
     data = requests.get(url)
     data = data.json()
     coin1val = float(data['price'])
     url = key + coin2 + "USDT"
     data = requests.get(url)
     data = data.json()
     coin2val = float(data['price'])
     conversion = coin1val / coin2val
     message = "1" + coin1 + " is worth " + coin2 + str(conversion)
     await ctx.send(message)

@client.command()
async def AmountCryptoToCrypto(ctx, Amount, coin1, coin2):
     url = key + coin1 + "USDT"
     data = requests.get(url)
     data = data.json()
     coin1val = float(data['price'])
     url = key + coin2 + "USDT"
     data = requests.get(url)
     data = data.json()
     coin2val = float(data['price'])
     conversion = (coin1val / coin2val) * float(Amount)
     message = Amount + coin1 + " is worth " + coin2 + str(conversion)
     await ctx.send(message)


client.run(token)