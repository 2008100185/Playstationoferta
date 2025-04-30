import requests
from bs4 import BeautifulSoup

def obtener_ofertas_ig():
    url = "https://www.instant-gaming.com/es/busquedas/?q=playstation"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    juegos = []

    for producto in soup.select("div.item"):
        titulo_tag = producto.select_one(".name")
        precio_tag = producto.select_one(".price")
        enlace_tag = producto.select_one("a")

        if not titulo_tag or not precio_tag or not enlace_tag:
            continue

        titulo = titulo_tag.text.strip()
        precio = precio_tag.text.strip()
        enlace = "https://www.instant-gaming.com" + enlace_tag.get("href")

        if "ps4" in titulo.lower() or "ps5" in titulo.lower() or "playstation" in titulo.lower():
            juegos.append({
                "titulo": titulo,
                "precio": precio,
                "url": enlace
            })

    return juegos
