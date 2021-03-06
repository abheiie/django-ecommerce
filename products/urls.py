from django.conf.urls import url

from django.urls import path

from .views import (
        ProductListView, 
        ProductDetailSlugView, 
        product_category,
        ProductCategoryListView
        )

app_name= "products"

urlpatterns = [

    url(r'^$', ProductListView.as_view(), name='list'),
    path('category/<str:category>/', ProductCategoryListView.as_view(), name='categorylist'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
    # path("category/<str:category>/", product_category, name = "product_category" )

]

