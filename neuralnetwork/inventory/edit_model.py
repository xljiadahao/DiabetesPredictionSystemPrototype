from models import Product

p = Product.objects.get(code="P2033")
p.price = int(p.price * 0.95)
p.save()
