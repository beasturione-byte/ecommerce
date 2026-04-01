# tienda/carrito.py

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, producto):
        id_producto = str(producto.id)
        if id_producto not in self.carrito.keys():
            self.carrito[id_producto] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
            }
        else:
            self.carrito[id_producto]["cantidad"] += 1
        self.guardar()

    def guardar(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id_producto = str(producto.id)
        if id_producto in self.carrito:
            del self.carrito[id_producto]
            self.guardar()

    def restar(self, producto):
        id_producto = str(producto.id)
        if id_producto in self.carrito.keys():
            self.carrito[id_producto]["cantidad"] -= 1
            if self.carrito[id_producto]["cantidad"] <= 0:
                self.eliminar(producto)
            else:
                self.guardar()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
        
    def obtener_total(self):
        total = 0
        for item in self.carrito.values():
            total += float(item["precio"]) * item["cantidad"]
        return total