class Producto:
    def __init__(self, producto_id, nombre, descripcion, costo, cantidad, margen_de_venta):
        self.id = producto_id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.margen_de_venta = margen_de_venta
        self.precio_de_venta = None  

    def registrar_producto(self, callback):
  
        self.precio_de_venta = callback(self.costo, self.margen_de_venta)

        producto_dict = {
            'ID': self.id,
            'Nombre': self.nombre,
            'Descripción': self.descripcion,
            'Costo': self.costo,
            'Cantidad': self.cantidad,
            'Precio de Venta': self.precio_de_venta
        }

        productos[self.id] = producto_dict

    @staticmethod
    def imprimir_productos():
    
        for producto_id, producto_info in productos.items():
            print(f"ID: {producto_id}")
            for key, value in producto_info.items():
                print(f"{key}: {value}")
            print("\n")


productos = {}

def calcular_precio_venta(costo, margen_de_venta):
    return costo / (1 - margen_de_venta)

producto_id = int(input("Ingrese el ID del producto: "))
nombre = input("Ingrese el nombre del producto: ")
descripcion = input("Ingrese la descripción del producto: ")
costo = float(input("Ingrese el costo del producto: "))
cantidad = int(input("Ingrese la cantidad del producto: "))
margen_de_venta = float(input("Ingrese el margen de venta del producto (porcentaje): ")) / 100


nuevo_producto = Producto(producto_id, nombre, descripcion, costo, cantidad, margen_de_venta)

nuevo_producto.registrar_producto(calcular_precio_venta)

Producto.imprimir_productos()
