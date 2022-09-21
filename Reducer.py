#╔══════════════════════════════════╗
#║ PROYECTO 1 LFP                   ║
#║ JAVIER  RICARDO YLLESCAS BARRIOS ║
#║ CARNE: 201906795                 ║
#╚══════════════════════════════════╝

#█┼┼┼┼┼┼┼┼┼┼┼[ IMPORTACIONES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
import Estado as estado1
import AccionesLectura as accL

#Iniciando la base de datos
global estado
estado = estado1.estado()


#█┼┼┼┼┼┼┼┼┼┼┼| REDUCER |┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
def reducer(instruccion):

    print("• ---------------------")
    print("• REDUX: ",instruccion)
    

    try:
        if (instruccion == "LEER_ARCHIVO"):
            print("• • Leyendo Archivo")
            arh = accL.leerarhivo()
            print("• • •")
            print("Texto: " ,arh["texto"])
            print("• • •")
            print("Lista: " ,arh["lista"])
            print("• • •")
        else:
            print("No se reconcio la instruccion")
    
    except Exception as e:
        print("Error REDUX: ", e)


