def precioTotalCarrito(request):
    total = 0
    # if request.user.is_authenticated:
    if "carrito" in request.session:
        for key, value in request.session["carrito"].items():
            total = total + (float(value["price"]))
    return {"precioTotalCarrito": total}


def cantTotalCarrito(request):
    cantidad = 0
    # if request.user.is_authenticated:
    if "carrito" in request.session:
        for key, value in request.session["carrito"].items():
            cantidad = cantidad + value["quantity"]
    return {"cantTotalCarrito": cantidad}
