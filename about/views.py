from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def about_me(request):
    return HttpResponse("This is a page about me. I'm learning Django and it's tricky.")