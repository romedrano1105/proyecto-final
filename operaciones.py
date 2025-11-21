import datos_del_inventario
from utilidades import generar_codigo

def agregar_prenda():
    print("\n--- AGREGAR PRENDA ---")
    print("1. Pantalón")
    print("2. Camisa")
    print("3. Suéter")
    print("4. Agregar tipo nuevo")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        tipo = "pantalon"
    elif opcion == "2":
        tipo = "camisa"
    elif opcion == "3":
        tipo = "sueter"
    elif opcion == "4":
        tipo = input("Ingrese nuevo tipo: ").lower()
    else:
        print("Opción inválida")
        return

    codigo = generar_codigo(tipo)
    talla = input("Talla: ").upper()
    color = input("Color: ").capitalize()
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio unitario: $ "))

    prenda = {
        "tipo": tipo,
        "codigo": codigo,
        "talla": talla,
        "color": color,
        "cantidad": cantidad,
        "precio": precio
    }

    datos_del_inventario.inventario.append(prenda)

    print(f"\nPrenda agregada con código {codigo}\n")


def vender_prenda():
    print("\n--- REGISTRAR VENTA ---")
    codigo_buscar = input("Código de la prenda vendida: ").upper()

    prenda_encontrada = None

    for prenda in datos_del_inventario.inventario:
        if prenda["codigo"] == codigo_buscar:
            prenda_encontrada = prenda
            break

    if prenda_encontrada is None:
        print("No existe ninguna prenda con ese código.")
        return

    print("\n=== Prenda encontrada ===")
    print(f"Tipo: {prenda_encontrada['tipo']}")
    print(f"Código: {prenda_encontrada['codigo']}")
    print(f"Talla: {prenda_encontrada['talla']}")
    print(f"Color: {prenda_encontrada['color']}")
    print(f"Existencias: {prenda_encontrada['cantidad']}")
    print(f"Precio unitario: ${prenda_encontrada['precio']:.2f}")

    cantidad_vendida = int(input("\nCantidad vendida: "))

    if cantidad_vendida > prenda_encontrada["cantidad"]:
        print("No hay suficientes existencias.")
        return

    prenda_encontrada["cantidad"] -= cantidad_vendida
    ingreso = cantidad_vendida * prenda_encontrada["precio"]
    datos_del_inventario.ingresos_del_dia += ingreso

    print(f"\nVenta registrada correctamente.")
    print(f"Ingreso generado: ${ingreso:.2f}")

    if prenda_encontrada["cantidad"] == 0:
        datos_del_inventario.inventario.remove(prenda_encontrada)
        print("La prenda llegó a 0 existencias y fue eliminada.")


def consultar_existencias():
    print("\n--- CONSULTAR EXISTENCIAS ---")

    tipo = input("Tipo de prenda: ").lower()

    existe_tipo = False
    for p in datos_del_inventario.inventario:
        if p["tipo"] == tipo:
            existe_tipo = True
            break
    if not existe_tipo:
        print("No existe ese tipo de prenda.")
        return

    codigo = input("Código: ").upper()

    existe_codigo = False
    prendas_mismo_codigo = []
    for p in datos_del_inventario.inventario:
        if p["codigo"] == codigo:
            existe_codigo = True
            prendas_mismo_codigo.append(p)

    if not existe_codigo:
        print("No existe ninguna prenda con ese código.")
        return

    talla = input("Talla: ").upper()

    existe_talla = False
    prendas_misma_talla = []
    for p in prendas_mismo_codigo:
        if p["talla"] == talla:
            existe_talla = True
            prendas_misma_talla.append(p)

    if not existe_talla:
        print("No existe esa talla para ese código.")
        return

    color = input("Color: ").capitalize()

    existe_color = False
    prenda_final = None
    for p in prendas_misma_talla:
        if p["color"] == color:
            existe_color = True
            prenda_final = p
            break

    if not existe_color:
        print("No existe ese color en esa talla.")
        return

    print(f"\nExistencias: {prenda_final['cantidad']}")
    print(f"Precio unitario: ${prenda_final['precio']:.2f}")


def mostrar_inventario():
    print("\n===== INVENTARIO COMPLETO =====\n")

    if len(datos_del_inventario.inventario) == 0:
        print("Inventario vacío.")
        return

    for p in datos_del_inventario.inventario:
        print(f"Tipo: {p['tipo']} | Código: {p['codigo']} | Talla: {p['talla']} | "
              f"Color: {p['color']} | Cantidad: {p['cantidad']} | "
              f"Precio: ${p['precio']:.2f}")
