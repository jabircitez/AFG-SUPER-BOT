from telegram import Update
from telegram.ext import ContextTypes
from utils.config import OWNER_ID

async def ban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        return
    if not update.message.reply_to_message:
        await update.message.reply_text("به پیام کاربر ریپلای کن.")
        return
    await update.message.chat.ban_member(update.message.reply_to_message.from_user.id)
    await update.message.reply_text("کاربر بن شد ❌")

async def mute(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        return
    if not update.message.reply_to_message:
        await update.message.reply_text("به پیام کاربر ریپلای کن.")
        return
    await update.message.chat.restrict_member(
        update.message.reply_to_message.from_user.id,
        permissions={"can_send_messages": False}
    )
    await update.message.reply_text("کاربر بی‌صدا شد 🔇")
