equipo = input("Equipo (laptop o tablet): ")
for i in range(3):
    if equipo == "laptop":
        print("Equipo permitido")
        print("Puede continuar")
        break
    else: 
        print("Equipo no permitido")
        print("No puede continuar")
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