import discord
from discord.ext import commands

PlayerLists = []

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

def embed(messageuser):
    message = discord.Embed(description=messageuser, colour=0xCC0000)
    return message

class UserCommand(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

    @commands.command()
    async def Player(self,ctx, arg1=None, arg2=None, arg3=None):
        CommandPlayer = arg1
        NamePlayer = arg2
        Description = arg3

        user = ctx.author
        UserID = user.id

        AllNamePlayers = GetAllNamePlayers()
        AllIdPlayers = GetAllIdUser()

        if CommandPlayer == "show":
            if NamePlayer == None:
                message = "Actuellement, `" + str(AllNamePlayers) + "` sont cré(e)(s)"
                await ctx.send(embed=embed(message))
                await ctx.message.delete()
                return
            else:
                if not NamePlayer in AllNamePlayers:
                    message = "Ce joueur n'existe pas!"
                    await ctx.send(embed=embed(message))
                    await ctx.message.delete()
                    return
                else:
                    PlayerSheet = SearchSheet(NamePlayer, "Name", PlayerLists)

                    message = "**Nom:** `" + str(PlayerSheet.get("Name")) + "`, **description** " + str(
                        PlayerSheet.get("description"))

                    await ctx.send(embed=embed(message))
                    await ctx.message.delete()
                    return

        elif CommandPlayer == "create":
            if NamePlayer == None:
                message = "Veuillez entrer un nom pour la fiche personnage"
                await ctx.send(embed=embed(message))
                await ctx.message.delete()
                return
            else:
                if not NamePlayer in AllNamePlayers:
                    PlayerLists.append(SavePlayer(UserID, NamePlayer, Description))
                    message = NamePlayer + " a été crée(e)!"
                    await ctx.send(embed=embed(message))
                    await ctx.message.delete()
                    return
                else:
                    message = NamePlayer + " existe déjà!"
                    await ctx.send(embed=embed(message))
                    await ctx.message.delete()
                    return
        else:
            message = "Veuillez entrer /create ou /show!"
            await ctx.send(embed=embed(message))
            await ctx.message.delete()
            return

def setup(bot):
    bot.add_cog(UserCommand(bot))