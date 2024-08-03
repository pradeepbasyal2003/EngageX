from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('signup' , signup , name = 'signup'),
    path('account/profile' , profile , name='profile'),
    path('account/update_profile' , update_profile , name='update-profile')

  

]
