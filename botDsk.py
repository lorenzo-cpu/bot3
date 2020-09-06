import discord
from discord.ext import commands
from discord import client

print("il tuo bot si sta avviando...")
token = "NzUxOTY5MTY4NDU0MDU4MDE1.X1Qz3A.KYn7gfWLEkgqAJYXxz8bMbzJdk0"
client = commands.Bot(command_prefix = ("--")) 

@client.event 
async def on_ready():  
    print(client.user, "è ora ONLINE (ID: ", client.user.id,")")

@client.command() 
async def ciaociao(ctx):
    await ctx.send("ciao")

@client.command() 
async def Cancella5Messaggi(ctx, amount = 6):
    await ctx.channel.purge(limit = amount)


        
client.run(token)


