from django.shortcuts import render

# Create your views here.

def personal_driver_details_view(request):
	context = {}
	return render(request, 'personal_driver_details.html', context)
