from django.urls import path
from .views import personal_driver_details_view

urlpatterns = [

	path("personal_driver_details", personal_driver_details_view),
]
