import os
import shutil
import msvcrt
import sys

usb_letra = "E"  # letra inicial por defecto

def obtener_ruta(letra):
    return f"{letra}:\\"

def cambiar_letra():
    print("\nPut the new letter here (ej: F): ", end="")
    letra = input().strip().upper()

    if len(letra) != 1 or not letra.isalpha():
        print("Letter not found (404).")
        return None

    if letra == "C":
        print("You CAN'T use C: (system).")
        return None

    ruta = obtener_ruta(letra)
    if not os.path.exists(ruta):
        print(f"Letter {letra}: doesn't exist.")
        return None

    print(f"Changed to: {letra}:")
    return letra

print("=== PANIC USB/SD ===")
print("ESC = delate ALL files")
print("N   = Change route of USB")

while True:
    print(f"USB/ SD: {usb_letra}:\\")
    print("waiting command...")

    tecla = msvcrt.getch()

    if tecla == b'\x1b':  # ESC
        USB_PATH = obtener_ruta(usb_letra)

        if not os.path.exists(USB_PATH):
            print("ERROR: USB/SD not detected.")
            continue

        print("ERASING ALL...")
        for item in os.listdir(USB_PATH):
            full = os.path.join(USB_PATH, item)
            try:
                if os.path.isfile(full):
                    os.remove(full)
                elif os.path.isdir(full):
                    shutil.rmtree(full)
            except:
                pass

        print("Erased with any matter. Kamikaze.py can be closed.")
        sys.exit()

    elif tecla in (b'n', b'N'):
        nueva = cambiar_letra()
        if nueva:
            usb_letra = nueva

