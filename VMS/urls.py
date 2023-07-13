<<<<<<< HEAD

from django.contrib import admin
from django.urls import  path ,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
=======
"""
URL configuration for VMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import  path ,include

>>>>>>> 016e58452a172b5d6ef68c4ccac19597a44f6828
from accounts.views import LoginView

urlpatterns = [
    
    path('accounts', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('realtrips.urls')),
    path('', include('accounts.urls')),
]
<<<<<<< HEAD
urlpatterns+=staticfiles_urlpatterns()
=======
>>>>>>> 016e58452a172b5d6ef68c4ccac19597a44f6828
