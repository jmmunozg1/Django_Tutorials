from django.urls import path
from .views import *
from .utils import ImageLocalStorage

urlpatterns =[
    path("",HomePageView.as_view(), name='home'),
    path('about/',AboutPageView.as_view(),name='about'),
    path('contact/',ContactPageView.as_view(),name='contact'),
    path('products/',ProductIndexView.as_view(),name='index'),
    path('products/create/',ProductCreateView.as_view(),name='form'),
    path('products/create/created/',ProductCreatedView.as_view(),name='created'),
    path('products/<str:id>',ProductShowView.as_view(),name='show'),
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'),
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),
    
    #Path para imagenes con dependencias
    path('image/', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_index'),
    path('image/save', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_save'),
    
    #para imagenes sin dependencias
    path('imagenotdi/', ImageViewNoDI.as_view(), name='imagenotdi_index'),
    path('imagenotdi/save', ImageViewNoDI.as_view(), name='imagenotdi_save'),
]   