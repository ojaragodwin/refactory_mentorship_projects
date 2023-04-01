#interface where a user creates data
from django .forms import ModelForm
#accessing our model so that we can link to the form
from .models import *

class AddForm(ModelForm):
    class Meta:
        model = Product
        #updating the already existing stock
        fields = ['received_quantity']
#we are modelling a form based on our model that we shall use to record a given product
class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = ['quantity','amount_received','issued_to']