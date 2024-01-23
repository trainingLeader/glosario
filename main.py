import modulos.ui.menu as m
import modulos.glosario as g
import os
glosario = {

}
isActive = True
while isActive:
    os.system('cls')
    op = m.MenuPrincipal()
    if (op == 1):
        g.AddWord(glosario)
    elif (op == 2):
        g.SeachWord(glosario)
    elif (op == 3):
        g.DelWord(glosario)
    elif (op == 4):
        isActive = False
    else:
        os.system('cls')
        print("La opcion ingresada es invalida.....")
        os.system('pause')