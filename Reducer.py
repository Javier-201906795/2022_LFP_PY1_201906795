#╔══════════════════════════════════╗
#║ PROYECTO 1 LFP                   ║
#║ JAVIER  RICARDO YLLESCAS BARRIOS ║
#║ CARNE: 201906795                 ║
#╚══════════════════════════════════╝

#█┼┼┼┼┼┼┼┼┼┼┼[ IMPORTACIONES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
import Estado as estado1
import AccionesLectura as accL
import AccionesBusquedad as accB

#Iniciando la base de datos
global estado
estado = estado1.estado()

#█┼┼┼┼┼┼┼┼┼┼┼| Estado |┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
global texto, textolista, textoposicion



#█┼┼┼┼┼┼┼┼┼┼┼| REDUCER |┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
def reducer(instruccion):

    print("• ---------------------")
    print("• REDUX: ",instruccion)
    

    try:
        if (instruccion == "LEER_ARCHIVO"):
            print("• • Leyendo Archivo")

            arch = accL.leerarhivo()
            global texto, textolista, textoposicion
            texto = arch.get("texto")
            textolista = arch.get("lista")
            textoposicion = arch.get("posicion")

            
            print("• • •")
            print("Texto: \n" , texto)
            print("• • •")


        elif (instruccion == "ANALIZAR"):
            print("• • •")

            accB.Buscar("NUMERO",textolista[0])

        else:
            print("No se reconcio la instruccion")
    
    except Exception as e:
        print("Error REDUX: ", e)


