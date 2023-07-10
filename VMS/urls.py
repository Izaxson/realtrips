
from django.contrib import admin
from django.urls import  path ,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from accounts.views import LoginView

urlpatterns = [
    
    path('accounts', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('realtrips.urls')),
    path('', include('accounts.urls')),
]
urlpatterns+=staticfiles_urlpatterns()
