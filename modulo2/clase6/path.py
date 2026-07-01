import os
from pathlib import Path

ruta = Path(r"C:\Development\prueba\Captura de pantalla 2026-06-30 150444.png")
con_os = r"C:\Development\prueba\Captura de pantalla 2026-06-30 150444.png"
print("======================= con os =====================================")
print(os.path.exists(con_os))
print(os.path.basename(con_os))
print(os.path.dirname(con_os))
print(os.path.getsize(con_os))
print(os.path.splitext(con_os))

print("================== con pathlib =====================================")
print(ruta.exists())
print(ruta.name)
print(ruta.parent)
print(ruta.suffix)
