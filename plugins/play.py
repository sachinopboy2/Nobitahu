from pyrogram import filters
from pytgcalls.types import AudioPiped
import yt_dlp
from main import app, call_py

# Assistant account ko join karwane ke liye
@app.on_message(filters.command("play"))
async def play_command(client, message):
    if len(message.command) < 2:
        return await message.reply("Gane ka naam likho! Example: `/play Gulli`")

    query = message.text.split(None, 1)[1]
    m = await message.reply("🔎 Searching...")

    try:
        ydl_opts = {"format": "bestaudio[ext=m4a]"}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
            url = info['url']
            title = info['title']

        await call_py.join_group_call(
            message.chat.id,
            AudioPiped(url)
        )
        await m.edit(f"🎶 **Playing Now:** {title}")
    except Exception as e:
        await m.edit(f"Error: {e}")
      
