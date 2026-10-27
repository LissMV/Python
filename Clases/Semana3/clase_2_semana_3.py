#Clase 2, semana 3

#CONDICIONALES#
#Ejercicio 1: solicitud de beca

nombre = input("Nombre completo: ")
promedio = float(input("Promedio: "))

if promedio >= 0 and promedio <= 10:
    ingreso_mensual = float(input("Ingreso mensual familiar: "))
    if ingreso_mensual > 0: 
        materias_reprobadas = int(input("Materias reprobadas:"))
        if materias_reprobadas >= 0: 
            is_active = input("¿Está activo en la institución? (S/N): ")
            if is_active == "S":
                if promedio >= 9 and ingreso_mensual <= 500 and materias_reprobadas == 0:
                    print("Tienes beca completa")
                elif promedio >= 9 and ingreso_mensual <= 1000 and materias_reprobadas <= 1:
                    print("Tienes beca parcial")
                elif promedio >= 8 and ingreso_mensual <= 800 and materias_reprobadas <= 1:
                    print("Tienes beca parcial")
                else:
                    print(f"{nombre} no cumple con los requisitos para la beca")
            elif is_active == "N":
                print(f"{nombre} no está activo en la institución")
else:
    print("Promedio no válido")
    
    
    
    
#ingreso_mensual = ("Ingreso mensual familiar: ")
#materias_reprobadas = int(input("Materias reprobadas:"))
#is_active = input('')

#if materias_reprobadas == 1:
    
    
