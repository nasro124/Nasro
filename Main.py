import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from pyrogram import Client, filters

# ==================================================
# 1. QAABAYNTA SIRTA AH
# ==================================================
API_TOKEN = '837943577:AAFc2NKsW...'  # Token-kaaga rasmiga ah ee BotFather
API_ID = 37969354
API_HASH = '314b542bff26b9af4a816e029066ce37'
MINI_APP_URL = 'https://ciwaanka-app-kaaga.com' # Link-ga Mini App-kaaga
STRING_SESSION = "BAJDXcoAm0CVO2lBemYSOK8LyFCI_ah1wOpcApckCzyI8sja7rQ9nTGbyx0Dq_WOmCLwV4QJzB-CZS83wVyKGBkzNuj1AeWko1Via5lXKCGYEUJerWbydgJqKOpsvVWObA80_z0CWDlYzmvAUeQE4qktrfDn0Qnj-wB1JoQ2bFHJXn0K9gDIJtj3VLEP74GC5NH83lZhrpQnV8MPHzUHc4BdA5F2YAnT-yKWTiGvYY0HJuQvdRiIfRQO-VM39a1Uc5RCbBvn9VnLsuJM6A27CnpfLDldcje5NwmkQjpxm5SuR2tq_ecCDbv0N2p_zT6I76ctXmYer_aXo5wtazbwV9ysqS_LoAAAAAF-XDvuAA"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

userbot = Client(
    "bot_user_session",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION
)

# ==================================================
# 2. BOT-KA MACAAMIISHA (Aiogram)
# ==================================================
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="📱 Open Mini App", web_app=types.WebAppInfo(url=MINI_APP_URL))]],
        resize_keyboard=True
    )
    await message.reply(
        "👋 Ku soo dhawaada Bot-keena rasmiga ah!\n\n"
        "Fadlan riix badhanka hoose si aad u furto Mini App-ka rasmiga ah.", 
        reply_markup=keyboard
    )

# ==================================================
# 3. KICINTA LABADA HAL MAR
# ==================================================
async def main():
    print("[*] Waxaa la kicinayaa Userbot-ka...")
    await userbot.start()
    print("[+] Userbot-ku si guul leh ayuu u bilowday!")
    
    print("[*] Waxaa la kicinayaa Bot-ka macaamiisha...")
    try:
        await dp.start_polling(bot)
    finally:
        await userbot.stop()

if __name__ == "__main__":
    asyncio.run(main())
  
