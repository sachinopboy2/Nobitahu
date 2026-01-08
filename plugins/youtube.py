import yt_dlp
from pyrogram import filters

def get_youtube_stream(query):
    ydl_opts = {
        "format": "bestaudio[ext=m4a]",
        "quiet": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
            return {
                "videoid": info['id'],
                "title": info['title'],
                "url": info['url'],
                "duration": info['duration'],
            }
        except Exception:
            return None

