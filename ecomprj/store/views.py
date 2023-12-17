from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime


from .models import *
from .utils import guestOrder, cartData
# Create your views here.
def home_view(request):
    data = cartData(request)

    products = Product.objects.all()

    context = {
        'products': products,
        'cartItems': data['cartItems']
    }
    
    return render(request, 'store/index.html', context)



def cart_view(request):
    data = cartData(request)

    context = {
        'items': data['items'],
        'order': data['order'],
        'cartItems': data['cartItems']

    }
    return render(request, 'store/cart.html', context)


def checkout_view(request):
    data = cartData(request)

    context = {
        'items': data['items'],
        'order': data['order'],
        'cartItems': data['cartItems']

    }
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderitem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderitem.quantity = (orderitem.quantity + 1)
    elif action == 'remove':
        orderitem.quantity = (orderitem.quantity - 1)

    orderitem.save()

    if orderitem.quantity  <= 0:
        orderitem.delete()

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    trasaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        
    else:
        customer, order =  guestOrder(request, data)
        print(request.COOKIES)
    total = float(data['form']['total'])
    order.transaction_id = trasaction_id

    if total == float(order.get_cart_total):
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
            )

    return JsonResponse('Payment omplete', safe=False)
