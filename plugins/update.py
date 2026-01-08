import os
import subprocess
import sys
from pyrogram import filters
from config import OWNER_ID
from main import app

@app.on_message(filters.command("update") & filters.user(OWNER_ID))
async def update_bot(client, message):
    m = await message.reply("⚙️ **GitHub se updates check kar raha hoon...**")
    
    try:
        # GitHub se latest code pull karna
        pull = subprocess.check_output(["git", "pull"]).decode("utf-8")
        
        if "Already up to date." in pull:
            return await m.edit("✅ **Bot pehle se hi updated hai!**")
        
        await m.edit(f"✨ **Updates mile!**\n\n`{pull}`\n\n🔄 **Bot restart ho raha hai...**")
        
        # VPS par process ko restart karna
        os.execl(sys.executable, sys.executable, "main.py")
        
    except Exception as e:
        await m.edit(f"❌ **Update Error:** `{e}`")
      
