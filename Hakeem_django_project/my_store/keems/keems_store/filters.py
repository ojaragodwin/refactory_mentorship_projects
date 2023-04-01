import django_filters
from .models import Category,Product
#creating a class to filter objects from models
class Product_filters(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = [
            'item_name',
        ]

class Category_filter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = [
            'name',
        ]        
        