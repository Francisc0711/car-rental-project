from django.urls import path
from .views import car_details_view
from .views import all_cars_view
from .views import car_details,category_view
from .views import homepage
urlpatterns = [
    path("", homepage, name='home'),
	path("all", all_cars_view),
	path("details_car", car_details_view),
    path('details/<slug:slug>/', car_details, name='car_details'),
    path('car_category/<str:category>/', category_view, name='category'),

]
