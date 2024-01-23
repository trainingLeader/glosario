opciones = ["1. Agregar palabra\n2. Buscar Palabra\n3. Borrar Palabra\n4. Salir"]
def MenuPrincipal()->int:
    titulo = """
        +++++++++++++++++++++++++++++++++++++++++
        +  DICCIONARIO TECNICO DE PROGRAMACION  +
        +++++++++++++++++++++++++++++++++++++++++
    """
    print(titulo)
    for item in opciones:
        print(item)
    op = int(input(":)_"))
    return op
    