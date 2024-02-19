import discord
from datetime import datetime

intents = discord.Intents.default()

# If your bot will interact with members (send messages, listen to messages, etc.)
intents.members = True
intents.presences = True
intents.message_content = True

client = discord.Client(intents=intents)

answer = "Pokud neni day one neco se posralo"  # Define answer as a global variable
lidi = {}
score = {}

@client.event
async def on_ready():
    print("Let's goooooooooooooooooooooooo")

@client.event
async def on_message(message):
    global answer  # Use the global answer variable
    global lidi
    global score
    if message.author == client.user:
        return
    
    if str(message.channel) != "fyziklání-odpovědi":
        return
    
    kdo = str(message.author)
    if kdo == "lukissf" and message.content[0] == "|" and message.content[1] == "|" and message.content[-1] == "|" and message.content[-2] == "|":
        await message.channel.send(score)

        
        date = datetime.today().date()
        string = "Včerejší odpověď byla " + answer + "\n---------------------------------------------------------- KONTROLUJEME DEN " + str(date) + " ODPOVĚĎ BUDE ZÍTRA ----------------------------------------------------------"

        answer = message.content
        await message.channel.send(string)
        lidi = {}
        score = {}
    elif message.content[0] == "|" and message.content[1] == "|" and message.content[-1] == "|" and message.content[-2] == "|":
        zprava = str(message.content)
        if kdo in score:
            await message.channel.send("neser mě")
            return

        if kdo not in lidi:
            lidi[kdo] = 5

        if zprava == answer:
           await message.channel.send("gj máš to dobře")
           score[kdo] = lidi[kdo]
        else:
           await message.channel.send("kappa to to neni")
           if lidi[kdo] == 5:
               lidi[kdo] = 3
           elif lidi[kdo] > 1:
               lidi[kdo] -= 1


client.run("MTIwOTE2MzU2NTc0ODA2NDM0Nw.GFp83t.DdrcqbMESz5D-7bgC8pOOlPwGhGlsMnwSLINsU")
