#from pickle import FROZENSET
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from.import views

urlpatterns = [
    path('', views.index, name="home"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('cart', views.cart_info, name="cartdtls"),
    path('checkout', views.checkout, name="checkout"),

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)