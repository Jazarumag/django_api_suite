# guia 20
from django.urls import path
from . import views

urlpatterns = [
    # GET y POST
    path("index/", views.DemoRestApi.as_view(), name="demo_rest_api_resources"),
    
    # PUT, PATCH y DELETE
    path("index/<str:item_id>/", views.DemoRestApiItem.as_view(), name="demo_rest_api_item"),
]
