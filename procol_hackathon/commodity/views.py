from django.shortcuts import render
from django.http import HttpResponse

from .models import Commodity

def index(request):
    if request.method == 'POST':
        commodity = request.POST.get('commodity')

        data = function(commodity)




    return HttpResponse("Hello")
