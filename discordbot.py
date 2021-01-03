import os
import random 
import discord
import youtube_dl
from dotenv import load_dotenv 
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('Discord_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
clientt = commands.Bot(command_prefix = '!')
players ={}


client = discord.Client()



@client.event # console event welcoming jojo bot 
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
      

@client.event #joining the server 
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to  Undercover server fellow agent! and fuck you'

    )

       
@client.event # reseponding to messages
async def on_message(message):
    if message.author == client.user:  #client user is bot user 
        return 

    #badwordquote = ['WTF no fucken bad words please here ']


    #Bot Dictionary
    smamozquote = ['Jojo loves moza']
    holmesquote = ['Jojo loves Holmes']
    khokhaquote = ['Jojo loves Khokha']
    Aymanquote = ['Jojo loves Vader']
    ahmedquote = ['Jojo loves whodis']
    seifqoute = ['Jojo loves Semsem']
    badwordsList = ["shit","fuck","bitch","7omar","5awal","a7a","3ars","gay","shaz","metnak","5ara","beed","bedan"]
    greetings = ["how are you" , "how are u" , "are you ok"]
    intimate = ["I love you" , " I hate you" , " Ba7bak" , "bahebak" , "ba7bak"]
    

    if 'moza' in message.content or 'Moza' in message.content or 'Smamoz' in message.content or 'smamoz' in message.content or 'moez' in message.content:
        response = random.choice(smamozquote)
        await message.channel.send(response)

    if 'holmes' in message.content or 'Holmes' in message.content or 'John' in message.content or 'john' in message.content or 'monti' in message.content:
        response = random.choice(holmesquote)
        await message.channel.send(response)
        
    if 'khokha' in  message.content or 'Khokha' in message.content or 'khaled' in message.content or 'Khaled' in message.content:
        response = random.choice(khokhaquote)
        await message.channel.send(response)

    if 'ayman' in message.content or 'Ayman' in message.content or 'Vader' in message.content or 'vader' in message.content:
        response = random.choice(Aymanquote)
        await message.channel.send(response)

    
    if 'ahmed' in message.content or 'Ahmed' in message.content or 'whodis' in message.content or 'Whodis' in message.content:
        response = random.choice(ahmedquote)
        await message.channel.send(response)
    
    if 'seif' in  message.content or 'Seif' in message.content or 'semsem' in message.content or 'Semsem' in  message.content:
         response = random.choice(seifqoute)
         await message.channel.send(response)

    for words in badwordsList:
        if words in message.content:
            #response = random.choice("eh ya3am el kalam el 5ara da")
            await message.channel.send('5ara 3alek ya ' + f'{message.author.name} ' + 'matbatal te2ol el alfaz el wes5a di' ) 

    
    #chatting with the Jojo
    
    
    if   'hi Jojo' in message.content or 'Hi Jojo' in message.content or 'hi jojo' in message.content or 'jojo' in message.content:
        await message.channel.send (f'Hi {message.author.name}') 
        #await message.channel.send ('Type Jojo in every phrase u send to me so that I can comprehend that you are speaking directly to me alone :D')
    
    if 'Tondela' in message.content:
        await message.channel.send ('Tondela is the best team in the world, had the best manager Georginio and fuck u all softy teams')
    
    if 'PDF' in message.content:
        await message.channel.send ('Tondela had best partner PDF and its word doc')
     
    if 'Bolognese' in message.content or 'Bolonese' in message.content:
        await message.channel.send ('Tondela wants to eat Spaghetti Bolognese')

    for words in greetings:
        if words in message.content:
             await message.channel.send ('I am fine, u?')
    
    for words in intimate:
        if words in message.content:
            await message.channel.send("I love you")
    
   

    

    #if 'Ok Jojo' in message.content or 'ok Jojo' in message.content or 'okay Jojo' in message.content or 'ok jojo' in message.content:
     #  await message.channel.send (f'OK {message.author.name}') 

  #music 
    #while True:
        #if "whodis" in message.author.name:
            #await message.channel.send("Fuck u whodis")
    
  
    #while True:
        #if message.author.name == "Smamoz":
            #await message.channel.send("fuck you ya moez ya 5awallllllllllllllllllll")
    
    
    
    
    
    
    
    #thankmoza = ['Thanks Moza appreciate it you sexy banana sonic boy']
    #await message.channel.send(thankmoza)





#commands





    


#client = discord.Client()

#@client.event
#async def on_ready():

  # for guild in client.guilds:
    #    if (guild.name == GUILD):
      #      break



  #  print(f'{client.user} is connected to the following server:\n '
    #f'{guild.name} (id:{guild.id})')

client.run('NzE2ODAyNDE0MDE5MzQ2NTAz.XtRPOg.Qr_Jo96Hn9q6FttdOH8mvRpm5jI')