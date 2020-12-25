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
        @self.app.route('/')
        def home():
            return "Hello world!"
    
    def run(self):
        self.app.run()
        
WebSite().start()

# Here starts the bot code
import discord
import re
import urllib.request

def firstImage(q):
    
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    
    url = "https://www.google.com/search?q=" + q.replace(" ", "+")
    headers = {'User-Agent':user_agent} 
    request = urllib.request.Request(url, headers=headers) #The assembled request
    response = urllib.request.urlopen(request)
    data = response.read().decode("utf8")
    match = re.search("<img src=['\"]([^'\"]*)['\"]", data)
    src = match.group(1)
    return src

class bot(discord.Client):
    
    # When bot logged in
    async def on_ready(self):
        print("Ready!")
    
    # When bot receives a message
    async def on_message(self, msg):
        
        # Check if user pinged bot
        if msg.content.startsWith("--google "):
            q = msg.content.replace("--google ", "")
            embed = discord.Embed(title=q)
            embed.setImage(firstImage(q))
            await msg.channel.send(embed)

peopledex = bot()
peopledex.run(open("env").read())
