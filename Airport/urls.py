from django.urls import path
from .views import airport_details_view

urlpatterns = [

	path("details_airport", airport_details_view),
]
