import csv
from pathlib import Path
from prefect import task
from decouple import config

FILE_PATH = Path(config("PYTHON_PATH") + '/files/offers.csv')


@task(name="GUARDAR OFERTAS LABORALES EN CSV")
def save_offers(list_offers):
    with open(FILE_PATH, 'w') as file:
        writer = csv.DictWriter(
            file, fieldnames=['puesto', 'ubicacion', 'url']
        )
        writer.writerows(list_offers)
