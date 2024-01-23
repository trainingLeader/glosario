import os
def AddWord(dataSource : dict):
    letra = input("Ingrese la letra Indice :").upper()
    data = dataSource.get(letra)
    palabra = input("Ingrese la palabra :")
    significado = input("Ingrese significado")
    word ={
        "palabra":  palabra,
        "significado": significado
    }
    data.update({len(data)+1:word})

