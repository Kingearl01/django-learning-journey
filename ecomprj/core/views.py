from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from taggit.models import Tag

from core.models import *
from core.forms import ProductReviewForm

# Create your views here.

# @login_required
def IndexView(request):
    products = Product.objects.filter(product_status='published').order_by('-date')
    featured_products = Product.objects.filter(featured=True).order_by('-date')
    context = {
        'products': products,
        'featured_products': featured_products,
    }
    return render(request, 'core/index.html', context)

def product_list_view(request):
    products = Product.objects.filter(product_status='published').order_by('-date')
    context = {
        'products': products,
    }
    return render(request, 'core/product-list.html', context)

def product_detail_view(request, pid):
    product = get_object_or_404(Product, pid=pid)
    product_images = product.product_images.all()

    products = Product.objects.filter(product_status='published', category=product.category).exclude(pid=pid)

    # get review
    reviews = ProductReview.objects.filter(product=product).order_by('-date')

    # Getting Average Ratings
    average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('ratings'))

    # Product Review Form
    review_form = ProductReviewForm()

    context = {
        'product': product,
        'product_images': product_images,
        'products': products,
        'reviews': reviews,
        'average_rating': average_rating,
        'review_form': review_form,
        'avg_percent_rating': int(average_rating['rating'] * 20),
 
    }
    return render(request, 'core/product-detail.html', context)

def category_list_view(request):
    # categories = Category.objects.all()
    categories = Category.objects.all().annotate(product_count=Count('category'))
    context = {
        'categories': categories,
    }
    return render(request, 'core/category-list.html', context)

def category_product_list_view(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status='published', category=category).order_by('-date')

    context = {
        'category': category,
        'products': products,
    }

    return render(request, 'core/category-product-list.html', context)

def vendor_list_view(request):
    vendors = Vendor.objects.all()
    context = {
        'vendors': vendors
    }
    return render(request, 'core/vendors-list.html', context)

def vendor_detail_view(request, vid):
    vendor = Vendor.objects.get(vid=vid)
    products = Product.objects.filter(product_status='published',vendor=vendor)
    context = {
        'vendor': vendor,
        'products': products,
    }
    return render(request, 'core/vendor-details.html', context)

def tag_list(request, tag_slug=None):
    product= Product.objects.filter(product_status='published').order_by('-date')

    tag = None
    if tag_slug:
        tag = get_list_or_404(Tag ,slug=tag_slug)
        products = product.filter(tags__in=tag)
        print(tag[0])
        print(products  )
        context = {
            "products": products,
            'tag': tag,
        }

    return render(request, 'core/tag.html', context)


def ajax_add_review(request, pid):
    product = Product.objects.get(pid=pid)
    user = request.user

    if request.method == "POST":
        # review = ProductReview.objects.create(
        #     user=user,
        #     product=product,
        #     review= request.POST['review'],
        #     ratings = request.POST['rating']
        # )
        data = request.POST.get('data_key', None)
        print(data)

        context  = {
            'user': user.username,
            'review': request.POST['review'],
            'rating': request.POST['ratings'],
        }

        average_ratings = ProductReview.objects.filter(product=product).aggregate(rating=Avg('ratings'))
        response_data = {
            'bool': True,
            'context': context,
            'average_ratings': average_ratings
            }

        return JsonResponse(response_data)

    else:
        return JsonResponse({'error': 'Invalid request input'})



def filter_product(request):
    
    categories= request.GET.getlist('category[]')
    vendors= request.GET.getlist('vendor[]')

    
    products = Product.objects.filter(product_status='published').order_by('date')

    if len(categories) > 0:
        products = products.filter(category__id__in=categories)
    print(f'{products} with length {len(products)}')  
    if len(vendors) > 0:
        products = products.filter(vendor__id__in=vendors)

    print(f'{products} with length {len(products)}') 
    data = render_to_string("core/async/product-list.html", {'products': products}) 

    return JsonResponse({
        'data': data,
    })

def add_to_cart(request):
    cart_product = {}
    cart_product[str(request.GET['id'])] = {
        'title': request.GET['title'],
        'qty': request.GET['qty'],
        'price': request.GET['price'],
    }

    if 'cart_data_obj' in request.session:
        if str(request.GET['id']) in request.session['cart_data_obj']:
            cart_data = request.session['cart_data_obj']
            cart_data[str(request.GET['id'])]['qty'] = int(cart_product[str(request.GET['id'])]['qty'])
            cart_data.update(cart_data)
            request.session['cart_data_obj'] = cart_data
        
        else:
            cart_data = request.session['cart_data_obj']
            cart_data.update(cart_product)
            request.session['cart_data_obj'] = cart_data

    else:
        request.session['cart_data_obj'] = cart_product

    return JsonResponse({
        'data': request.session['cart_data_obj'],
        'total_cart_item': len(request.session['cart_data_obj']),
    })