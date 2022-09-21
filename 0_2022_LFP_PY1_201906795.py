#╔══════════════════════════════════╗
#║ PROYECTO 1 LFP                   ║
#║ JAVIER  RICARDO YLLESCAS BARRIOS ║
#║ CARNE: 201906795                 ║
#╚══════════════════════════════════╝

#█┼┼┼┼┼┼┼┼┼┼┼[ IMPORTACIONES ]┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
import Reducer as redux

#█┼┼┼┼┼┼┼┼┼┼┼| MAIN |┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼█
if __name__ == '__main__':

    print("Bienvenidos")

    #Leer archivo y guardarlo en una lista
    redux.reducer("LEER_ARCHIVO")

    #Identifacar <Operaciones>
    redux.reducer("IDENTIFICAR_TIPO")
