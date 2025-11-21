import datos_del_inventario
from operaciones import agregar_prenda, vender_prenda, consultar_existencias, mostrar_inventario

def menu():
    while True:
        print("\n==============================")
        print("      SISTEMA DE INVENTARIO")
        print("==============================")
        print("1. Agregar prenda")
        print("2. Registrar venta")
        print("3. Consultar existencias")
        print("4. Mostrar inventario")
        print("5. Ingresos del día")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_prenda()
        elif opcion == "2":
            vender_prenda()
        elif opcion == "3":
            consultar_existencias()
        elif opcion == "4":
            mostrar_inventario()
        elif opcion == "5":
            print(f"\nIngresos del día: ${datos_del_inventario.ingresos_del_dia:.2f}")
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
