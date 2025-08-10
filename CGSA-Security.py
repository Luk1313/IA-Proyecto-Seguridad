import cv2
import time
import threading

class SistemaSeguridadCajero:
    def __init__(self, camaras):
        self.camaras = camaras
        self.grabacion_activa = False
        self.alarma_activada = False

    def iniciar_camaras(self):
        """
        Inicia la transmisión de las cámaras y lanza un hilo por cámara para monitoreo continuo.
        """
        for camara_url in self.camaras:
            hilo = threading.Thread(target=self.monitorear_camara, args=(camara_url,), daemon=True)
            hilo.start()

    def monitorear_camara(self, camara_url):
        """
        Monitorea la cámara en tiempo real y evalúa riesgos basados en eventos.
        """
        cap = cv2.VideoCapture(camara_url)

        if not cap.isOpened():
            print(f"❌ Error al conectar con la cámara {camara_url}")
            return

        print(f"✅ Monitoreando cámara: {camara_url}")
        while True:
            ret, frame = cap.read()
            if not ret:
                print(f"⚠️ Error al recibir datos de {camara_url}")
                break

            # Evaluación de eventos
            movimiento = self.detectar_movimiento(frame)
            obstruccion = self.detectar_obstruccion(frame)
            manipulacion = self.detectar_manipulacion(frame)

            riesgo = self.evaluar_riesgo(movimiento, obstruccion, manipulacion)

            if riesgo == "ALTO":
                self.activar_alarma()
                self.grabar_video(frame)
                self.enviar_alerta_seguridad()
            elif riesgo == "MEDIO":
                self.grabar_video(frame)
            else:
                print("Monitoreo activo: sin incidentes.")

            time.sleep(1)  # Evita consumo excesivo de CPU

        cap.release()

    def detectar_movimiento(self, frame):
        """
        Lógica para detectar movimiento anómalo (puede integrarse IA o background subtraction).
        """
        return False  # Simulación de resultado

    def detectar_obstruccion(self, frame):
        """
        Lógica para detectar obstrucción (por ejemplo, imagen completamente oscura o borrosa).
        """
        return False

    def detectar_manipulacion(self, frame):
        """
        Lógica para detectar manipulación del cajero (puede integrarse IA o cambios bruscos).
        """
        return False

    def evaluar_riesgo(self, movimiento, obstruccion, manipulacion):
        """
        Evalúa el nivel de riesgo según los indicadores detectados.
        """
        if manipulacion or obstruccion:
            return "ALTO"
        elif movimiento:
            return "MEDIO"
        return "BAJO"

    def activar_alarma(self):
        if not self.alarma_activada:
            print("\n🚨 Alarma activada: incidente detectado 🚨")
            self.alarma_activada = True
            # Aquí se puede integrar señal al hardware externo

    def grabar_video(self, frame):
        if not self.grabacion_activa:
            self.grabacion_activa = True
            print("📹 Grabación iniciada como evidencia.")
            # Aquí puedes guardar el frame como imagen o iniciar escritura de video

    def enviar_alerta_seguridad(self):
        print("📡 Alerta enviada a seguridad y autoridades.")
        # Aquí se integraría el envío por email, Telegram, WhatsApp, etc.


if __name__ == "__main__":
    camaras_ip = [
        "http://192.168.1.10:8080/video",
        "http://192.168.1.11:8080/video",
        "http://192.168.1.12:8080/video",
        "http://192.168.1.13:8080/video"
    ]

    sistema = SistemaSeguridadCajero(camaras_ip)
    sistema.iniciar_camaras()

    # Mantener el programa vivo para que los hilos continúen
    while True:
        time.sleep(10)
