from django.urls import path
from . import views


urlpatterns = [
    path('', views.getData, name='get_data'),
    path('api/add_item/', views.addItem, name='add_item'),
]
