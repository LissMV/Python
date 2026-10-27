#Clase 1, semana 3

#VARIABLES#

#forma de interactuar con la computadora es CLI (command, line, interface)
#GUI (graphic, user, interface) 

#Int es capaz de recibir un input y convertirlo a un entero (casting)
edad_alumno = int(input("Digite la edad del alumno: "))
mayoria_edad = 18
adulto = edad_alumno > mayoria_edad

#f es capaz de recibir variables y mostrarlas en un string
print(f"La edad del alumno es: {edad_alumno}")

#-----------------------------------------------------------------------------------
#CONDICIONALES#

equipo = input("Equipo (laptop o tablet): ")

if equipo == "laptop":
    horas = int(input("horas: "))
    if horas < 0:
        print("Solo valores positivos")
    elif horas <= 2:
        print("Pocas horas de uso")
    elif horas <= 5:
        print("Normal")    
    elif horas <= 8:
        print("Mucho")
    else:
        print("No aplica")
else: 
    print("Equipo no permitido")
#print(equipo == "Laptop")