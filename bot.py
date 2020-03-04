# bot.py
import os
import random
from random import randint
import discord
from dotenv import load_dotenv
from time import sleep
from threading import Thread
import requests
from bs4 import BeautifulSoup
import pafy
#scrap
url="https://karyapemuda.com/kata-kata-galau/"
p = requests.get(url)
soup = BeautifulSoup(p.content,'html.parser')
x = soup.findAll('p',style='text-align: center;')
def scrap():
    url='http://randomfactgenerator.net/' # web simple buat latihan, bisa dibuka
    p = requests.get(url)
    soup = BeautifulSoup(p.content,'html.parser')
    x = soup.findAll('div',id='z')
    y=randint(0,2)
    return list(x)[y].text[:-6]
def quotes():
    global x
    y = randint(0,426)
    y = list(x)[y].text[1:-1]
    y = "kata kata galau : \n"+y
    return y
    


cursed = [
"kontol",
"asu",
"asu",
"bego",
"goblok",
"anjing",
"anjeng",
"tolol",
"bajingan",
"kampret",
"babi",
"bangke",
"ngentot",
"memek",
"jembut",
"bangsat",
"setan",
"keparat",
"berengsek",
"brengsek",
"keparat",
"bgst",
"fuck",
"dick",
"bitch",
"ngewe",
"pler",
"meki",
"peler",
"kimak",
"setan",
"tetek",
"toket",
"boobs",
"fuck",
"bitch",
"anal",
"pepek",
"cipet",
"asshole"
]
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, selamat datang pler'
    )
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    if "apakah" in message.content[:6].lower():
        rand = randint(1,2)
        if(rand==1):
            await message.channel.send("iya")
        else:
            await message.channel.send("engga")
    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
    if message.content == 'halo neckbottle':
        await message.channel.send("halo juga :3")
    if 'nanti' in message.content:
        await message.channel.send("nanti mulu terus kapan pler?")
    if message.content.lower() == 'throw a dice':
        rand = randint(1,6)
        hasil = 'Nilai dadu yang dilempar : '+str(rand)
        await message.channel.send(hasil)
    for curse in cursed:
        if curse in message.content.lower():
            await message.channel.send(message.author.mention+" tolong dong omongan dijaga -.-\"")
    if message.content.lower()=='what is love?':
        await message.channel.send('baby don\'t hurt me')
        sleep(1)
        await message.channel.send('don\'t hurt me')
        sleep(1)
        await message.channel.send('no more')
        sleep(1)
        await message.channel.send('<3')
    #random fact
    if message.content.lower()=="random fact":
        await message.channel.send(scrap())
    if"galau" in message.content.lower():
        await message.channel.send(quotes())
    if "wow" in message.content.lower():
        await message.channel.send(file=discord.File('Harris,lick.gif'))
    if "/download" == message.content.lower()[:9]:
        x =message.content.split(' ')
        x = x[1]
        print(x)
        await message.channel.send('your command is being proceed\nplease don\'t send anything...')
        video = pafy.new(x) 
        
        bestaudio = video.getbestaudio() 
        bestaudio.download(filepath=video.title+'.mp3')
        os.system("cls")
        print(video.title)
        await message.channel.send(video.title+'.mp3 is being sent..')
        await message.channel.send(file=discord.File(video.title+'.mp3'))
        os.remove(video.title+'.mp3')


client.run(token)