from .cart import Cart
from store.models import Category

# Create context processor so our cart can work on all pages of the site
def cart(request):
    # Return the default data from our Cart
    return {'cart': Cart(request)}

def categories(request):
    # Return all categories.
    categories = Category.objects.all()
    return {'categories': categories}
