from .eneba import obtener_ofertas_eneba
from .amazon import obtener_ofertas_amazon
from .instant_gaming import obtener_ofertas_ig
from .ps_store import obtener_ofertas_ps_store
from .mediamarkt import obtener_ofertas_mediamarkt
from .carrefour import obtener_ofertas_carrefour
from .fnac import obtener_ofertas_fnac
from .game import obtener_ofertas_game
from .ps_direct import obtener_ofertas_ps_direct

def obtener_todas_las_ofertas():
    return (
        obtener_ofertas_eneba() +
        obtener_ofertas_amazon() +
        obtener_ofertas_ig() +
        obtener_ofertas_ps_store() +
        obtener_ofertas_mediamarkt() +
        obtener_ofertas_carrefour() +
        obtener_ofertas_fnac() +
        obtener_ofertas_game() +
        obtener_ofertas_ps_direct()
    )
