# Importar Bilbioteca
from deepface import DeepFace
import pandas as pd

# Buscar Rostro
print ("Buscando rostro")

# df = DeepFace.find(img_path = "img1.jpg", db_path = "C:/workspace/my_db")
df = DeepFace.find (img_path = "//home/david/Documents/GitHub/Apertura-puertas-reconocimiento-facial/deepfaces/Faces/diego-luna.jpg", db_path = "/home/david/Documents/GitHub/Apertura-puertas-reconocimiento-facial/deepfaces/my_db", enforce_detection = "false")
print ("Resultado ")
print (df)
print ("Imagen de mayor similitud")
print (df.identity[0])
print("Imagen de similitud secundaria")
print(df.identy[1])
