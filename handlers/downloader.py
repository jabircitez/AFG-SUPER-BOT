import requests
from yt_dlp import YoutubeDL
from telegram import Update
from telegram.ext import ContextTypes

async def download_youtube(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = context.args[0]
    await update.message.reply_text("⏳ در حال دانلود از YouTube ...")

    ydl_opts = {"outtmpl": "video.mp4"}
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    await update.message.reply_video("video.mp4")

async def download_tiktok(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = context.args[0]
    await update.message.reply_text("⏳ دانلود TikTok ...")

    api = f"https://api.tikmate.app/api/lookup?url={url}"
    r = requests.get(api).json()
    link = f"https://tikmate.app/download/{r['token']}/{r['id']}.mp4"

    await update.message.reply_video(link)

async def download_instagram(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = context.args[0]
    await update.message.reply_text("⏳ دانلود Instagram ...")

    api = f"https://saveinsta.io/core/ajax.php?url={url}"
    res = requests.get(api).json()
    media = res["medias"][0]["url"]

    await update.message.reply_video(media)