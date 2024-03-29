import ctypes
import cv2

classificador = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
camera = cv2.VideoCapture(0)
amostra = 1
numeroAmostras = 25
ctypes.windll.user32.MessageBoxW(0, "Serão capturadas 25 imagens suas para armazenamento, agora digite seu identificador", "Captura", 0)
id = input('Digite seu iden1tificador: ')
largura, altura = 220, 220
ctypes.windll.user32.MessageBoxW(0, 'Aperte a tecla "q" para capturar uma imagem', "Captura", 0)
print('Capturando as faces...')

while (True):
    conectado, imagem = camera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(100,100))

    for (x, y, l, a) in facesDetectadas:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (255, 0, 0), 2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            imagemFace = cv2.resize(imagemCinza[y: y + a, x: x + l], (largura, altura))
            cv2.imwrite('fotos/pessoa.' + str(id) + '.' + str(amostra) + '.jpg', imagemFace)
            print('[foto ' + str(amostra) + ' capturada com suceso]')
            amostra += 1

    cv2.imshow("Face", imagem)
    cv2.waitKey(1)
    
    if (amostra >= numeroAmostras + 1): 
        break

ctypes.windll.user32.MessageBoxW(0, "Faces capturadas com sucesso", "Captura", 0)
camera.release()
cv2.destroyAllWindows()