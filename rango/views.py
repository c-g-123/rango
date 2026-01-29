from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


def index(request):
	about_relative_url = reverse('rango:about')
	about_absolute_url = request.build_absolute_uri(about_relative_url)
	return HttpResponse('Rango says hey there partner! <a href="' + about_relative_url + '">About</a>.')

def about(request):
	index_relative_url = reverse('rango:index')
	index_absolute_url = request.build_absolute_uri(index_relative_url)
	return HttpResponse('Rango says here is the about page. <a href="' + index_relative_url + '">Index</a>.')