bad_words = ["fuck", "motherfucker", "shit", "کیر", "کون", "کوس"]

async def filter_messages(update, context):
    text = update.message.text.lower()

    if "http" in text:
        try:
            await update.message.delete()
        except:
            pass

    for w in bad_words:
        if w in text:
            try:
                await update.message.delete()
            except:
                pass