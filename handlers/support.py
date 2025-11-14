from telegram import Update
from telegram.ext import ContextTypes
from utils.config import OWNER_ID

async def forward_to_owner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user = update.message.from_user
    await context.bot.send_message(
        OWNER_ID,
        f"📩 پیام جدید\n"
        f"👤 {user.first_name}\n"
        f"🆔 ID: {user.id}\n"
        f"💬 پیام: {text}"
    )
    await update.message.reply_text("پیام شما به پشتیبانی ارسال شد ✔️")

async def owner_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        return

    parts = update.message.text.split(" ", 1)
    if len(parts) < 2:
        await update.message.reply_text("فرمت اشتباه. مثال:\n/reply 123456 سلام")
        return

    user_id, msg = parts
    try:
        user_id = int(user_id.replace("/reply", "").strip())
    except:
        await update.message.reply_text("ID درست نیست.")
        return

    await context.bot.send_message(user_id, f"📨 پاسخ پشتیبان:\n{msg}")
    await update.message.reply_text("ارسال شد ✔️")