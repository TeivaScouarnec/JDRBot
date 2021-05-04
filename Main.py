import discord

client = discord.Client()

@client.event
async def on_ready():
    print("Bot On")

@client.event
async def on_message(message):
    if message.content == "Ping":
        await message.channel.send("Pong")

client.run("ODM5MTgwOTg3NTQzMDYwNTYw.YJF6Mg.hWRcx4XKPyhgPJkwo7nmzIfTmkc")