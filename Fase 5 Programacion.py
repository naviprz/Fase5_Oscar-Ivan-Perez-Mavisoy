def obtener_datos_equipo(n):
    matriz = []
    print(f"--- Registro de horas para {n} empleados ---")
    for i in range(n):
        print(f"\nEmpleado #{i+1}:")
        nombre = input("Nombre del recurso: ")
        # Solicitamos las horas de lunes a viernes
        horas = []
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        for dia in dias:
            h = float(input(f"Horas trabajadas el {dia}: "))
            horas.append(h)
        
        # Guardamos en la matriz: [Nombre, h1, h2, h3, h4, h5]
        matriz.append([nombre] + horas)
    return matriz

def procesar_reporte(matriz, umbral=40):
    print("\n" + "="*45)
    print(f"{'Nombre':<10} | {'Total':<8} | {'Clasificación'}")
    print("-"*45)
    
    for fila in matriz:
        nombre = fila[0]
        total_horas = sum(fila[1:])
        
        if total_horas > umbral:
            clasificacion = "Sobretiempo"
        else:
            clasificacion = "Horario Estándar"
            
        print(f"{nombre:<10} | {total_horas:<8} | {clasificacion}")

# --- Ejecución del programa ---
try:
    cantidad = int(input("¿Cuántos empleados desea registrar? "))
    datos = obtener_datos_equipo(cantidad)
    procesar_reporte(datos)
except ValueError:
    print("Error: Por favor, ingrese valores numéricos válidos para las horas.")
