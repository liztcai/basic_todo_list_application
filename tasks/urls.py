from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('show/<str:pk>', views.show, name="show"),
    path('store', views.store, name="store"),
    path('delete/<str:pk>', views.delete, name="delete"),
    path('update/<str:pk>', views.update, name="update"),
    path('put', views.put, name="put"),
]
