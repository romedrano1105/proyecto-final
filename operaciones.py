import datos_del_inventario
from utilidades import generar_codigo

# FUNCION AGREGAR PRENDA
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
        return # Se evitan posibles errores por ingresar una opcion no registrada, regresando al menu de opciones

    codigo = generar_codigo(tipo) # Se crea código único por lote ingresado, esto en base a la funcion generar_codigo
    talla = input("Talla: ").upper() 
    color = input("Color: ").capitalize()
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio unitario: $ "))

    prenda = {  # Se definen las características particulares de cada prenda por medio de un diccionario
        "tipo": tipo,
        "codigo": codigo,
        "talla": talla,
        "color": color,
        "cantidad": cantidad,
        "precio": precio
    }

    datos_del_inventario.inventario.append(prenda) # Se agrega la prenda ingresada al inventario

    print(f"\nPrenda agregada con código {codigo}\n") # Se muestra el código generado para la prenda al usuartio
                                                      # junto con la confirmación de que fue agregada exitosamente  

# FUNCION VENDER PRENDA
def vender_prenda():
    print("\n--- REGISTRAR VENTA ---")
    codigo_buscar = input("Código de la prenda vendida: ").upper() 

    prenda_encontrada = None 
# Se asegura la existencia de la prenda
    for prenda in datos_del_inventario.inventario:
        if prenda["codigo"] == codigo_buscar: 
            prenda_encontrada = prenda # Se define la prenda que se ingresó, por medio de una búsqueda en el diccionario de cada prenda
            break                      # si se encuentra el código, entonces se ejecutará el siguiente paso

    if prenda_encontrada is None:
        print("No existe ninguna prenda con ese código.") # En caso de que no haya coincidencias, regresará al usuario al menu inicial de la funcion
        return

    print("\n=== Prenda encontrada ===") # En el siguiente paso, se informa al usuario que la prenda ingresada fue encontrada
    print(f"Tipo: {prenda_encontrada['tipo']}")
    print(f"Código: {prenda_encontrada['codigo']}")
    print(f"Talla: {prenda_encontrada['talla']}")
    print(f"Color: {prenda_encontrada['color']}")
    print(f"Existencias: {prenda_encontrada['cantidad']}")
    print(f"Precio unitario: ${prenda_encontrada['precio']:.2f}") # Se muestran todas las características de la prenda seleccionada 
                                                                  # para confirmación
    cantidad_vendida = int(input("\nCantidad vendida: ")) # Se pregunta al usuario cuántas unidades fueron vendidas para
                                                          # removerlas del inventario y calcular los ingresos
    if cantidad_vendida > prenda_encontrada["cantidad"]:
        print("No hay suficientes existencias.") # Se comprueba la existencia de la prenda, si en el inventario hay una cantidad menor
        return                                   # a la ingresada, se regresará al usuario al input de "Cantidad vendida"

    prenda_encontrada["cantidad"] -= cantidad_vendida # Se hace la resta de las unidades vendidas para guardar el registro en el inventario
    ingreso = cantidad_vendida * prenda_encontrada["precio"]
    datos_del_inventario.ingresos_del_dia += ingreso # Se agregan las ventas a los ingresos del día

    print(f"\nVenta registrada correctamente.") 
    print(f"Ingreso generado: ${ingreso:.2f}") # Se muestra el ingreso generado en esta venta especifica

    if prenda_encontrada["cantidad"] == 0:
        datos_del_inventario.inventario.remove(prenda_encontrada)
        print("La prenda llegó a 0 existencias y fue eliminada.") # Si la prenda llega a existencia 0, se eliminará del inventario

# FUNCION CONSULTAR EXISTENCIAS
def consultar_existencias():
    print("\n--- CONSULTAR EXISTENCIAS ---")

    tipo = input("Tipo de prenda: ").lower() 

    existe_tipo = False
    for p in datos_del_inventario.inventario: # Se asegura que exista ese tipo de prenda en el inventario
        if p["tipo"] == tipo: # Se filtran dentro del inventario las prends que coincidan con ese tipo
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
# Asi como con el codigo, en las siguientes líneas se asegura que existan tanto el color como la talla en la prenda con dicho código
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

# FUNCION MOSTRAR INVENTARIO
def mostrar_inventario():
    print("\n===== INVENTARIO COMPLETO =====\n")

    if len(datos_del_inventario.inventario) == 0: # Si el inventario está vacío, imprimirá el siguiente mensaje
        print("Inventario vacío.")
        return

    for p in datos_del_inventario.inventario: # Se muestra el inventario completo
        print(f"Tipo: {p['tipo']} | Código: {p['codigo']} | Talla: {p['talla']} | "
              f"Color: {p['color']} | Cantidad: {p['cantidad']} | "
              f"Precio: ${p['precio']:.2f}")
