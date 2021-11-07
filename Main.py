import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from cogs import UserDiscord

load_dotenv(dotenv_path="config")
Server = commands.Bot

class JDRBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")

    async def on_ready(self):
       print("JDRBot as connected on the server")

JDR = JDRBot()

JDR.load_extension("cogs.UserDiscord")

JDR.run(os.getenv("TOKEN"))