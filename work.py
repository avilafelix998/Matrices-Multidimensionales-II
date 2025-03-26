# Función para mostrar el menú de opciones
def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Ingresar nueva persona")
    print("2. Mostrar todos los datos")
    print("3. Filtrar por DNI")
    print("4. Salir")

# Función para ingresar una nueva persona
def ingresar_persona():
    # Solicitar el nombre, apellido, DNI, teléfonos e hijos al usuario
    nombre = input("Ingresa el nombre: ")
    apellido = input("Ingresa el apellido: ")
    dni = input("Ingresa el DNI: ")
    
    # Ingresar los teléfonos como una cadena separada por comas, luego convertirlos en una lista
    telefonos = input("Ingresa los teléfonos separados por comas: ").split(",")
    
    # Ingresar los hijos como una cadena separada por comas, luego convertirlos en una lista
    hijos = input("Ingresa los nombres de los hijos separados por comas: ").split(",")
    
    # Limpiar los espacios en blanco extra alrededor de cada teléfono e hijo
    telefonos = [telefono.strip() for telefono in telefonos]
    hijos = [hijo.strip() for hijo in hijos]
    
    # Retornar los datos como una lista con la estructura solicitada
    return [nombre, apellido, dni, telefonos, hijos]

# Función para mostrar todos los datos ingresados
def mostrar_datos(personas):
    # Verificar si la lista de personas está vacía
    if not personas:
        print("No hay datos para mostrar.")
        return
    
    # Mostrar los datos de cada persona en la lista
    print("\nDatos ingresados:")
    for persona in personas:
        # Desempaquetar los datos de la persona
        nombre, apellido, dni, telefonos, hijos = persona
        # Mostrar la cantidad de teléfonos e hijos, en lugar de los datos completos
        print(f"{nombre} {apellido}, DNI: {dni}, Teléfonos: {len(telefonos)} teléfono(s), Hijos: {len(hijos)}")

# Función para filtrar por DNI y mostrar los datos de la persona encontrada
def filtrar_por_dni(personas):
    # Solicitar el DNI para realizar la búsqueda
    dni_buscado = input("\nIngresa el DNI para filtrar: ")
    
    # Buscar la persona por el DNI en la lista de personas
    for persona in personas:
        # Desempaquetar los datos de la persona
        nombre, apellido, dni, telefonos, hijos = persona
        # Si el DNI de la persona coincide con el DNI buscado, mostrar los datos
        if dni == dni_buscado:
            print(f"\nDatos de {nombre} {apellido}:")
            print(f"DNI: {dni}, Teléfonos: {len(telefonos)} teléfono(s), Hijos: {len(hijos)}")
            return
    
    # Si no se encuentra una persona con ese DNI, mostrar un mensaje de error
    print("No se encontró una persona con ese DNI.")

# Función principal que controla la ejecución del programa
def main():
    # Lista para almacenar las personas ingresadas
    personas = []
    
    # Bucle principal que mantiene el programa en ejecución hasta que el usuario decida salir
    while True:
        # Mostrar el menú de opciones
        mostrar_menu()
        # Solicitar la opción elegida por el usuario
        opcion = input("Elige una opción: ")
        
        # Evaluar la opción seleccionada por el usuario
        if opcion == "1":
            # Opción 1: Ingresar una nueva persona
            persona = ingresar_persona()  # Llamar a la función para ingresar los datos
            personas.append(persona)  # Agregar los datos ingresados a la lista de personas
        elif opcion == "2":
            # Opción 2: Mostrar todos los datos
            mostrar_datos(personas)  # Llamar a la función para mostrar los datos
        elif opcion == "3":
            # Opción 3: Filtrar por DNI
            filtrar_por_dni(personas)  # Llamar a la función para buscar por DNI
        elif opcion == "4":
            # Opción 4: Salir del programa
            print("Gracias por usar el programa.")
            break  # Terminar el ciclo y salir del programa
        else:
            # Si el usuario ingresa una opción no válida
            print("Opción no válida, por favor elige una opción del 1 al 4.")

# Iniciar la ejecución del programa
if __name__ == "__main__":
    main()  # Llamar a la función principal para comenzar el programa
