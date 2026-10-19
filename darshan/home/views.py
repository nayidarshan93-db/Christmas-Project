from django.shortcuts import render, redirect, get_object_or_404
from home.models import*
from .models import Product
# Create your views here.

def headerweb(request):
    return render(request,"headerweb.html")

def headerpro(request):
    return render(request,"headerpro.html")

def project1(request):
    return render(request,"project1.html")

def shop1(request):
    products = Product.objects.all()
    return render(request,"shop1.html",{'products': products})
def shop2(request):
    return render(request,"shop2.html")

# def dashboard(request):
#     return render(request,"dashboard.html")

def dashboard(request):
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        Product.objects.create(
            name=name,
            price=price,
            description=description,
            image=image
        )
      
        return redirect('dashboard')
    products = Product.objects.all()
    return render(request, "dashboard.html", {'products': products})



def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('dashboard')

# def update(request,id):
#     product=Product.objects.get(id=id)
#     if request.method == "POST":
#             name = request.POST.get('name')
#             price = request.POST.get('price')
#             description = request.POST.get('description')
#             image = request.FILES.get('image')
    
#             Product.objects.filter(id=id).update(
#                 name=name,
#                 price=price,
#                 description=description,
#                 image=image
#             )
          
#             return redirect('dashboard')
#     products = Product.objects.all()
#     return render(request, "update.html", {'products': products})

def update(request, id):
    item = Product.objects.get(id=id)

    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("prize")
        image = request.FILES.get("image")

        item.name = name
        item.price = price

  
        if image:
            item.image = image

        item.save()

        return redirect('dashboard')

    context = {'detail': item}
    return render(request, "update.html", context)