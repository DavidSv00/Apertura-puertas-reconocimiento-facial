from deepface import DeepFace

obj = DeepFace.analyze (img_path = "/home/david/Documents/GitHub/Apertura-puertas-reconocimiento-facial/deepfaces/Faces/face-generated.jpg", actions = ['age', 'gender', 'race', 'emotion'])


print ("El resultado del analisis es: ")
print (obj)