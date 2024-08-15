from django.shortcuts import render, redirect
from django.views import View
from .models import Products, Order
from store.models import Customer, Category
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

# View for the homepage displaying products
class Index(View):
    def get(self, request):
        products = Products.get_all_products()
        return render(request, 'store/index.html', {'products': products})

# View for user signup
class Signup(View):
    def get(self, request):
        return render(request, 'store/signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        # Validation
        error_message = None
        if not first_name:
            error_message = "First Name Required!!"
        elif len(first_name) < 4:
            error_message = "First Name must be 4 characters long or more."
        elif not last_name:
            error_message = "Last Name Required."
        elif len(last_name) < 4:
            error_message = "Last Name must be 4 characters long or more."
        elif not phone:
            error_message = "Phone Number Required."
        elif len(phone) < 10:
            error_message = "Phone Number must be 10 characters long."
        elif len(password) < 6:
            error_message = "Password must be 6 characters long."
        elif Customer.get_customer_by_email(email):
            error_message = "Email Address Already Registered."

        if not error_message:
            customer = Customer(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                password=make_password(password)
            )
            customer.register()
            return redirect('homepage')
        else:
            return render(request, 'store/signup.html', {'error': error_message})

# View for user login
class Login(View):
    def get(self, request):
        return render(request, 'store/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)

        if customer and check_password(password, customer.password):
            request.session['customer'] = customer.id
            return redirect('homepage')
        else:
            return render(request, 'store/login.html', {'error': 'Email or Password invalid!'})

# View for the shopping cart
class Cart(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        product_ids = list(cart.keys())
        products = Products.get_products_by_id(product_ids)
        return render(request, 'store/cart.html', {'products': products})

# View for adding/removing items from the cart
def add_to_cart(request):
    product_id = request.GET.get('product_id')
    cart = request.session.get('cart', {})

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart
    return redirect('cart')

# View for checkout
class CheckOut(View):
    def get(self, request):
        return render(request, 'store/checkout.html')

    def post(self, request):
        # Handle order placement logic here
        return HttpResponse("Order placed successfully!")

# View for displaying user orders
class OrderView(View):
    def get(self, request):
        customer_id = request.session.get('customer')  # Get the logged-in customer ID from the session
        if customer_id:
            orders = Order.objects.filter(customer_id=customer_id)  # Fetch orders for the logged-in user
            return render(request, 'store/orders.html', {'orders': orders})  # Render orders template
        else:
            return redirect('login')  # Redirect to login if the user is not logged in