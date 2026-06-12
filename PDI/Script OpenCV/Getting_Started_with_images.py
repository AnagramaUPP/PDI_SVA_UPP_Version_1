import cv2                                              # Importa la biblioteca OpenCV

img = cv2.imread("../Images/madrid.png", 0)            # Lee la imagen en escala de grises

cv2.imshow("Figure1", img)                     # Muestra la imagen en una ventana llamada "Figure1"

k = cv2.waitKey(0)                                     # Espera una tecla y guarda su código ASCII

if k == 27:                                            # Si se presiona la tecla ESC
    cv2.destroyAllWindows()                            # Cierra todas las ventanas de OpenCV

elif k == ord('s') & 0xff:                             # Si se presiona la tecla 's'
    cv2.destroyAllWindows()                            # Cierra todas las ventanas
    print('salvando imagen')                           # Muestra mensaje de guardado
    print(img.shape)                                   # Muestra las dimensiones de la imagen
    cv2.imwrite("../Created_Images/madridgray.png",img)     # Guarda la imagen en disco