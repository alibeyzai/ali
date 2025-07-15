from telegram import Update, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

# توکن ربات از BotFather
BOT_TOKEN = "8134187462:AAHlwuANjWdEFbraKjuKh-vSCYMbuWt92ow"

# دیتابیس موقت ذخیره آدرس‌ها
user_addresses = {}

# شروع ربات
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌟 خوش اومدی به ربات رسمی توکن HAKHAMEN (HKM)\n\n"
        "دستورات:\n"
        "/token – اطلاعات توکن\n"
        "/pool – وضعیت استخر\n"
        "/airdrop – ثبت‌نام ایردراپ\n"
        "/faq – سوالات پرتکرار\n"
        "/contact – تماس با ادمین"
    )

# اطلاعات توکن
async def token(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🪙 اطلاعات توکن HKM:\n"
        "نام: HAKHAMEN\n"
        "نماد: HKM\n"
        "Decimals: 6\n"
        "Total Supply: 100,000,000\n"
        "آدرس قرارداد:\n"
        "`EQC_tZ2xxrbjWptQrtlbAV5GWnLdnUG-T4UQECIT7YxWrwmw`",
        parse_mode='Markdown'
    )

# اطلاعات استخر
async def pool(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔗 استخر نقدینگی:\n"
        "https://app.ston.fi/swap?chartVisible=false&ft=TON&tt=EQC_tZ2xxrbjWptQrtlbAV5GWnLdnUG-T4UQECIT7YxWrwmw"
    )

# شروع ایردراپ
async def airdrop_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔐 لطفاً آدرس کیف پول TON خود را ارسال کن:")
    return 1  # رفتن به مرحله بعد

# گرفتن آدرس TON و ذخیره
async def save_address(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    address = update.message.text
    user_addresses[user_id] = address
    await update.message.reply_text("✅ آدرس ذخیره شد. موفق باشی!")
    return ConversationHandler.END

# لغو عملیات
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ عملیات لغو شد.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

# سوالات پرتکرار
async def faq(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 سوالات پرتکرار:\n"
        "– HKM رو از کجا بخرم؟\n"
        "👉 از استخر Ston: /pool\n"
        "– کیف پول مناسب چیه؟\n"
        "👉 TON Keeper یا MyTonWallet\n"
        "– چجوری نقدینگی بدم؟\n"
        "👉 آموزش در وب‌سایت رسمی به‌زودی"
    )

# راه تماس
async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📬 تماس با ادمین: @binesh_beyzaii")

# اجرای ربات
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("token", token))
    app.add_handler(CommandHandler("pool", pool))
    app.add_handler(CommandHandler("faq", faq))
    app.add_handler(CommandHandler("contact", contact))

    # ایردراپ با گرفتن ورودی
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("airdrop", airdrop_start)],
        states={1: [MessageHandler(filters.TEXT & ~filters.COMMAND, save_address)]},
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    app.add_handler(conv_handler)

    app.run_polling()

if __name__ == '__main__':
    main()
