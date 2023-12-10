from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

CART_SESSION_ID = 'cart'

class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID) 
        
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
            
        self.cart = cart
    
    def add(self, product, quantity=1):
        product_id = str(product.id)
        if not product_id in self.cart:
            self.cart[product_id] = {'title' :product.title , 'quantity' : 0, 'price' : str(product.price) } 
        self.cart[product_id]['quantity'] += quantity
        self.save()

    def delete(self, product, quantity=1):
        product_id = str(product.id)
        if not product_id in self.cart:
            return None
        
        if self.cart[product_id]['quantity'] >= quantity :
            self.cart[product_id]['quantity'] -= quantity

        self.save()


    def save(self):
        self.session.modified = True


    def __len__(self):
        return sum([self.cart[id]['quantity'] for id in self.cart])

    def __iter__(self):
        for product in self.cart.items():
            yield product


    def get_total_price(self):
        return sum([item['quantity'] * float(item['price']) for item in self.cart.values()])
        
    
        



