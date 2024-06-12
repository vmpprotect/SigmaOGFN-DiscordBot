# (SigmaFN) -> Imports
import os
import discord
import datetime
import time
from discord.ext import commands
from colorama import Fore, Back, Style, init

# (SigmaFN) -> Settings/Configurable Options
init(autoreset=True)
prefix = "?"
bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())
token = "TOKEN_HERE"
show_debug_logs = False

# (SigmaFN) -> On Ready Event
@bot.event
async def on_ready():
    print_dbg("Bot is online and ready.")

# (SigmaFN) -> Show Debug Message
def print_dbg(title, text):
    current_time = datetime.datetime.now()
    minutes_seconds = current_time.strftime("%M:%S")
    print(f"{Fore.MAGENTA}[{Fore.WHITE}{minutes_seconds}{Fore.MAGENTA}] {Fore.MAGENTA}({Fore.WHITE}SigmaFN{Fore.MAGENTA}) {Fore.WHITE}-> {title} {Fore.MAGENTA}[{Fore.WHITE}{text}{Fore.MAGENTA}]{Fore.RESET}")

# (SigmaFN) -> On Message Received Event
@bot.event
async def on_message(message):
    print_dbg(f"Received message: {message.content}")
    await bot.process_commands(message)

# (SigmaFN) -> Inject BattleRoyale DLL Function
@bot.command()
async def battleroyale(ctx):
    await inject_game(ctx, "SigmaOGFN_BR.dll")

# (SigmaFN) -> Inject LateGame DLL Function
@bot.command()
async def lategame(ctx):
    await inject_game(ctx, "SigmaOGFN_LG.dll")

# (SigmaFN) -> Stop Game Function
@bot.command()
async def stopgame(ctx):
    game_processes = [
        "FortniteLauncher.exe",
        "FortniteClient-Win64-Shipping_BE.exe",
        "FortniteClient-Win64-Shipping.exe"
    ]
    for process in game_processes:
        os.system(f"taskkill /F /IM {process}")
    await ctx.send("Game processes stopped.") if show_debug_logs else print_dbg("Game processes stopped.")


# (SigmaFN) -> Bot Latency Function
@bot.command()
async def ping(ctx):
    latency = bot.latency
    await ctx.send(f"Latency: {latency * 1000:.2f}ms")

# (SigmaFN) -> Echo Text Function
@bot.command()
async def echo(ctx, *, content: str):
    await ctx.send(content)

# (SigmaFN) -> Inject DLL Function
async def inject_game(ctx, dll_name: str):
    try:
        os.system("start C:\\Users\\Administrator\\Desktop\\FortniteLauncher.exe")
        await ctx.send("Started FortniteLauncher.exe") if show_debug_logs else print_dbg("Started FortniteLauncher.exe")

        os.system("start C:\\Users\\Administrator\\Desktop\\FortniteClient-Win64-Shipping_BE.exe")
        await ctx.send("Started Fake BE Service.exe") if show_debug_logs else print_dbg("Started Fake BE Service.exe")

        os.system(
            "start C:\\Users\\Administrator\\Desktop\\14.60\\FortniteGame\\Binaries\\Win64\\FortniteClient-Win64-Shipping.exe "
            "-epicapp=Fortnite -epicenv=Prod -epiclocale=en-us -epicportal -skippatchcheck -nobe -fromfl=eac "
            "-fltoken=3db3ba5dcbd2e16703f3978d -caldera=eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9..."
            "-AUTH_LOGIN=Player664@projectreboot.dev -AUTH_PASSWORD=Rebooted -AUTH_TYPE=epic -nullrhi -nosplash -nosound"
        )
        await ctx.send("Started Fortnite, waiting for the game to load.") if show_debug_logs else print_dbg("Started Fortnite, waiting for the game to load.")
        await asyncio.sleep(30)

        dlls_to_inject = ["cobalt.dll", "memory.dll", dll_name, "console.dll"]
        for dll in dlls_to_inject:
            os.system(f"start C:\\Users\\Administrator\\Desktop\\inj.exe -n FortniteClient-Win64-Shipping.exe -i {dll}")
        await ctx.send("Injected DLLs. Waiting for the game to start.") if show_debug_logs else print_dbg("Injected DLLs. Waiting for the game to start.")
        await asyncio.sleep(45)
        await ctx.send("Game should be starting. Give it around 90 seconds.") if show_debug_logs else print_dbg("Game should be starting. Give it around 90 seconds.")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}") if show_debug_logs else print_dbg(f"An error occurred: {e}")

# (SigmaFN) -> Run Bot
if token:
    bot.run(token)
else:
    print_dbg("It was DNS 😭")
    
