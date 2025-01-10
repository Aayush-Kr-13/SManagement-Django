from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('home/', home),
    path('add-std/', std_add),
    path('delete-std/<int:regno>', delete_std),
    path('update-std/<int:regno>', update_std),
    path('do-update-std/<int:regno>', do_update_std),
]
