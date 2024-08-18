from os import system
system("cls")
import re


# Lista de las zapatillas
zapatillas = [
    {"nombre": "Nike Air Max", "precio": 120, "disponible": True},
    {"nombre": "Adidas Ultraboost", "precio": 150, "disponible": True},
    {"nombre": "Puma Suede", "precio": 90, "disponible": True}
]

# Lista de compras realizadas
compras = []

def validar_nombre(nombre):
    """Valida que el nombre solo contenga letras y espacios."""
    return bool(re.match(r'^[a-zA-Z\s]+$', nombre))

def validar_rut(rut):
    """Valida que el RUT esté en un formato correcto (simple)."""
    return bool(re.match(r'^\d{7,8}-[\dkK]$', rut))

def validar_cantidad(cantidad):
    """Valida que la cantidad sea un número entero positivo."""
    return cantidad.isdigit() and int(cantidad) > 0

def solicitar_datos_usuario():
    """Solicita y valida el nombre y el RUT del usuario."""
    while True:
        nombre = input("Ingresa tu nombre: ").strip()
        if not validar_nombre(nombre):
            print("Nombre inválido. Solo se permiten letras y espacios.")
            continue

        rut = input("Ingresa tu RUT: ").strip()
        if not validar_rut(rut):
            print("RUT inválido. Debe estar en el formato correcto (ej: 12345678-9).")
            continue
        
        return nombre, rut

def mostrar_zapatillas(zapatillas):
    """Muestra todas las zapatillas con su estado de disponibilidad."""
    print("Zapatillas disponibles:")
    for idx, zapatilla in enumerate(zapatillas):
        estado = "Disponible" if zapatilla["disponible"] else "No disponible"
        print(f"{idx}. {zapatilla['nombre']} - ${zapatilla['precio']} - {estado}")

def seleccionar_zapatilla(zapatillas):
    """Permite al usuario seleccionar una zapatilla disponible."""
    while True:
        try:
            zapatilla_id = int(input("Selecciona el número de la zapatilla que deseas comprar: "))
            if zapatilla_id < 0 or zapatilla_id >= len(zapatillas):
                print("Selección inválida. Inténtalo de nuevo.")
                continue
            
            if not zapatillas[zapatilla_id]["disponible"]:
                print("Lo siento, esa zapatilla ya ha sido comprada.")
                continue
            
            return zapatilla_id
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

def solicitar_cantidad():
    """Solicita y valida la cantidad de zapatillas que el usuario desea comprar."""
    while True:
        cantidad = input("¿Cuántas zapatillas deseas comprar?: ").strip()
        if not validar_cantidad(cantidad):
            print("Cantidad inválida. Debe ser un número entero positivo.")
            continue
        
        return int(cantidad)

def procesar_compra(nombre, rut, zapatilla_id, cantidad):
    """Procesa la compra, marca la zapatilla como no disponible y registra la compra."""
    zapatillas[zapatilla_id]["disponible"] = False
    precio_total = zapatillas[zapatilla_id]['precio'] * cantidad
    compra = {
        "nombre": nombre,
        "rut": rut,
        "zapatilla_id": zapatilla_id,
        "cantidad": cantidad,
        "precio_total": precio_total
    }
    compras.append(compra)
    generar_boleta(compra)

def generar_boleta(compra):
    """Genera y muestra una boleta de la compra realizada."""
    zapatilla = zapatillas[compra["zapatilla_id"]]
    print("\n--- BOLETA DE COMPRA ---")
    print(f"Nombre del cliente: {compra['nombre']}")
    print(f"RUT: {compra['rut']}")
    print(f"Producto: {zapatilla['nombre']}")
    print(f"Cantidad: {compra['cantidad']}")
    print(f"Precio Unitario: ${zapatilla['precio']}")
    print(f"Total: ${compra['precio_total']}")
    print("------------------------\n")

def ver_compras(rut, compras, zapatillas):
    """Muestra las compras realizadas por un usuario."""
    print(f"Compras para el RUT: {rut}")
    user_compras = [compra for compra in compras if compra["rut"] == rut]
    
    if not user_compras:
        print("No has realizado ninguna compra.")
        return
    
    for compra in user_compras:
        zapatilla_id = compra["zapatilla_id"]
        zapatilla = zapatillas[zapatilla_id]
        print(f"- Nombre del cliente: {compra['nombre']} - Zapatilla Comprada: {zapatilla['nombre']} - Cantidad: {compra['cantidad']} - Total: ${compra['precio_total']}")

def ejecutar_menu():
    """Muestra el menú principal y ejecuta la opción seleccionada por el usuario."""
    while True:
        print("\nMenú Principal")
        print("a. Ver todas las zapatillas")
        print("b. Comprar zapatillas")
        print("c. Ver mis compras")
        print("d. Salir")
        
        opcion = input("Selecciona una opción: ").lower()
        
        if opcion == "a":
            mostrar_zapatillas(zapatillas)
        elif opcion == "b":
            nombre, rut = solicitar_datos_usuario()
            mostrar_zapatillas(zapatillas)
            zapatilla_id = seleccionar_zapatilla(zapatillas)
            cantidad = solicitar_cantidad()
            procesar_compra(nombre, rut, zapatilla_id, cantidad)
        elif opcion == "c":
            rut = input("Ingresa tu RUT: ")
            ver_compras(rut, compras, zapatillas)
        elif opcion == "d":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecutor del codigo
if __name__ == "__main__":
    ejecutar_menu()
