class Carro:
    def __init__(self, id, marca, modelo, costo, cantidad):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.costo = costo
        self.cantidad = cantidad
        self.precio_de_venta = None

    def calcular_precio_venta(self, margen_de_venta):
        if margen_de_venta <= 0:
            raise ValueError("El margen de venta debe ser mayor que 0")
        self.precio_de_venta = self.costo / (1 - margen_de_venta)

class RegistroCarros:
    def __init__(self):
        self.carros = {}

    def registrar_carro(self, carro, margen_de_venta):
        if carro.id in self.carros:
            raise ValueError("El carro ya está registrado.")
        carro.calcular_precio_venta(margen_de_venta)
        self.carros[carro.id] = carro

    def imprimir_carros(self):
        for carro in self.carros.values():
            print(f"ID: {carro.id}, Marca: {carro.marca}, Modelo: {carro.modelo}, Precio de Venta: {carro.precio_de_venta:.2f}")

# Función para obtener datos del usuario
def obtener_datos_carro():
    id = int(input("ID del carro: "))
    marca = input("Marca del carro: ")
    modelo = input("Modelo del carro: ")
    costo = float(input("Costo del carro: "))
    cantidad = int(input("Cantidad de carros: "))
    return Carro(id, marca, modelo, costo, cantidad)

# Ejemplo de uso
if __name__ == "__main__":
    registro = RegistroCarros()
    
    while True:
        try:
            carro = obtener_datos_carro()
            margen_de_venta = float(input("Margen de venta (porcentaje): ")) / 100
            registro.registrar_carro(carro, margen_de_venta)
            imprimir = input("¿Desea registrar otro carro? (S/N): ").strip().lower()
            if imprimir != 's':
                break
        except ValueError as e:
            print(e)
    
    registro.imprimir_carros()
