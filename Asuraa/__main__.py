import asyncio
import importlib
from pyrogram import idle
from Asuraa import Asuraa
from Asuraa.modules import ALL_MODULES

LOGGER_ID = -1002100219353

loop = asyncio.get_event_loop()

async def JARVIS():
    for all_module in ALL_MODULES:
        importlib.import_module("Asuraa.modules." + all_module)
    print("Bot Started Successfully")
    await idle()
    print("MAI HU PIRO CODER BOLO NHI AAYA ERROR")
    await Asuraa.send_message(LOGGER_ID, "**𝖨 𝖺𝗆 𝖺𝗅𝗂𝗏𝖾 𝖡𝖺𝖻𝗒 𝖸𝗈𝗎𝗋 𝖡𝗈𝗍 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅 𝖣𝖾𝗉𝗅𝗈𝗒 \n Mʏ Dᴇᴠᴇʟᴏᴘᴇʀ [ɢᴏᴅ ʀᴀᴠᴀɴ](t.me/GOD_R4V4N)*")

if __name__ == "__main__":
    loop.run_until_complete(JARVIS())
    
