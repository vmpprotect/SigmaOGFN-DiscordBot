import os 
import discord #pip install discord
import time
import threading
from discord.ext import commands

prefix = "?"
bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())
# token = "the black kid from southpark or wtv"

@bot.event
async def on_ready():
    print("tunnin")


@bot.event
async def on_message(message):
    print("The message's content was", message.content)
    await bot.process_commands(message)


@bot.command()
async def battleroyale(ctx):
    await inject_br(ctx)

@bot.command()
async def lategame(ctx):
    await inject_lg(ctx)

@bot.command()
async def stopgame(ctx):
    await stopgameonfoenem(ctx)

@bot.command()
async def ping(ctx):
    latency = bot.latency
    await ctx.send(latency)

@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)

async def stopgameonfoenem(ctx):
    os.system("taskkill /F /IM FortniteLauncher.exe")
    os.system("taskkill /F /IM FortniteClient-Win64-Shipping_BE.exe")
    os.system("taskkill /F /IM FortniteClient-Win64-Shipping.exe")
    await ctx.send("Stopped Game.")

async def inject_br(ctx):
    os.system("start C:\\Users\\Administrator\\Desktop\\FortniteLauncher.exe")
    await ctx.send("Started FortniteLauncher.exe")
    os.system("start C:\\Users\\Administrator\\Desktop\\FortniteClient-Win64-Shipping_BE.exe")
    await ctx.send("Started Fake BE Service.exe")
    os.system("start C:\\Users\\Administrator\\Desktop\\14.60\\FortniteGame\\Binaries\\Win64\\FortniteClient-Win64-Shipping.exe -epicapp=Fortnite -epicenv=Prod -epiclocale=en-us -epicportal -skippatchcheck -nobe -fromfl=eac -fltoken=3db3ba5dcbd2e16703f3978d -caldera=eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50X2lkIjoiYmU5ZGE1YzJmYmVhNDQwN2IyZjQwZWJhYWQ4NTlhZDQiLCJnZW5lcmF0ZWQiOjE2Mzg3MTcyNzgsImNhbGRlcmFHdWlkIjoiMzgxMGI4NjMtMmE2NS00NDU3LTliNTgtNGRhYjNiNDgyYTg2IiwiYWNQcm92aWRlciI6IkVhc3lBbnRpQ2hlYXQiLCJub3RlcyI6IiIsImZhbGxiYWNrIjpmYWxzZX0.VAWQB67RTxhiWOxx7DBjnzDnXyyEnX7OljJm-j2d88G_WgwQ9wrE6lwMEHZHjBd1ISJdUO1UVUqkfLdU5nofBQ -AUTH_LOGIN=Player664@projectreboot.dev -AUTH_PASSWORD=Rebooted -AUTH_TYPE=epic -nullrhi -nosplash -nosound")
    await ctx.send("Started Fortnite, waiting a minute until game is fully loaded.")
    time.sleep(30)
    os.system("start C:\\Users\\Administrator\\Desktop\\inj.exe -n FortniteClient-Win64-Shipping.exe -i cobalt.dll")
    os.system("start C:\\Users\\Administrator\\Desktop\\inj.exe -n FortniteClient-Win64-Shipping.exe -i memory.dll")
    time.sleep(45)
    os.system("start C:\\Users\\Administrator\\Desktop\\inj.exe -n FortniteClient-Win64-Shipping.exe -i SigmaOGFN_BR.dll")
    os.system("start C:\\Users\\Administrator\\Desktop\\inj.exe -n FortniteClient-Win64-Shipping.exe -i console.dll")
    await ctx.send("Started game. Give it around 90~ seconds to start battle bus")

async def inject_lg(ctx):
    os.system("start C:\\Users\\Administrator\\Desktop\\FortniteLauncher.exe")
    await ctx.send("Started FortniteLauncher.exe")
    os.system("start C:\\Users\\Administrator\\Desktop\\FortniteClient-Win64-Shipping_BE.exe")
    await ctx.send("Started Fake BE Service.exe")
    os.system("start C:\\Users\\Administrator\\Desktop\\14.60\\FortniteGame\\Binaries\\Win64\\FortniteClient-Win64-Shipping.exe -epicapp=Fortnite -epicenv=Prod -epiclocale=en-us -epicportal -skippatchcheck -nobe -fromfl=eac -fltoken=3db3ba5dcbd2e16703f3978d -caldera=eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50X2lkIjoiYmU5ZGE1YzJmYmVhNDQwN2IyZjQwZWJhYWQ4NTlhZDQiLCJnZW5lcmF0ZWQiOjE2Mzg3MTcyNzgsImNhbGRlcmFHdWlkIjoiMzgxMGI4NjMtMmE2NS00NDU3LTliNTgtNGRhYjNiNDgyYTg2IiwiYWNQcm92aWRlciI6IkVhc3lBbnRpQ2hlYXQiLCJub3RlcyI6IiIsImZhbGxiYWNrIjpmYWxzZX0.VAWQB67RTxhiWOxx7DBjnzDnXyyEnX7OljJm-j2d88G_WgwQ9wrE6lwMEHZHjBd1ISJdUO1UVUqkfLdU5nofBQ -AUTH_LOGIN=Player664@projectreboot.dev -AUTH_PASSWORD=Rebooted -AUTH_TYPE=epic -nullrhi -nosplash -nosound")
    await ctx.send("Started Fortnite, waiting a minute until game is fully loaded.")
    time.sleep(30)
    os.system("start C:\\Users\\Administrator\\Desktop\\inj.exe -n FortniteClient-Win64-Shipping.exe -i cobalt.dll")
    os.system("start C:\\Users\\Administrator\\Desktop\\inj.exe -n FortniteClient-Win64-Shipping.exe -i memory.dll")
    time.sleep(45)
    os.system("start C:\\Users\\Administrator\\Desktop\\inj.exe -n FortniteClient-Win64-Shipping.exe -i SigmaOGFN_LG.dll")
    os.system("start C:\\Users\\Administrator\\Desktop\\inj.exe -n FortniteClient-Win64-Shipping.exe -i console.dll")
    await ctx.send("Started game. Give it around 90~ seconds to start battle bus")

bot.run(token) 
