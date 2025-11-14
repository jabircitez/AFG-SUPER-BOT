from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📥 دانلود", callback_data="download_menu")],
        [InlineKeyboardButton("📊 مدیریت گروه", callback_data="admin_menu")],
        [InlineKeyboardButton("☎️ پشتیبانی", callback_data="support_menu")],
        [InlineKeyboardButton("ℹ️ درباره ربات", callback_data="about")]
    ])

def download_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("TikTok", callback_data="tiktok")],
        [InlineKeyboardButton("Instagram", callback_data="insta")],
        [InlineKeyboardButton("YouTube", callback_data="youtube")],
        [InlineKeyboardButton("بازگشت", callback_data="back")]
    ])