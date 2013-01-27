# coding: utf-8

#from django.http import HttpResponse
#from django.template import loader, Context

from django.views.generic.simple import direct_to_template

def homepage(request):
    return  direct_to_template(request, template='index.html')
