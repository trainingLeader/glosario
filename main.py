import modulos.ui.menu as m
import modulos.glosario as g
import os
glosario = {
    "A" :{
    },
    "B" :{},
    "C" :{},
    "D" :{},
    "E" :{},
    "F" :{}
}
isActive = True
while isActive:
    os.system('cls')
    op = m.MenuPrincipal()
    if (op == 1):
        g.AddWord(glosario)
        print(glosario)
        os.system('pause')
    elif (op == 2):
        pass
    elif (op == 3):
        pass
    elif (op == 4):
        isActive = False
    else:
        os.system('cls')
        print("La opcion ingresada es invalida.....")
        os.system('pause')