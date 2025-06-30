from django.shortcuts import render

# Create your views here.

def van_details_view(request):
	context = {}
	return render(request, 'van_details.html', context)
