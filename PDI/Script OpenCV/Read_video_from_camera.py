import cv2                                                    # Importa la biblioteca OpenCV

cap = cv2.VideoCapture(0)                                     # Abre la cámara web (0 = cámara predeterminada)

while(True):                                                  # Bucle infinito para capturar video en tiempo real

    ret, frame = cap.read()                                   # Captura un fotograma de la cámara
                                                              # ret = True si la captura fue exitosa
                                                              # frame = imagen capturada

    cv2.imshow('CamaraWeb', frame)                    # Muestra el fotograma en una ventana llamada "CamaraWeb"

    if cv2.waitKey(1) & 0xFF == ord('q'):                     # Si se presiona la tecla 'q'
        break                                                 # Sale del bucle

cap.release()                                                 # Libera la cámara web

cv2.destroyAllWindows()                                       # Cierra todas las ventanas de OpenCV