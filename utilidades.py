import datos_del_inventario

def generar_codigo(tipo):
        """Genera un código único para una prenda basada en su tipo"""
    inicial = tipo[0].upper()
    contador = 0
    for prenda in datos_del_inventario.inventario:
        if prenda["tipo"] == tipo:
            contador += 1
    numero = contador + 1
    return f"{inicial}{numero:03d}"
