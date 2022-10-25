from django.urls import path
from django.views.decorators.csrf import csrf_exempt 
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', csrf_exempt(views.processOrder), name='process_order'),
    path('account/register/', views.register, name='register'),
    path('account/login/', views.login, name='login'),
]
