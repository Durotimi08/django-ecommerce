from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('fashion', views.fashion, name='fashion'),
    path('jewellery/', views.jewellery, name='jewellery'),
    path('electronic/', views.electronic, name='electronic'),
    path('product_upload', views.product_upload, name='product_upload'),
]
