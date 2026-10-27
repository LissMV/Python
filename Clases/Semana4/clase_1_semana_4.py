#Clase 1, semana 4

#LISTAS#
#posiciones en la lista: pop, remove, append, insert, sort, reverse, count, index. Además, len() para saber la longitud de la lista 
# y las listas se cuentan desde 0, es decir, la primera posición es 0, la segunda es 1, la tercera es 2, etc.

#SISTEMA DE COLAS#
print("Bienvenido al sistema de colas del laboratorio de computación")

#Lista actual de mi sistema#
cola = ["Sofía", "Mateo", "Valeria"]
atendidos = 0
cancelados = 0

print(f"La cola actual es: {cola}")
print("menu")
print("1. Registrar estudiante regular")
print("2. Registrar estudiante prioritario")
print("3. Cancelar una solicitud")
print("4. Atender al siguiente estudiante")
print("5. Consultar la cola")
print("6. Cerrar el sistema")

opcion = int(input("Elija una opción (1 - 6): "))
while True:
    if opcion == 1:
        while True:
            estudiante = input("Nombre del estudiante (Ej. Juan): ")
            if estudiante in cola or estudiante == "":
                print("Error: el nombre no puede estar vacío o ya está en la cola.")
            else:
                cola.append(estudiante)
                print(f"La nueva cola es: {cola}")
                cancelados.append(estudiante)
                print(f"La cola de cancelados es: {cancelados}")
                break
    elif opcion == 2:
        while True:
            estudiante = input("Nombre del estudiante (Ej. Juan): ")
            if estudiante in cola or estudiante == "":
                print("Error: el nombre no puede estar vacío o ya está en la cola.")
            else:
                cola.insert(0, estudiante)
                print(f"La nueva cola es: {cola}")
                break
    elif opcion == 3:
        while True:
            estudiante = input("Nombre del estudiante a cancelar (Ej. Juan): ")
            if estudiante in cola or estudiante == "":
                cola.remove(estudiante)
                cancelados += 1
                print(f"{estudiante} ha sido eliminado de la cola.")
                print(f"La nueva cola es: {cola}")
            else:
                print(f"Error: {estudiante} no está en la cola.")
    elif opcion == 6:
        confirmacion = input("¿Está seguro de que desea cerrar el sistema? (S/N): ")
        if confirmacion.upper() == "S":
            print("El sistema se ha cerrado.")
            print(f"La lista actual es: {cola}")
            break