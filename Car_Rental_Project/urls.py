"""
URL configuration for Car_Rental_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from Cars.views import homepage
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", homepage, name='homepage'),
    path('admin/', admin.site.urls),
	path('Cars/', include('Cars.urls')),
	path('Airport/', include('Airport.urls')),
	path('Van_Rental/', include('Van_Rental.urls')),
	path('Personal_Driver/', include('Personal_Driver.urls')),
    path('', include('accounts.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
