from django.urls import path
from .views import car_details_view
from .views import all_cars_view, car_category_view
from .views import confort_view, lux_view, sport_view, car_details

urlpatterns = [

	path("all", all_cars_view),
	path("details_car", car_details_view),
    path('car_category', car_category_view),
    path('category/confort/', confort_view, name='category_confort'),
    path('category/lux/', lux_view, name='category_lux'),
    path('category/sport/', sport_view, name='category_sport'),
    path('details/<slug:slug>/', car_details, name='car_details'),

]
