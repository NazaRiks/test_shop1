from django.urls import path

from shop import views



urlpatterns = [

path('All_Products/', views.ProductListAll.as_view(), name='product_list' ),
path('<int:pk>', views.ProductDetail.as_view(), name='product_detail'),

]