from django.conf.urls import url

from django.urls import path

from .views import (
        ProductListView, 
        ProductDetailSlugView, 
        product_category
        )

app_name= "products"

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
    path("category/<str:category>/", product_category, name = "product_category" )

]

