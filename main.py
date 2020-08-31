# Get folder the project is in
import os
path = os.path.dirname(__file__)

# If repl.it doesn't serve web-content, it shuts down
from flask import Flask
from threading import Thread

class WebSite(Thread):
    def __init__(self):
        super().__init__()
        self.app = Flask(__name__)
        @app.route('/')
        def home():
            return "Hello world!"
    
    def run(self):
        self.app.run()
        
WebSite().run()

# Here starts the bot code
import discord
import re

class bot(discord.Client):
    
    # When bot logged in
    async def on_ready(self):
        print("Ready!")
    
    # When bot receives a message
    async def on_message(self, msg):
        
        # Check if user pinged bot
        if re.search("<@749692977483350137>", msg.content):
            msg.channel.send("Hello, " + str(msg.author) + "!")

peopledex = bot()
peopledex.run(open(".env").read())