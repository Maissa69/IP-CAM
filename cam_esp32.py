import cv2
import numpy as np

class Camera:
    def __init__(self,ip):
        self.ip = ip
    def cam (self):
        adress = 'http://' + self.ip + ':81/stream'
        cap = cv2.VideoCapture(adress)

        while True:
            ret, frame = cap.read()  # Lire une image du flux vidéo
            if not ret:
                print("Impossible de recevoir le flux vidéo.")
                break

            # Afficher l'image
            cv2.imshow('ESP32-CAM', frame)

            # Quitter la boucle avec la touche 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Libérer les ressources
        cap.release()
        cv2.destroyAllWindows()
        
        