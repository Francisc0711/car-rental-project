from django.urls import path
from .views import van_details_view

urlpatterns = [

	path("details_van", van_details_view),
]
