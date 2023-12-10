from django.conf import settings


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


    def save(self):
        self.session.modified = True


    def __len__(self):

        return sum([self.cart[id]['quantity'] for id in self.cart])
