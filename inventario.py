"""
Sistema de inventario para una tienda local.
Taller Práctico de Git - Control de Versiones.
"""

inventario = {}


def agregar_producto(codigo, nombre, precio, cantidad):
    """Agrega un producto nuevo a la estructura de inventario."""
    if precio < 0 or cantidad < 0:
        print("Error: el precio y la cantidad no pueden ser negativos.")
        return

    inventario[codigo] = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
    }
    print(f"Producto '{nombre}' agregado con éxito.")

def actualizar_stock(codigo, cantidad_nueva):
    """Actualiza la cantidad en stock de un producto ya registrado."""
    if codigo in inventario:
        inventario[codigo]["cantidad"] = cantidad_nueva
        print(f"Stock actualizado: {inventario[codigo]['nombre']} -> {cantidad_nueva} unidades.")
    else:
        print("Producto no encontrado.")


def mostrar_inventario():
    """Muestra todos los productos registrados y su información."""
    print("\n--- Inventario actual ---")
    for codigo, datos in inventario.items():
        print(f"{codigo}: {datos['nombre']} | ${datos['precio']} | Stock: {datos['cantidad']}")


# Registro de productos iniciales de la tienda
agregar_producto("P001", "Arroz x 500g", 3500, 50)
agregar_producto("P002", "Aceite x 1L", 8500, 20)

# Prueba de las nuevas funciones
actualizar_stock("P001", 40)
mostrar_inventario()