import requests
from bs4 import BeautifulSoup

LINKEDIN_URL = (
    "https://www.linkedin.com/jobs/search/"
    "?keywords=#&position=1&pageNum=0"
)


def get_offers(skill):
    search_url = LINKEDIN_URL.replace("#", skill)

    response = requests.get(
        search_url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 Chrome/150.0 Safari/537.36"
            )
        },
        timeout=15
    )

    if response.status_code != 200:
        print(f"Error HTTP: {response.status_code}")
        return []

    print("EXTRACCIÓN DE DATOS...")

    html = BeautifulSoup(response.text, "html.parser")

    data_ofertas = html.find(
        "ul",
        class_="jobs-search__results-list"
    )

    if data_ofertas is None:
        print("No se encontró la lista de ofertas.")
        return []

    lista_ofertas = data_ofertas.find_all("li")
    resultado_ofertas = []

    for oferta in lista_ofertas:
        titulo = oferta.find(
            "h3",
            class_="base-search-card__title"
        )

        ubicacion = oferta.find(
            "span",
            class_="job-search-card__location"
        )

        enlace = oferta.find(
            "a",
            class_="base-card__full-link"
        )

        if titulo is None or ubicacion is None or enlace is None:
            continue

        href = enlace.get("href")

        if not href:
            continue

        dic_oferta = {
            "puesto": titulo.get_text(strip=True),
            "ubicacion": ubicacion.get_text(strip=True),
            "url": href.strip()
        }

        resultado_ofertas.append(dic_oferta)

    return resultado_ofertas
