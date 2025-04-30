import os
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater
from scraper.eneba import obtener_ofertas_eneba

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")

def publicar_ofertas():
    bot = Bot(token=TOKEN)
    ofertas = obtener_ofertas_eneba()
    for oferta in ofertas:
        mensaje = f"{oferta['titulo']}\nPrecio: {oferta['precio']}"
        boton = [[InlineKeyboardButton("Ir a la oferta", url=oferta['url'])]]
        reply_markup = InlineKeyboardMarkup(boton)
        bot.send_message(chat_id=CHANNEL_ID, text=mensaje, reply_markup=reply_markup)

if __name__ == "__main__":
    publicar_ofertas()
