from core.models import Category, Address, Vendor

def default(request):
    categories = Category.objects.all()
    vendors = Vendor.objects.all()
    # address = Address.objects.get(user=request.user)
    context = {
        'categories': categories,
        # 'address': address,
        'vendors': vendors,
    }

    return context 