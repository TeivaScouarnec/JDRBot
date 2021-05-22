import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv(dotenv_path="config")
Server = commands.Bot
PlayerLists = []

#save a sheet's Player
def SavePlayer(idPlayer,name,descr):
    PlayerSheet = {
        "Id": idPlayer,
        "Name": name,
        "description": descr,
    }
    return PlayerSheet

def SearchSheet(name,key,list):
    for sheet in list:
        if sheet[key] == name:
            return sheet

#get all name's players in server
def GetAllNamePlayers():
    Names : list = []
    for nameplayer in PlayerLists:
        Name = nameplayer.get("Name")
        Names.append(Name)
    return Names

#get all id's players in server
def GetAllIdUser():
    Users : list = []
    for user in PlayerLists:
        Id = user.get("Id")
        Users.append(Id)
    return Users

class JDRBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")

    async def on_ready(self):
       print("JDRBot as connected on the server")

JDR = JDRBot()

#Commands
@JDR.command()
async def Player(ctx, arg1 = None, arg2 = None, arg3= None):
    CommandPlayer = arg1
    NamePlayer = arg2
    Description = arg3

    user = ctx.author
    UserID = user.id

    AllNamePlayers = GetAllNamePlayers()
    AllIdPlayers = GetAllIdUser()

    def embed(messageuser):
        message = discord.Embed(description=messageuser,colour=0xCC0000)
        return message

    if CommandPlayer == "show":
        if NamePlayer == None:
            message = "Actuellement, `" + str(AllNamePlayers) + "` sont cré(e)(s)"
            await ctx.send(embed=embed(message))
            return
        else:
            if not NamePlayer in AllNamePlayers:
                message = "Ce joueur n'existe pas!"
                await ctx.send(embed=embed(message))
                return
            else:
                PlayerSheet = SearchSheet(NamePlayer,"Name",PlayerLists)

                message = "**Nom:** `" + str(PlayerSheet.get("Name")) + "`, **description** " + str(PlayerSheet.get("description"))

                await ctx.send(embed=embed(message))
                return

    elif CommandPlayer == "create":
        if NamePlayer == None:
            message = "Veuillez entrer un nom pour la fiche personnage"
            await ctx.send(embed=embed(message))
            return
        else:
            if not NamePlayer in AllNamePlayers:
                PlayerLists.append(SavePlayer(UserID,NamePlayer,Description))
                message = NamePlayer + " a été crée(e)!"
                await ctx.send(embed=embed(message))
                return
            else:
                message = NamePlayer + " existe déjà!"
                await ctx.send(embed=embed(message))
                return
    else:
        message = "Veuillez entrer /create ou /show!"
        await ctx.send(embed=embed(message))
        return

JDR.run(os.getenv("TOKEN"))