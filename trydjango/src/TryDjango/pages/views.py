from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def home_view(request, *args, **kwargs):
	return render(request, "home.html", {})

 
def about_view(request, *args, **kwargs):
	my_context = {
		"this_is_true": True,
		"my_text":"This is 1",
		"my_text2": "This is 2",
		"my_list": [3, 399, "numbers"]
	}
	return render (request, "about.html", my_context)


def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})