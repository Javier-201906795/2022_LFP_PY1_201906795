


def leerarhivo():
    try:
        archivo = open("entrada.txt", "r")
        contenido = archivo.readlines()
        archivo.close()

        texto_archivo = ""
        lista_archivo = []

        

        for i in contenido:
            i = i.replace(' ', '') #QUITANDO ESPACIOS
            i = i.replace('\n', '') # QUITANDO SALTOS DE LINEA
            if i != '':
                texto_archivo += i
                lista_archivo.append(i)
        
        
        return {"texto": texto_archivo, "lista": lista_archivo}
    
    except Exception as e:
        print(e)