empleados = {
    "E003": {
        "nombre": "Carla", "departamento": "ventas", "hijos": ["Mía"]
    },
    "E001": {
            "nombre": "Ana", "departamento": "ventas", "hijos": ["Lucía", "Diego"]
    },
    "E002": {
            "nombre": "Luis", "departamento": "soporte", "hijos": [""]
    },
    "E004": {
            "nombre": "Javier", "departamento": "cobros", "hijos": ["Maria", "Mariana"]
    }
}

# Declarar la función para buscar empleado
def buscar_empleado(registros, codigo):
    #print(registros.get(codigo, "No hay un empleado con ese ID"))
    empleado = registros.get(codigo, "Empleado no encontrado")
    return empleado

print(buscar_empleado(empleados, "E001")["nombre"])