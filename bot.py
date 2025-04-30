import os
import asyncio
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "scraper"))
from __init__ import obtener_todas_las_ofertas

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")

publicadas = set()

async def publicar_ofertas():
    bot = Bot(token=TOKEN)
    ofertas = obtener_todas_las_ofertas()
    for oferta in ofertas:
        if oferta["url"] in publicadas:
            continue
        mensaje = f"*{oferta['titulo']}*\nPrecio: {oferta['precio']}"
        boton = [[InlineKeyboardButton("Ir a la oferta", url=oferta["url"])]]
        reply_markup = InlineKeyboardMarkup(boton)
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=mensaje,
            reply_markup=reply_markup,
            parse_mode=ParseMode.MARKDOWN
        )
        publicadas.add(oferta["url"])

async def main():
    while True:
        await publicar_ofertas()
        await asyncio.sleep(600)  # 10 minutos

if __name__ == "__main__":
    asyncio.run(main())
