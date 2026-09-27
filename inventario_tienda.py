class InventarioTienda:
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.productos = []

    # Agregar producto
    def agregar_producto(self, nombre, precio, cantidad):
        if precio <= 0 or cantidad <= 0:
            print("El precio y la cantidad deben ser mayores que 0.")
            return

        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }

        self.productos.append(producto)
        print("Producto agregado correctamente.")

    # Vender producto
    def vender_producto(self, nombre, cantidad):
        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():

                if cantidad <= 0:
                    print("La cantidad debe ser mayor que 0.")
                    return

                if producto["cantidad"] >= cantidad:
                    producto["cantidad"] -= cantidad
                    print("Venta realizada con éxito.")
                else:
                    print("No hay suficiente stock.")
                return

        print("El producto no existe.")

    # Mostrar inventario
    def mostrar_inventario(self):
        if len(self.productos) == 0:
            print("No hay productos en el inventario.")
            return

        print("\n-INVENTARIO-")
        for producto in self.productos:
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: ${producto['precio']:.2f}")
            print(f"Cantidad: {producto['cantidad']}")
            print("------------------------")

    # Producto más caro
    def producto_mas_caro(self):
        if len(self.productos) == 0:
            print("No hay productos registrados.")
            return

        mas_caro = self.productos[0]

        for producto in self.productos:
            if producto["precio"] > mas_caro["precio"]:
                mas_caro = producto

        print("\nProducto más caro:")
        print(f"Nombre: {mas_caro['nombre']}")
        print(f"Precio: ${mas_caro['precio']:.2f}")


# ---------------- PROGRAMA PRINCIPAL ----------------
nombre = input("Ingrese el nombre de la tienda: ")
tienda = InventarioTienda(nombre)

while True:

    print("\n=MENÚ=")
    print("1. Agregar producto")
    print("2. Vender producto")
    print("3. Mostrar inventario")
    print("4. Producto más caro")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        tienda.agregar_producto(nombre, precio, cantidad)

    elif opcion == "2":
        nombre = input("Nombre del producto: ")
        cantidad = int(input("Cantidad a vender: "))
        tienda.vender_producto(nombre, cantidad)

    elif opcion == "3":
        tienda.mostrar_inventario()

    elif opcion == "4":
        tienda.producto_mas_caro()

    elif opcion == "5":
        print("¡Gracias por usar el sistema!")
        break

    else:
        print("Opción no válida.")