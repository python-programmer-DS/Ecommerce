from django.urls import path
from .views import Index, Signup, Login, Cart, CheckOut, OrderView, add_to_cart

urlpatterns = [
    path('', Index.as_view(), name='homepage'),  # Homepage
    path('signup/', Signup.as_view(), name='signup'),  # User signup
    path('login/', Login.as_view(), name='login'),  # User login
    path('cart/', Cart.as_view(), name='cart'),  # Shopping cart
    path('check-out/', CheckOut.as_view(), name='checkout'),  # Checkout
    path('orders/', OrderView.as_view(), name='orders'),  # Order history
    path('add-to-cart/', add_to_cart, name='add_to_cart'),  # Add item to cart
]