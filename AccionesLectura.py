


def leerarhivo():
    try:
        archivo = open("entrada.txt", "r")
        contenido = archivo.readlines()
        archivo.close()

        texto_archivo = ""
        lista_archivo = []

        
        #Obtiene el texto y un listado de archivos
        for i in contenido:
            i = i.replace(' ', '') #QUITANDO ESPACIOS
            # i = i.replace('\n', '') # QUITANDO SALTOS DE LINEA
            if i != '':
                texto_archivo += i
                lista_archivo.append(i)

        #Obtiene el texto 
        textonormal = ""
        for i in contenido:
            textonormal += i 


        #Listado con posicion de los espacios
        listaposicion = []
        for i in contenido:
            #Contar espacios
            contespacios = 0
            for j in i:
                if (j == ' '):
                    contespacios += 1
            #agregar Espacio encontrados
            listaposicion.append(contespacios)
        

        
        return {"texto": textonormal,"textosinespacios": texto_archivo, "lista": lista_archivo, "posicion": listaposicion}
    
    except Exception as e:
        print("Error AccionesLectura.py: ",e)