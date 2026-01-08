from pyrogram import filters
from pytgcalls.types import AudioPiped
from main import app, call_py
from plugins.youtube import get_yt_stream # ensure youtube.py exists

@app.on_message(filters.command("play"))
async def play_command(client, message):
    if len(message.command) < 2:
        return await message.reply("Gane ka naam likho! Example: `/play Gulli`")

    # 1. Sabse pehle Processing message bhejein
    m = await message.reply("⚙️ **Processing...**")

    query = message.text.split(None, 1)[1]
    
    # 2. NexGen API se link nikalna
    details = get_yt_stream(query)

    if not details:
        return await m.edit("❌ **Gana nahi mila ya API error hai!**")

    try:
        # 3. Voice chat join karke stream start karna
        await call_py.join_group_call(
            message.chat.id,
            AudioPiped(details["url"])
        )
        
        # 4. Processing message ko update karke "Playing" dikhana
        await m.edit(f"🎶 **Playing Now:** {details['title']}\n\n👤 **Requested by:** {message.from_user.mention}")
        
    except Exception as e:
        await m.edit(f"⚠️ **Error:** `{e}`")
        
