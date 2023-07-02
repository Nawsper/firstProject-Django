class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito

    def addCarrito(self, product):
        if str(product.id) not in self.carrito.keys():
            self.carrito[str(product.id)] = {
                "product_id": product.id,
                "title": product.title,
                "price": product.price,
                "quantity": 1,
            }
            self.saveCarrito()

    def plusCarrito(self, product):
        product_id = str(product.id)
        if product_id in self.carrito:
            for key, value in self.carrito.items():
                if key == str(product.id):
                    value["quantity"] = value["quantity"] + 1
                    value["price"] = float(value["price"])+product.price
                    break
        self.saveCarrito()

    def saveCarrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def deleteProd(self, product):
        product_id = str(product.id)
        if product_id in self.carrito:
            del self.carrito[product_id]
            self.saveCarrito()

    def restProd(self, product):
        product_id = str(product.id)
        for key, value in self.carrito.items():
            if key == product_id:
                value["quantity"] = value["quantity"] - 1
                if value["quantity"] < 1:
                    self.deleteProd(product)
                break
        self.saveCarrito()

    def cleanCarrito(self):
        self.session["carrito"] = {}
        self.session.modified = True
