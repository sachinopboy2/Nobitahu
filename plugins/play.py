import os
from pyrogram import filters
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioPiped
from main import app, call_py  # Aapki main.py se app aur call_py le raha hai
from plugins.youtube import get_yt_stream # YouTube details nikalne ke liye
from config import OWNER_ID

@app.on_message(filters.command("play") & filters.group)
async def play_command(client, message):
    # 1. Check karein ki user ne gane ka naam likha hai ya nahi
    if len(message.command) < 2:
        return await message.reply_text("✨ **Usage:** `/play [Song Name/URL]`")

    # 2. Processing message dikhayyein
    m = await message.reply_text("⚙️ **Processing... Please wait.**")

    query = message.text.split(None, 1)[1]

    # 3. NexGen API se link nikalna (youtube.py ka function)
    details = get_yt_stream(query)

    if not details:
        return await m.edit("❌ **Gana nahi mila!** Check your API Key or connection.")

    title = details["title"]
    stream_url = details["url"]

    try:
        # 4. Voice chat join karke audio stream karna
        # PyTgCalls v2.x mein play() ya join_group_call use hota hai
        await call_py.join_group_call(
            message.chat.id,
            AudioPiped(stream_url)
        )

        # 5. Message update karein jab gana shuru ho jaye
        await m.edit(
            f"🎶 **Started Streaming**\n\n"
            f"📝 **Title:** {title}\n"
            f"👤 **Requested by:** {message.from_user.mention}"
        )

    except Exception as e:
        await m.edit(f"⚠️ **Error:** `{e}`")

# Extra: Stop command
@app.on_message(filters.command("stop") & filters.group)
async def stop_command(client, message):
    try:
        await call_py.leave_group_call(message.chat.id)
        await message.reply_text("🔇 **Streaming stopped by user.**")
    except:
        await message.reply_text("❌ **Bot is not streaming anything.**")
        
