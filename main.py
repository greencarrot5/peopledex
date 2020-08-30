# Get folder the project is in
import os
path = os.path.dirname(__file__)

import discord

class bot(discord.Client):
    
    # When bot logged in
    async def on_ready(self):
        print("Ready!")
    
    # When bot receives a message
    async def on_message(self, msg):
        pass

peopledex = bot()
peopledex.run(open(".env").read())