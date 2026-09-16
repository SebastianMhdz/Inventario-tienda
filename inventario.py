"""
Sistema de inventario para una tienda local.
Taller Práctico de Git - Control de Versiones.
"""

inventario = {}


def agregar_producto(codigo, nombre, precio, cantidad):
    """Agrega un producto nuevo a la estructura de inventario."""
    inventario[codigo] = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
    }
    print(f"Producto '{nombre}' agregado con éxito.")


# Registro de productos iniciales de la tienda
agregar_producto("P001", "Arroz x 500g", 3500, 50)
agregar_producto("P002", "Aceite x 1L", 8500, 20)