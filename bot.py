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
import pafy, ffmpeg, asyncio
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
def search(x):   
    url="https://www.youtube.com/results?search_query="+x
    p = requests.get(url)
    soup = BeautifulSoup(p.content,'html.parser')
    find=[]
    i=1
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        title = vid['title']
        # print(vid['href'])
        link = "https://www.youtube.com/results"+vid['href']
        data = title+';'+link
        # print (str(i)+": "+vid['title'])
    # print (type(vid['href']))
    # print(vid.find('a')['href'])
        find.append(data)
        if i == 5:
            break
        i+=1
    return find
# search("hanezeve caradhina")

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
"asshole",
"kntl"
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
flag = 1
user = ""
tmp = []
@client.event
async def on_message(message):
    global flag
    global user
    global tmp
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
        await message.channel.send('please don\'t send anything to avoid error\nConverting file...')
        video = pafy.new(x) 
        bestaudio = video.getbestaudio() 
        title = video.title
        title = ''.join(e for e in title if e.isalnum() or e == ' ' or e == '-'or e == '_'or e == '.')
        bestaudio.download(filepath=title+'.mp3')
        await message.channel.send(title+'.mp3 is being sent..')
        await message.channel.send(file=discord.File(title+'.mp3'))
        os.remove(title+'.mp3')
    if "/search" == message.content.lower()[:7]:
        title=[]
        link=[]
        x = message.content[8:]
        y = search(x)
        
        i = 1
        res = ''
        for z in y:
            title,link = z.split(';')
            res+='\n'+str(i)+". "+title+" ; "+link[-11:]
            i+=1
        await message.channel.send("here is what i\'ve found:"+res) 
   
    if '/help' == message.content.lower():
        gogogo='''```bot feature:
\'apakah\'
\'throw a dice\'
\'what is love?\'
\'nanti\'
teguran buat kata kata kasar
\'galau\'
\'random fact\'
\'/download\'+ 11 digit kode youtube / link youtube langsung juga bisa
\'/search\' + apa yg mau dicari (via youtube), buat dapet judul + 11 digit kode youtube
sekian, mungkin baru ini :)```'''

        await message.channel.send(gogogo)

    
    # if "//play" == message.content.lower()[:6]:
    #     if tmp:
    #         tmp = []
    #     x = message.content[7:]
    #     user = message.author
    #     print(str(user) +" "+ x)
    #     y = searchi(x)
    #     count = 1
    #     y1 = search(x)
    #     msg = user.mention+" here is what i've found:"
    #     # await message.channel.send(user.mention+" here is what i\'ve found:")
    #     for i in y1:
    #         tmp.append(i)
    #     for i in y:
    #         msg+='\n'+i
    #     print(msg)
    #     await message.channel.send(msg+"\nwhich number do you want to play?")
    #     flag = 0 
    # print(user)
    # if message.author == user and flag == 0 and message.content.isdigit():
        
    #     print (tmp)
    #     voice_channel = message.author.voice.channel
    #     # voice_channel = 
    #     channel=None
    #     # only play music if user is in a voice channel
    #     flag = 1
    #     if voice_channel!= None:
    #         x = tmp[int(message.content)]
    #         # await message.channel.send('your command is being proceed\nplease don\'t send anything...')
    #         video = pafy.new(x) 
    #         bestaudio = video.getbestaudio() 
    #         title = video.title
    #         title = ''.join(e for e in title if e.isalnum() or e == ' ' or e == '-'or e == '_')
    #         title = title +".mp3"
    #         bestaudio.download(filepath=title)
    #         # grab user's voice channel
    #         channel=voice_channel.name
    #         # await message.channel.send('User is in channel: '+ channel)
    #         # create StreamPlayer
    #         vc = await message.author.voice.channel.connect()
    #         # vc.play(discord.FFmpegPCMAudio(title))
    #         print(vc.play(discord.FFmpegPCMAudio(title)))
    #         # vc.is_playing()
    #         # vc.pause()
    #         # vc.resume()
    #         # vc.stop()
    #         while vc.is_playing():
    #             asyncio.sleep(1)
    #         # disconnect after the player has finished
            
    #         vc.stop()
    #         await vc.disconnect()
    #     else:
    #         await message.channel.send('User is not in a channel.')

# @client.command(
#     name='vuvuzela',
#     description='Plays an awful vuvuzela in the voice channel',
#     pass_context=True,
# )
# async def vuvuzela(context):
#     # grab the user who sent the command
#     user=context.message.author
#     voice_channel=user.voice.voice_channel
#     channel=None
#     # only play music if user is in a voice channel
#     if voice_channel!= None:
#         # grab user's voice channel
#         channel=voice_channel.name
#         await client.say('User is in channel: '+ channel)
#         # create StreamPlayer
#         vc= await client.join_voice_channel(voice_channel)
#         player = vc.create_ffmpeg_player('vuvuzela.mp3', after=lambda: print('done'))
#         player.start()
#         while not player.is_done():
#             await asyncio.sleep(1)
#         # disconnect after the player has finished
#         player.stop()
#         await vc.disconnect()
#     else:
#         await client.say('User is not in a channel.')
client.run(token)
