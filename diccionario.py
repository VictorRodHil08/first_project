import time
#Diccionario
meme_dict = {"CREEPY": "aterrador, siniestro", 
            "Concho": "Taxi para diversas personas",
            "Coro": "Grupo de gente/amigos",
            "Cualto": "Dinero",
            "Pariguayo": "Gente que cree que sabe mas que uno"
            }
#Saludo
print("Saludos pana")
time.sleep(1)
#bucle
for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

    if word in meme_dict.keys():
        # ¿Qué debemos hacer si se encuentra la palabra?
        print(meme_dict[word])
        time.sleep(2)
    else:
        # ¿Qué hacer si no se encuentra la palabra?
        print("Esa palabra no esta brother.")
