"""
PROGRAMA PARA GUARDAR DATOS DE MI PC
"""
import platform
import socket


def guardar_pc_info():
    pc_data = "==========INFO DE PC =============\n"
    pc_data += (
        f"SISTEMA OPERATIVO : "
        f"{platform.system()} "
        f"{platform.version()} \n")
    pc_data += (
        f"ARQUITECTURA : "
        f"{platform.machine()} \n")
    pc_data += (
        f"PROCESADOR : "
        f"{platform.processor()} \n")
    pc_data += (
        f"HOSTNAME : "
        f"{socket.gethostname()} \n")
    pc_data += (
        f"IP : "
        f"{socket.gethostbyname(socket.gethostname())} \n")

    pc_file = open("pc.docx", "w")
    pc_file.write(pc_data)
    pc_file.close()


def leer_pc_info():
    try:
        pc_file = open("pc.docx", "r")
        pc_data = pc_file.read()
        print(pc_data)
        pc_file.close()
    except FileNotFoundError:
        print("No se encontró el archivo")


if __name__ == '__main__':
    guardar_pc_info()
    leer_pc_info()
