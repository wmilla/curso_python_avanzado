# trabajo con archivos csv
import csv
from pathlib import Path

FILE_PATH = Path("users.csv")


def read_csv():
    try:
        with open(FILE_PATH, "r") as file:
            reader = csv.DictReader(file)  # convierte a un diccionario
            for row in reader:
                print(f"{row.get("first_name")} : {row.get("email")}")
    except FileNotFoundError:
        print("no se encontró el archivo")


def write_csv():
    try:
        with open(FILE_PATH, "a") as file:  # "a" es de append
            writer = csv.DictWriter(
                file, fieldnames=["first_name", "last_name", "email"]
            )

            writer.writerows([
                {
                    "first_name": "César",
                    "last_name": "Mayta",
                    "email": "cesarmayta@ed.team"
                },
                {
                    "first_name": "Alvaro",
                    "last_name": "Felipe",
                    "email": "alvaro@ed.team"
                }
            ])
            print("datos agregados")
    except FileNotFoundError:
        print("No se encontró el archivo")


if __name__ == "__main__":
    write_csv()
    read_csv()
