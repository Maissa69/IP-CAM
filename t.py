# Importer la classe Camera
from cam_esp32 import Camera  # Remplace 'ton_fichier' par le nom du fichier contenant ta classe Camera

# Entrer l'IP de ton ESP32-CAM (celle obtenue depuis le moniteur série après la configuration)
ip_esp32_cam = '192.168.1.18'  # Remplace par l'adresse IP correcte

# Créer une instance de la classe Camera
camera = Camera(ip_esp32_cam)

# Lancer la capture du flux vidéo
camera.cam()
