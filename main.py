import datos_del_inventario
from operaciones import agregar_prenda, vender_prenda, consultar_existencias, mostrar_inventario

# Interfaz del usuario
def menu():
    while True:
        print("\n==============================")
        print("      SISTEMA DE INVENTARIO")
        print("==============================")
        print("1. Agregar prenda") # Se muestra cada una de las opciones
        print("2. Registrar venta") # para facilitar la comprensión 
        print("3. Consultar existencias")
        print("4. Mostrar inventario")
        print("5. Ingresos del día")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")
# Funciones importadas
        if opcion == "1":
            agregar_prenda() #
        elif opcion == "2":
            vender_prenda()
        elif opcion == "3":
            consultar_existencias()
        elif opcion == "4":
            mostrar_inventario()
        elif opcion == "5":
            print(f"\nIngresos del día: ${datos_del_inventario.ingresos_del_dia:.2f}") # 
        elif opcion == "6":
            break # La opcion 6 saca al usuario del menu
        else:
            print("Opción inválida.") # Se evitan posibles errores 

if __name__ == "__main__":
    menu()
