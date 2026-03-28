estudiante = {
    "nombre": "Marco",
    "apellido": "Alpírez",
    "sexo": "M",
    "edad": 25,
    "estado_civil": "Soltero",
    "habilidades": ["Python", "MATLAB", "Circuitos"],
    "pais": "México",
    "ciudad": "Veracruz",
    "direccion": "Topacio 186"
}

cantidad_letras = len(estudiante)
print("La longitud del diccionario es: ",cantidad_letras)

print(estudiante["habilidades"])
print(type(estudiante["habilidades"]))

estudiante["habilidades"].append("SolidWorks")
estudiante["habilidades"].append("Autocad")
print(estudiante["habilidades"])

claves = list(estudiante.keys())
print(claves)

valores = list(estudiante.values())
print(valores)

tuplas = list(estudiante.items())
print(tuplas)

estudiante.pop("edad") 
print(estudiante)

