import csv
import time
import pyinotify

# Ruta al archivo de registro de eventos en sistemas Ubuntu/Debian
archivo_registro = "/var/log/syslog"

# Función para observar cambios en el archivo de registro de eventos
class ObservadorEventos(pyinotify.ProcessEvent):
    def process_IN_MODIFY(self, event):
        evento = leer_ultimo_evento(archivo_registro)
        if evento:
            print(evento)
            # Guardar evento en el archivo CSV especificado
            guardar_evento_en_csv(ruta_csv, evento)

# Función para leer el último evento del archivo de registro de eventos
def leer_ultimo_evento(archivo):
    try:
        with open(archivo, "r") as file:
            lineas = file.readlines()
            return lineas[-1].strip()
    except FileNotFoundError:
        return None

# Función para guardar eventos en un archivo CSV
def guardar_evento_en_csv(ruta_csv, evento):
    with open(ruta_csv, mode="a", newline="", encoding="utf-8") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), evento])

if __name__ == "__main__":
    print("Sistema de Monitorización de Eventos del Sistema (Linux)")
    ruta_csv = "data/syslogs.csv"  # Reemplaza con la ruta deseada
    # Crea el archivo CSV si no existe y escribe un encabezado
    with open(ruta_csv, mode="w", newline="", encoding="utf-8") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(["Timestamp", "Evento"])

    # Configuración de pyinotify para observar cambios en el archivo de registro de eventos
    wm = pyinotify.WatchManager()
    mask = pyinotify.IN_MODIFY
    handler = ObservadorEventos()
    notifier = pyinotify.Notifier(wm, handler)

    # Agrega el archivo de registro de eventos a la lista de observación
    wdd = wm.add_watch(archivo_registro, mask, rec=True)

    while True:
        try:
            notifier.process_events()
            if notifier.check_events():
                notifier.read_events()
        except KeyboardInterrupt:
            notifier.stop()
            break