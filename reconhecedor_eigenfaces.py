import cv2

def getPessoa(id):
    nome = ''

    if id == 1:
        nome = 'Carlos'
    elif id == 2:
        nome = 'Pessoa 2'
    elif id == 3:
        nome = 'Pessoa 3'
    elif id == 4:
        nome = 'Pessoa 4'
    elif id == 5:
        nome = 'Zuzu'
    
    return nome


detectorFace = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
reconhecedor = cv2.face.EigenFaceRecognizer_create()
reconhecedor.read("treinamento/classificadorEigen.yml")
largura, altura = 220, 220
font = cv2.FONT_HERSHEY_COMPLEX_SMALL

camera = cv2.VideoCapture(0)

while (True):
    conectado, imagem = camera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesDetectadas = detectorFace.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(30,30))

    for (x, y, l, a) in facesDetectadas:
        imagemFace = cv2.resize(imagemCinza[y: y + a, x: x + l], (largura, altura))
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (255, 0, 0), 2)
        id, confianca = reconhecedor.predict(imagemFace)

        cv2.putText(imagem, getPessoa(id), (x, y + (a + 30)), font, 2, (255, 0, 0))
        cv2.putText(imagem, str("{:.2f}".format(confianca)), (x, y + (a + 50)), font, 1, (0, 0, 255))
        print(id)

    cv2.imshow("Face", imagem)
    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()

