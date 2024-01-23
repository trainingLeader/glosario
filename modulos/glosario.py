import os
def AddWord(dataSource : dict):
    word = input("Ingrese la palabra :").upper()
    if word[0:1] != ' ':
        if (dataSource.get(word[0:1],-1)):
            dataSource.update({word[0:1]:{}})
        #key = str(word).replace(' ','') 
        data = dataSource.get(word[0:1])
        significado = input("Ingrese significado")
        wordAdd ={
            "palabra":  word,
            "significado": significado
        }
        data.update({word:wordAdd})
    else:
        print("El primer caracter no puede ser en blanco")
        os.system('pause')

def DelWord(dataSource : dict):
    palabra=(input("Por favor ingresa la palabra que quiere borrar: ")).upper()
    dataSource.get(palabra[0:1]).pop(palabra)


def SeachWord(dataSource : dict):
    palabra=(input("ingresa la palabra que desea buscar: ")).upper()
    print(dataSource.get(palabra[0:1]).get(palabra)["significado"])
    os.system('pause')


