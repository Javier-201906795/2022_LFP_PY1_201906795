from enum import Enum
from lib2to3.pgen2 import token
import re

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




class Analizador:
    #Variable globales
    def __init__(self):
        self.cadena = ""
        self.linea = 0
        self.columna = 0  
        self.lista_cadena = []
        self.tmp_cadena = ""
    

    def quitar(self, _cadena :str, _num : int):
        
        _tmp = ""
        count = 0
        #Quitar el valor encontrado y devolver el resto
        for i in _cadena:
            if count >= _num:
                #Texto que es la cadena nueva
                _tmp += i
            else:
                #Guardar y concatena en cadena (para compararlos en aumentar linea)
                #Guarda valores encontrados
                self.tmp_cadena += i 
            count += 1
        
        return _tmp

    def aumentarLinea(self):
        print("---------Aumenta Linea---------")
        _tmp = self.lista_cadena[self.linea]
        print("temp:",_tmp , " == tempcadena:", self.tmp_cadena)
        if _tmp == self.tmp_cadena:
            #Seguir contando Lineas
            self.linea += 1
            #Reiniciar valores
            self.tmp_cadena = ""
            self.columna = 0 
            print("igual: linea:",self.linea, "|cadenatmp",self.tmp_cadena,"|columna",self.columna)

    def Numero(self, _cadena : str):
        tokens = [
            L_tokens.TK_MENOR.value,    # <
            L_tokens.TK_E_NUMERO.value, # Numero
            L_tokens.TK_MAYOR.value,    # >
            L_tokens.TK_NUMERO.value,         # 10
            L_tokens.TK_MENOR.value,    # <
            L_tokens.TK_BARRAINV.value, # /
            L_tokens.TK_E_NUMERO.value, # Numero
            L_tokens.TK_MAYOR.value     # >
        ]
        _numero = ""

        for i in tokens:
            try:
                print("°°°°°Numero°°°°°°°°")
                print("item: [",i,"] Cadena: ",_cadena)
                #BUSCADOR
                #Configuracion de busquedad
                patron = re.compile(f'^{i}')
                #Busquedad del texto
                s = patron.search(_cadena)
                #Aumenta valor columna
                self.columna += int(s.end())
                #Guardar el TOKEN
                if (i == L_tokens.TK_NUMERO.value):
                    _numero = s.group()
                #Imprimir busquedad
                print("Busquedad resultado |Linea: ", self.linea," |Columna: ", self.columna," |Item: ", s.group())
                #Quita el valor encontrado y crea una nueva cadena
                _cadena = self.quitar(_cadena, s.end())
                #
                self.aumentarLinea()
                #
                print("NUMERO: ",_numero)
                
            except:
                print("Ocurrio un Error")
                print("Error: Lexema: ", _cadena[0:1],"| Tipo: Error | Columna: ", self.columna," | Fila: ", self.linea)
                #Reptir proceso y seguir
                

        return {'resultado':_numero, "cadena":_cadena, "Error": False}
            

    def compile(self):
        # LEEMOS EL ARCHIVO DE ENTRADA
        archivo = open("entradatest.txt", "r")
        contenido = archivo.readlines()
        archivo.close()

        

        # LIMPIAR MI ENTRADA
        nueva_cadena = ""
        lista_cadena = []

        

        for i in contenido:
            i = i.replace(' ', '') #QUITANDO ESPACIOS
            i = i.replace('\n', '') # QUITANDO SALTOS DE LINEA
            if i != '':
                nueva_cadena += i
                lista_cadena.append(i)

        print("||||[ CADENA ]||||||")
        print(nueva_cadena)
        print("||||[ LISTA CADENA ]|||||||")
        print(lista_cadena)
        self.lista_cadena = lista_cadena
        print("|||||||||||||||||||||||")

        
        print(self.Numero(nueva_cadena))


Analizador().compile()
