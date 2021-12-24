from datetime import datetime
import sys
import os
def inicio():
    while True:   
        print("""
            [1] PEN
            """)
        moneda=str(input("[*] Ingrese el tipo de dinero: "))
        if moneda=="1":
            os.system("cls")
            break
        else:      
            print("Opcion Incorrecto, ingrese nuevamente..")
            os.system("cls")        
    proceso(moneda)
def proceso(moneda):
    if moneda=="1":
        ingreso=0.0
        saldo_anterior=float(0.0)
        gasto=float(0.0)
        c=0
        while  True:
            with open("./ingreso.txt", "r") as ingresoIngresado:
                ingreso=float(ingresoIngresado.readline())
                ingresoIngresado.close() 
            with open("./saldoAnterior.txt", "r") as saldoTotal:
                saldo_anterior=float(saldoTotal.readline())
                saldoTotal.close() 
            with open("./gasto.txt", "r") as gastoIngresado:
                gasto=float(gastoIngresado.readline())
                gastoIngresado.close() 
            saldo_actual=float(saldo_anterior-gasto)
            print("\n"*2)
            print("[*] Ingreso: ",ingreso)
            print("[*] Saldo anterior: ",saldo_anterior-ingreso)
            print("[*] Gasto: ",gasto)
            print("[*] Saldo actual: ",saldo_actual)
            if saldo_anterior-ingreso>saldo_actual:
                with open("./saldoAnterior.txt", "w") as saldoAnterior:
                    saldoAnterior.write(str(saldo_actual))
                    saldoAnterior.close()
            while True:
                print("Agregar una accion: ")
                print("""
                    [1] Ingresos
                    [2] Gastos
                    [3] Historial
                    """)
                opcion=str(input("[*] => "))
                if opcion=="1" or opcion=="2" or opcion=="3":break
                else:print("\n Opcion Incorrecta  ")
            if opcion=="1" or opcion=="2":
                while True:
                    try:
                        efectivo=float(input(" <> Ingrese cantidad de dinero:"))
                        break
                    except Exception as e:
                        print("    Ocurrio un error, Ingrese nuevamente solo numeros  ")
                
                print("\t [1][Ahorros]-\t [2][Efectivo]-\t [3][Targeta]-")
                tipo=str(input(" <> Escoja el tipo de gasto: "))
                if tipo=="1":tipo="Ahorros" 
                elif tipo=="2":tipo="Efectivo"
                elif tipo=="3":tipo="Targeta"
                else: tipo=="no hay"
                if opcion == "1":ingresos(efectivo, tipo, opcion)
                elif opcion == "2":gastos(efectivo, tipo, opcion)
            elif opcion=="3":
                with open("./detalles.txt" , "r") as historialParaMostrar:
                    data=historialParaMostrar.read()
                    print(data)
def gastos(efectivo, tipo, opcion):
    os.system("cls")
    print("\n")
    categoria=regualdor1()
    with open("./gasto.txt", "w") as gastoIngresado:
        gastoIngresado.write(str(efectivo))
        gastoIngresado.close()
    with open("./ingreso.txt", "w") as ingresoA:
        ingresoA.write('0')
        ingresoA.close()
    historial(efectivo, tipo, categoria, opcion)
def ingresos(efectivo, tipo, opcion):
    os.system("cls")
    print("\n")
    print("\t[1][Préstamo]\t[2][Sueldo]\t[3][Ventas]")
    categoria=str(input(" <> Escoja una categoria: "))
    if categoria=="1":categoria="Prestamo"
    elif categoria=="2":categoria="Sueldo"
    elif categoria=="3":categoria="Ventas"
    else:categoria=="no hay"
    with open("./gasto.txt", "w") as gastoIngresado:
        gastoIngresado.write('0')
        gastoIngresado.close()
    with open("./ingreso.txt", "w") as ingresoA:
        ingresoA.write(str(efectivo))
        ingresoA.close()
    with open("./saldoAnterior.txt", "r") as saldoAn:
        saldo_anterior=float(saldoAn.readline())
        saldoAn.close()
    with open("./saldoAnterior.txt", "w") as saldoAnterior:
        saldoAnterior.write(str(saldo_anterior+efectivo))
        saldoAnterior.close()
    historial(efectivo, tipo, categoria, opcion)
def historial(efectivo, tipo,categoria, opcion):
    if opcion=="1":opcion="Ingreso de saldo"
    elif opcion=="2":opcion="Gasto de saldo"
    fecha=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    informacion=f"""
    [*]Fecha: {fecha}
        >Accion: {opcion}
        >Efectivo: {efectivo}
        >Tipo: {tipo}
        >Categoria: {categoria}\n\n"""
    with open("./detalles.txt", "a") as resumen:
        resumen.write(informacion)        
def regualdor1():
    categoria=""
    while True:
        print("\t[1][Autos]\t[2][Bebidas]\t[3][Comida]\t[4][Diversion]\n\t[5][Educacion]\t[6][Gasolina]\t[7][Hotel]\t[8][Mascota]")
        categoria=str(input(" <> Escoja una categoria: "))
        if categoria=="1":return("Autos")
        elif categoria=="2":return("Bebidas")
        elif categoria=="3":return("Comida")
        elif categoria=="4":return("Diversion")
        elif categoria=="5":return("Educacion")
        elif categoria=="6":return("Gasolina")
        elif categoria=="7":return("Hotel")
        elif categoria=="8":return("Mascota")
        else:print("La opcion no existe ")
if __name__=='__main__':
    inicio()