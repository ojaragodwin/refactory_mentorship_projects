from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('index/',views.index, name = 'index'),
    path('home/',views.home, name = 'home'),
    path('', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'logout.html'), name='logout'),
    #this route is for buying items
    path('index/<int:product_id>', views.product_details, name='product_details'),
    path('issue_item/<str:pk>', views.issue_item, name= 'issue_item'),
    path('add_to_stock/<str:pk>', views.add_to_stock, name= 'add_to_stock'),
    #handling the receipt after a successful sale
    path('receipt/',views.receipt, name='receipt'),
]