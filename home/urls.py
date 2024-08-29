from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('signup' , signup , name = 'signup'),
    path('account/profile' , profile , name='profile'),
    path('search' , search , name='search'),
    path('search_profile' , search_profile , name='search_profile'),




  

]
