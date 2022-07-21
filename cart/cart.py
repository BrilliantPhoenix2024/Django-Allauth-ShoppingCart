

class Cart:
    def __init__(self, request):
        """
        Initialized the Cart
        """
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}
            # cart = self.session['cart']

        self.cart = cart

    def save(self):
        """
        Mark Session as Modified to Save Changes
        """
        self.session.modified = True

    def add(self, product, quantity=1):
        """
        Add the specified Product to the Cart if it exists
        """
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity}
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()