import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from cuenta_bancaria import CuentaBancaria

def main():
    # Crear una nueva cuenta bancaria con valores iniciales vacíos
    cuenta = CuentaBancaria('', '')

    # Establecer el nombre del titular
    print("Nombre del titular: ")
    titular = input()
    cuenta.setTitular(titular)
    
    while True:
        print(f"Nombre del titular: {cuenta.getTitular()}")
        print(f"Saldo actual de la cuenta: {cuenta.getSaldo()}")
        print(f"Interés del saldo: {cuenta.calcularInteres()}")
        print("")

        print("1. Ingresar")
        print("2. Retirar")
        print("3. Cambio de nombre del titular")

        try:
            opc = int(input("Seleccione una opción: "))
        except ValueError:
            print("Ingrese un número válido.")
            continue

        if opc == 1:
            print("Monto a ingresar: ")
            try:
                ingreso = float(input())
                cuenta.ingresar(ingreso)
                print(f"Nuevo Saldo actual de la cuenta: {cuenta.getSaldo()}")
                print(f"Nuevo Interés del saldo: {cuenta.calcularInteres()}")
                print("")
            except ValueError:
                print("Ingrese un monto válido.")
        
        elif opc == 2:
            print("Monto a retirar: ")
            try:
                retiro = float(input())
                cuenta.retirar(retiro)
                print(f"Nuevo Saldo actual de la cuenta: {cuenta.getSaldo()}")
                print(f"Nuevo Interés del saldo: {cuenta.calcularInteres()}")
                print("")
            except ValueError:
                print("Ingrese un monto válido.")
        
        elif opc == 3:
            print("Ingrese el nuevo nombre del titular:")
            nuevo_titular = input()
            cuenta.setTitular(nuevo_titular)
            print(f"Nombre actualizado a: {cuenta.getTitular()}")
        
        else:
            print("Ingrese una opción válida.")
            print("")

if __name__ == '__main__':
    main()
