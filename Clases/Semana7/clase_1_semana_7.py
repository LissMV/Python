#DICCIONARIOS# -- estructura mutable, funciona a partir de pares

diccionario = {'color': ['verde', 'cyan', 'naranja'], 'posicion': [9, 8, 7]}
#NOTA. En los diccionarios, cada llave/clave es un Item, este tiene 2
print(f"Es el color {diccionario['color'][0]} y también la posición {diccionario['posicion'][2]}")
    
alumno1 = ["0001","Carlos",19,True,['Artistica', 'Educación física']]
"""for i in range (2):
    materia = input("Digite la materia a agregar: ")
    alumno1[4].append(materia)
    """
print(alumno1[4])
#Diccionarios ordenados
#Los diccionarios no tienen indice, tienen llaves
prestamo = {
    'Estudiante': 'Ana',
    'Equipo': 'cargador',
    'Cantidad': 2,
    'Activio': True,
    'Materias': ['IDN', 'IDS', 'Proyecto Integrador', 'Negocios Digitales']
}
#print(type(prestamo))
#print(len(prestamo))
prestamo['Estudiante'] = "Mariana" #Una mutación

prestamo['Carnet'] = '20265381'
#.get funciona como una doble verificación, sí se le asigna un valor lo imprime, sino, imprime el comentario o none
print(prestamo.get('Carnet', "No tiene carnet asignado")) 

del prestamo['Cantidad']
print(prestamo.get('Cantidad', "No hay cantidad")) 

empleado = {}
empleado['id'] = input("Digite el ID: ")
empleado['nombre'] = input("Digite el nombre: ").strip().capitalize()
empleado['ingreso'] = input("Digite el año de ingreso: ")
hijos = int(input("Digite la cantidad de hijos: "))
if hijos > 0:
    empleado['hijos'] = []
    for h in range(hijos):
        empleado['hijos'].append(input("Digite el nombre del hijo: "))
    
print(empleado)