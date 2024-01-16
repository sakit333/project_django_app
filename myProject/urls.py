# from django.contrib import admin
# from django.urls import path,include
# from myApp import urls

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(urls))
# ]
 

from django.contrib import admin
from django.urls import path, include
from myApp.views import signup, login, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('home/', home, name='home'),  # Add this line
]

