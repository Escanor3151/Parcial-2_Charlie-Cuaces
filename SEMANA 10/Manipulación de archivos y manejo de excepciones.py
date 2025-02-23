import os
import json
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

    def to_dict(self):
        return {"id": self.id_producto, "nombre": self.nombre, "cantidad": self.cantidad, "precio": self.precio}

class Inventario:
    ARCHIVO = "inventario.txt"
    def __init__(self):
        self.productos = {}
        self.cargar_inventario()

    def guardar_inventario(self):
        try:
            with open(self.ARCHIVO, "w") as f:
                json.dump([p.to_dict() for p in self.productos.values()], f, indent=4)
        except (PermissionError, IOError) as e:
            print(f"Error al guardar el inventario: {e}")

    def cargar_inventario(self):
        if os.path.exists(self.ARCHIVO):
            try:
                with open(self.ARCHIVO, "r") as f:
                    productos = json.load(f)
                    self.productos = {p["id"]: Producto(p["id"], p["nombre"], p["cantidad"], p["precio"]) for p in
                                      productos}
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Error al cargar el inventario: {e}")

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: Producto ya existe. Actualizando Cantidad")
            self.productos[producto.id_producto].cantidad += producto.cantidad
        else:
            self.productos[producto.id_producto] = producto
            print("Producto agregado correctamente")
        self.guardar_inventario()

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado correctamente")
        else:
            print("Error: Producto no encontrado.")
        self.guardar_inventario()

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            print("Producto actualizado correctamente")
        else:
            print("Error: Producto no encontrado.")
        self.guardar_inventario()

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("Producto no encontrado.")

    def mostrar_inventario(self):
        if self.productos:
            for p in self.productos.values():
                print(p)
        else:
            print("Inventario vacío.")
# Interfaz de usuario
def menu():
    inventario = Inventario()
    while True:
        print(
            "\n1. Agregar Producto\n2. Eliminar Producto\n3. Actualizar Producto\n4. Buscar Producto\n5. Mostrar Inventario\n6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '6':
            break
        elif opcion == '1':
            id_producto = input("ID producto: ")
            nombre = input("Nombre producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
            inventario.guardar_inventario()
            inventario.cargar_inventario()
        elif opcion == '2':
            id_producto = input("ID producto: ")
            inventario.eliminar_producto(id_producto)
            inventario.guardar_inventario()
            inventario.cargar_inventario()
        elif opcion == '3':
            id_producto = input("ID producto: ")
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_producto(id_producto, cantidad, precio)
            inventario.guardar_inventario()
            inventario.cargar_inventario()
        elif opcion == '4':
            nombre = input("Nombre producto: ")
            inventario.buscar_producto(nombre)
            inventario.guardar_inventario()
            inventario.cargar_inventario()
        elif opcion == '5':
            inventario.mostrar_inventario()
            inventario.guardar_inventario()
            inventario.cargar_inventario()
if __name__ == "__main__":
    menu()
