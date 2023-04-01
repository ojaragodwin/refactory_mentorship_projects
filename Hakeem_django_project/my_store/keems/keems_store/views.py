from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product,Sale
from .filters import Product_filters
#we now include our filters from the filters side
#we are going to first include the models to be used here
# Create your views here.
#including our models form created in the forms file
from .forms import AddForm,SaleForm
def index(requests):
    products = Product.objects.all().order_by('-id')
    product_filters = Product_filters(requests.GET,queryset= products)
    products = product_filters.qs
    return render(requests,'index.html',{'products': products,'product_filters': product_filters})

@login_required
def home(requests):
    return render(requests,'home')

@login_required
def LoginView(requests):
    return render(requests,'login.html')

def home(requests):
    return render(requests,'base.html')

def LogoutView(requests):
    return render(requests,'logout.html')

#creating a view for product_detail
@login_required
def product_details(requests,product_id):
    product = Product.objects.get(id = product_id)
    return render(requests,'product_details.html',{'product':product})

@login_required
def issue_item(requests,pk):
   issued_item = Product.objects.get(id = pk)
   Sales_Form = SaleForm(requests.POST)

   if requests.method == 'POST':
        #checks if the input is as its supposed to be
        if Sales_Form.is_valid():
            new_sale = Sales_Form.save(commit = False)
            new_sale.item = issued_item
            new_sale.unit_price = issued_item.unit_price
            new_sale.save()
            #to keep tarck of the stock remaining after sales
            issued_quantity = int(requests.POST['quantity'])
            issued_item.total_quantity -= issued_quantity
            issued_item.save()
            print(issued_item.item_name)
            print(requests.POST['quantity'])
            print(issued_item.total_quantity)

        return redirect('receipt')
   return render (requests, 'issue_item.html',{'sales_form': Sales_Form})       
#this handles receipt
@login_required
def receipt(requests):
    sales = Sale.objects.all().order_by('-id')
    return render(requests, 'receipt.html', {'sales':sales})
                                                                
                                

@login_required
def add_to_stock(requests):
    pass

    

