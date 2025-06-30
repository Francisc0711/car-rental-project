from django.urls import path
from .views import personal_driver_details_view

urlpatterns = [

	path("details_personal_driver", personal_driver_details_view),
]
