from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_Item/', views.updateItem, name="update_Item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('login/register/', views.RegisterPage.as_view(), name="register"),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    
]