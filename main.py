for i in range(5):
    import random
    
    meme_dict = {
                "CRINGE": "Algo excepcionalmente raro o embarazoso",
                "LOL": "Una respuesta común a algo gracioso",
                "XD": "Risa",
                "Melo":"genial, bueno",
                "Parcero": "Amigo o conocido",
                "GUAYABA": "Una fruta"
                }
    
    palabra = input("¿Qué palabra no entiendes?")
    
    if palabra in meme_dict:
        print(palabra+ ":", meme_dict[palabra] )
    else:
        print("No tengo la definición de esa palabra, pero te muestro otra:")
        clave = random.choice( meme_dict.keys() )
        print(clave+ ":", meme_dict[clave] )
