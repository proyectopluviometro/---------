"""
Registrador de datos del pluviómetro (Arduino)
------------------------------------------------
Este script se conecta al puerto serie del Arduino y guarda automáticamente
todo lo que recibe (temperatura, humedad, lluvia) en un archivo CSV, con
fecha y hora reales de la computadora.

INSTRUCCIONES DE USO:

1. Cierra el Monitor Serie del Arduino IDE (o el Plotter). El puerto COM8
   solo puede estar abierto por un programa a la vez.

2. Instala la librería necesaria (solo la primera vez), abriendo una
   terminal / símbolo del sistema y escribiendo:

       pip install pyserial

3. Revisa las variables PUERTO y BAUDIOS abajo y ajústalas si tu Arduino
   usa otro puerto (por ejemplo COM3) o otra velocidad.

4. Ejecuta el script:

       python registrar_pluviometro.py

5. Deja la ventana abierta el tiempo que quieras registrar datos
   (puede ser todo el día). Para detenerlo, presiona Ctrl + C.

6. Los datos quedarán guardados en el archivo "datos_pluviometro.csv",
   en la misma carpeta donde esté este script. Ese archivo lo puedes
   abrir con Excel o subir a tu repositorio.
"""

import csv
import re
import serial
from datetime import datetime

# ----------------- CONFIGURACIÓN -----------------
PUERTO = "COM8"          # Cambia esto si tu Arduino usa otro puerto
BAUDIOS = 9600            # Debe coincidir con Serial.begin() en tu código
ARCHIVO_SALIDA = "../data/datos_pluviometro.csv"
# ---------------------------------------------------


def main():
    print(f"Conectando a {PUERTO} a {BAUDIOS} baudios...")
    try:
        arduino = serial.Serial(PUERTO, BAUDIOS, timeout=2)
    except serial.SerialException as e:
        print("No se pudo abrir el puerto. Revisa que:")
        print(" - El Monitor Serie / Plotter del Arduino IDE esté cerrado")
        print(" - El nombre del puerto (PUERTO) sea el correcto")
        print(f"Detalle del error: {e}")
        return

    # Creamos el archivo CSV y escribimos el encabezado si no existe
    archivo_nuevo = True
    try:
        with open(ARCHIVO_SALIDA, "r"):
            archivo_nuevo = False
    except FileNotFoundError:
        pass

    with open(ARCHIVO_SALIDA, "a", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        if archivo_nuevo:
            escritor.writerow(["fecha_hora", "temperatura_C", "humedad_%", "lluvia_V"])

        print(f"Guardando datos en '{ARCHIVO_SALIDA}'. Presiona Ctrl+C para detener.\n")

        # Guardamos la última temperatura y humedad leídas para poder
        # armar una sola fila completa cuando llegue el dato de lluvia
        temp_actual = None
        hum_actual = None

        try:
            while True:
                linea = arduino.readline().decode("utf-8", errors="ignore").strip()
                if not linea:
                    continue

                print(linea)  # también lo mostramos en pantalla

                if "emperatura" in linea:
                    m = re.search(r"([\d.]+)", linea)
                    if m:
                        temp_actual = m.group(1)

                elif "Humedad" in linea:
                    m = re.search(r"([\d.]+)", linea)
                    if m:
                        hum_actual = m.group(1)

                elif "Lluvia" in linea:
                    m = re.search(r"([\d.]+)", linea)
                    if m:
                        lluvia_actual = m.group(1)
                        marca_tiempo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        escritor.writerow([marca_tiempo, temp_actual, hum_actual, lluvia_actual])
                        f.flush()  # aseguramos que se guarde en disco al instante

        except KeyboardInterrupt:
            print("\nRegistro detenido por el usuario. Archivo guardado correctamente.")
        finally:
            arduino.close()


if __name__ == "__main__":
    main()
