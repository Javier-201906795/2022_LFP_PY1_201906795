from enum import Enum
from lib2to3.pgen2 import token
import re

global tokensNumero


class L_tokens(Enum):
    TK_MENOR = "<"
    TK_E_NUMERO = "Numero"
    TK_MAYOR = ">"
    TK_NUMERO = "[0-9]*"
    TK_BARRAINV = "/"
    TK_E_OPERACION = "Operacion"
    TK_IGUAL = "="
    TK_OP_SUMA = "SUMA",
    TK_OP_RESTA = "RESTA"
    TK_E_TIPO = "Tipo"


tokensNumero = [
            L_tokens.TK_MENOR.value,    # <
            L_tokens.TK_E_NUMERO.value, # Numero
            L_tokens.TK_MAYOR.value,    # >
            L_tokens.TK_NUMERO.value,         # 10
            L_tokens.TK_MENOR.value,    # <
            L_tokens.TK_BARRAINV.value, # /
            L_tokens.TK_E_NUMERO.value, # Numero
            L_tokens.TK_MAYOR.value     # >
        ]




def Buscar(tipodetoken,texto):
    try:
        print("Buscando")

        if (tipodetoken == "NUMERO"):
            Bn = buscarnumero(texto)

            print("Se encontro un numero: ", Bn.get("estado"))
            print("numero: ", Bn.get("numero"))
            

    except Exception as e:
        print("Error en AccionesBusquedad.py| Buscar, ", tipodetoken, ". \n", e)





def buscarnumero(texto):
    try:
        print("Texto recivido: ", texto)
        cadena = texto
        columna = 0  
        numero = -999
        cont = 0

        #Recorre token numero en texto en busquead de concidencias
        for i in tokensNumero:
            
            #Configuracion de busquedad (Buscar el primer elemento con el valor del token)
            patron = re.compile(f'^{i}')
            
            
            try:
                #Busquedad en el texto
                s = patron.search(cadena)
                #Aumenta valor columna
                columna += int(s.end())
                #Guardar el TOKEN
                if (i == L_tokens.TK_NUMERO.value):
                    numero = s.group()
                #Quita el valor encontrado y crea una nueva cadena
                cadena = quitar(cadena, s.end())
            except Exception as e:
                print("No se encontro el valor buscado: ", e)
            
            
            
            print("i: ", i)
            print("s: ",s.group())
            print("cadena: ", cadena)

            



        return {"estado": True, "numero": numero}

    except Exception as e:
        print("Error en AccionesBusquedad.py| buscarnumero. ", " \n", e)
        return {"estado": False, "numero": -9999}
    




def quitar(cadena :str, _num : int):
    
    _tmp = ""
    count = 0
    #Quitar el valor encontrado y devolver el resto
    for i in cadena:
        if count >= _num:
            #Texto que es la cadena nueva
            _tmp += i
        else:
            pass
        count += 1
    
    return _tmp