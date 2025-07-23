import sys

# Lista de nombres de estudiantes
listaEstudiante = ["Ashly", "Jeferson", "Jeirel", "Kianny", "Scarlette", "Kim", "Mari", "Luis"]

# Tupla de materias
materias = ("Programacion", "Bases de datos", "Ingles", "Calculo", "Cocina I", "Derecho Penal")

#Diccionarios
estudianteUno = {
    "nombre": "Ashly",
    "edad": 17,
    "carrera": "Derecho",
    "calificaciones": {
        "Programacion": 90,
        "Derecho Penal": 100,
        "Ingles": 80,
        "Calculo": 100
    }
}
estudianteDos = {
    "nombre": "Jeferson",
    "edad": 19,
    "carrera": "Informatica Empresarial",
    "calificaciones": {
        "Programacion": 90,
        "Bases de datos": 85,
        "Ingles": 80,
        "Calculo": 100
    }
}
estudianteTres = {
    "nombre": "Jeirel",
    "edad": 7,
    "carrera": "Medicina",
    "calificaciones": {
        "Programacion": 90,
        "Bases de datos": 85,
        "Ingles": 80,
        "Calculo": 100
    }
}
estudianteCuatro = {
    "nombre": "Kianny",
    "edad": 20,
    "carrera": "Informatica Empresarial",  
    "calificaciones": {
        "Programacion": 90,
        "Bases de datos": 85,
        "Ingles": 80,
        "Calculo": 100
    }  
}
estudianteCinco = {
    "nombre": "Scarlette",
    "edad": 20,
    "carrera": "Informatica Empresarial",
    "calificaciones": {
        "Programacion": 90,
        "Bases de datos": 85,
        "Ingles": 80,
        "Calculo": 100
    }
}
estudianteSeis = {
    "nombre": "Kim",
    "edad": 38,
    "carrera": "Educacion Español",
    "calificaciones": {
        "Programacion": 90,
        "Bases de datos": 85,
        "Ingles": 80,
        "Calculo": 100
    }
}
estudianteSiete = {
    "nombre": "Mari",
    "edad": 56,
    "carrera": "Chef",
    "calificaciones": {
        "Programacion": 90,
        "Bases de datos": 85,
        "Ingles": 80,
        "Calculo": 100
    }
}
estudianteOcho = {
    "nombre": "Luis",
    "edad": 64,
    "carrera": "Maestro de obras",
    "calificaciones": {
        "Programacion": 90,
        "Bases de datos": 85,
        "Ingles": 80,
        "Calculo": 100
    }
}

estudiantes = [estudianteUno, estudianteDos, estudianteTres, estudianteCuatro,
               estudianteCinco, estudianteSeis, estudianteSiete, estudianteOcho]

for estudiante in estudiantes:
    total = 0
    cantidad = 0
    for materia in estudiante["calificaciones"]:
        total += estudiante["calificaciones"][materia]
        cantidad += 1
    promedio = total / cantidad
    estudiante["promedio"] = promedio

for estudiante in estudiantes:
    promedio = estudiante["promedio"]
    if promedio >= 90:
        estudiante["rendimiento"] = "excelente"
    elif promedio >= 80:
        estudiante["rendimiento"] = "bueno"
    elif promedio >= 70:
        estudiante["rendimiento"] = "regular"
    elif promedio >= 60:
        estudiante["rendimiento"] = "riesgo academico"
    else:
        estudiante["rendimiento"] = "reprobado"

estudiantesPerfectos = set()
for estudiante in estudiantes:
    for materia in estudiante["calificaciones"]:
        if estudiante["calificaciones"][materia] == 100:
            estudiantesPerfectos.add(estudiante["nombre"])
            break

while True:
    print("1. Ver información de un estudiante específico")
    print("2. Mostrar estadísticas generales del curso")
    print("3. Listar estudiantes por categoría de rendimiento")
    print("4. Salir")
    
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        while True:
            nombreBuscar = input("Digite el nombre del estudiante")
           
            encontrado = False
            for estudiante in estudiantes:
                if estudiante["nombre"].lower() == nombreBuscar.lower():
                    print("\nNombre:", estudiante["nombre"])
                    print("Edad:", estudiante["edad"])
                    print("Carrera:", estudiante["carrera"])
                    print("Calificaciones:", estudiante["calificaciones"])
                    print("Promedio:", estudiante["promedio"])
                    print("Rendimiento:", estudiante["rendimiento"])
                    encontrado = True
                    break
            if not encontrado:
                print("Estudiante no encontrado. Intente de nuevo.")

    elif opcion == "2":
        sumaTotal = 0
        mejorPromedio = -1
        peorPromedio = 101
        mejorNombre = ""
        peorNombre = ""

        for estudiante in estudiantes:
            sumaTotal += estudiante["promedio"]
            if estudiante["promedio"] > mejorPromedio:
                mejorPromedio = estudiante["promedio"]
                mejorNombre = estudiante["nombre"]
            if estudiante["promedio"] < peorPromedio:
                peorPromedio = estudiante["promedio"]
                peorNombre = estudiante["nombre"]
        
        promedioGeneral = sumaTotal / len(estudiantes)
        print("\nCantidad total de estudiantes:", len(estudiantes))
        print("Promedio general del curso:", promedioGeneral)
        print("Estudiante con mejor promedio:", mejorNombre, "-", mejorPromedio)
        print("Estudiante con menor promedio:", peorNombre, "-", peorPromedio)
        print("Estudiantes con nota perfecta (100):", estudiantesPerfectos)

        excelente = 0
        bueno = 0
        regular = 0
        riesgo = 0
        reprobado = 0

        for estudiante in estudiantes:
            if estudiante["rendimiento"] == "excelente":
                excelente += 1
            elif estudiante["rendimiento"] == "bueno":
                bueno += 1
            elif estudiante["rendimiento"] == "regular":
                regular += 1
            elif estudiante["rendimiento"] == "riesgo":
                riesgo += 1
            else:
                reprobado += 1
        
        print("Estudiantes en cada categoría:")
        print("Excelente:", excelente)
        print("Bueno:", bueno)
        print("Regular:", regular)
        print("Riesgo académico:", riesgo)
        print("Reprobado:", reprobado)

    elif opcion == "3":
        for estudiante in estudiantes:
            print("\nNombre:", estudiante["nombre"])
            print("Promedio:", estudiante["promedio"])
            print("Rendimiento:", estudiante["rendimiento"])

            if estudiante["promedio"] >= 90:
                print("Felicidades!")
            elif estudiante["promedio"] >= 80:
                print("Buen desempeño, sigue así.")
            elif estudiante["promedio"] >= 70:
                print("Vas superrr, seguí esforzándote")
            else:
                print("Debes mejorar tu rendimiento:(")

    elif opcion == "4":
        print("Saliendo del programa, byes")
        sys.exit()

    else:
        print("Opción no válida, intenta de nuevo")
