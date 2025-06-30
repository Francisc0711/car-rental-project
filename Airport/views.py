from django.shortcuts import render

# Create your views here.

def airport_details_view(request):
	context = {}
	return render(request, 'airport_details.html', context)
