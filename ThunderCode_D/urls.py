from django.contrib import admin
from django.urls import path,include
#from django.contrib.auth.urls import

admin.site.site_header = "Welcome Shubhank"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]
