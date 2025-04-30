import os
import time
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from scraper.eneba import obtener_ofertas_eneba

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")

publicadas = set()

def publicar_ofertas():
    bot = Bot(token=TOKEN)
    ofertas = obtener_ofertas_eneba()
    for oferta in ofertas:
        if oferta['url'] in publicadas:
            continue  # Evitar repetir
        mensaje = f"{oferta['titulo']}\nPrecio: {oferta['precio']}"
        boton = [[InlineKeyboardButton("Ir a la oferta", url=oferta['url'])]]
        reply_markup = InlineKeyboardMarkup(boton)
        bot.send_message(chat_id=CHANNEL_ID, text=mensaje, reply_markup=reply_markup)
        publicadas.add(oferta['url'])

if __name__ == "__main__":
    while True:
        publicar_ofertas()
        time.sleep(600)  # Espera 10 minutos antes de volver a buscar
