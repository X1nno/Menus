from os import system
system("cls")
import time

Norte=[]
Pacifico=[]
Sur=[]
Andes=[]

def boleta(nombre,apellido,cantidad,sector,equipo,descto,descuento,total):
    print(f"""
            {equipo}
            
            Nombre: {nombre}
            Apellido: {apellido}
            Sector: {sector}
            Cantidad: {cantidad} entradas
            Descuento: {descto}%
            Total: {total}
            """)

def comprar():
    descto=0
    descuento=0
    comprar=input("""
            Sistema de compra de entradas:
            
            1-Galeria Norte(Barcelona)    6000
            2-Galeria Pacifico(Barcelona) 45000
            3-Galeria Sur(Real Madrid)    6000
            4-Galeria Andes(Real Madrid)  30000
            
            """)
    match comprar:
        case "1":
            nombre=input("Ingresa tu nombre: ")
            apellido=input("Ingresa apellido: ")
            cantidad=int(input("Ingresa cantidad de entradas: "))
            sector="Norte"
            equipo="Barcelona"
            codigo=input("Ingresa el codigo de descuento correspondiente: ")
            if codigo=="yosoydelbarca":
                print("Codigo aceptado con exito")
                descto=15
            else:
                print("Codigo no valido")
            if descto==15:
                subtotal=6000*cantidad
                descuento=subtotal*0.15
                total=subtotal-descuento
            else:
                total=6000*cantidad
            boleta(nombre,apellido,cantidad,sector,equipo,descto,descuento,total)
            Norte.append(cantidad)
        case "2":
            nombre=input("Ingresa tu nombre: ")
            apellido=input("Ingresa apellido: ")
            cantidad=int(input("Ingresa cantidad de entradas: "))
            sector="Pacifico"
            equipo="Barcelona"
            codigo=input("Ingresa el codigo de descuento correspondiente: ")
            if codigo=="yosoydelbarca":
                print("Codigo aceptado con exito")
                descto=15
            else:
                print("Codigo no valido")
            if descto==15:
                subtotal=45000*cantidad
                descuento=subtotal*0.15
                total=subtotal-descuento
            else:
                total=45000*cantidad
            boleta(nombre,apellido,cantidad,sector,equipo,descto,descuento,total)
            Pacifico.append(cantidad)
        case "3":
            nombre=input("Ingresa tu nombre: ")
            apellido=input("Ingresa apellido: ")
            cantidad=int(input("Ingresa cantidad de entradas: "))
            sector="Sur"
            equipo="Real Madrid"
            codigo=input("Ingresa el codigo de descuento correspondiente: ")
            if codigo=="yosoydelmadrid":
                print("Codigo aceptado con exito")
                descto=20
            else:
                print("Codigo no valido")
            if descto==20:
                subtotal=6000*cantidad
                descuento=subtotal*0.20
                total=subtotal-descuento
            else:
                total=6000*cantidad
            boleta(nombre,apellido,cantidad,sector,equipo,descto,descuento,total)
            Sur.append(cantidad)
        case "4":
            nombre=input("Ingresa tu nombre: ")
            apellido=input("Ingresa apellido: ")
            cantidad=int(input("Ingresa cantidad de entradas: "))
            sector="Andes"
            equipo="Real Madrid"
            codigo=input("Ingresa el codigo de descuento correspondiente: ")
            if codigo=="yosoydelmadrid":
                print("Codigo aceptado con exito")
                descto=20
            else:
                print("Codigo no valido")
            if descto==20:
                subtotal=30000*cantidad
                descuento=subtotal*0.20
                total=subtotal-descuento
            else:
                total=30000*cantidad
            boleta(nombre,apellido,cantidad,sector,equipo,descto,descuento,total)
            Andes.append(cantidad)
        case other:
            print("Opcion no valida")

def total_entradas():
    totalnorte=sum(Norte)
    totalpacifico=sum(Pacifico)
    totalsur=sum(Sur)
    totalandes=sum(Andes)
    print(f"""
            Resumen entradas vendidas por sector:
            
            Galeria Norte: {totalnorte}
            Galeria Pacifico: {totalpacifico}
            Galeria Sur: {totalsur}
            Galeria Andes: {totalandes}
            
            """)

#Menu
while True:
    opcion=input("""
                    Bienvenido al sistema de venta de entradas del Clasico
                    Elije opcion usando el numero al costado de cada una.
                    
                    1.Comprar
                    2.Ver Total de entradas vendidas por sector
                    
                    9.Salir
                    
                    """)
    match opcion:
        case "1":
            comprar()
        case "2":
            total_entradas()
        case "9":
            print("Saliendo del programa, gracias por su preferencia.....")
            time.sleep(1.5)
            break
        case other:
            print("Opcion no valida")