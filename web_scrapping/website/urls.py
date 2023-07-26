from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('iphone/',iphone,name='home'),
    path('ipad/',ipad,name='home'),
    path('macbook/',macbook,name='home'),
    path('downloadIphone/',downloadIphone,name='download'),
    path('downloadIpad/',downloadIpad,name='download'),
    path('downloadMac/',downloadMac,name='download'),
    path('graphIphone/',graphIphone,name='download'),

]