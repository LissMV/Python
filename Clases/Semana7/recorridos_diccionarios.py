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
buscar_empleado = input("Digite el codigo del empleado que desea buscar: ")
print(empleados[buscar_empleado])

for i, j in empleados.items():
    if j["departamento"].lower() == "ventas":
        print(f"El empleado {i} con combre {j["nombre"]} tiene {len(j["hijos"])}") 