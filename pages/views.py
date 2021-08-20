from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from prometheus_client import Info
def homePageView(request):
    i = Info('my_build_version', 'Description of info')
    i.info({'version': '1.2.3', 'buildhost': 'wawawawa'})
    return HttpResponse('Hello, World!')


def helloPageView(request):
    i = Info('my_build_version222', 'Description of info')
    i.info({'version': '1.2.3', 'buildhost': 'pppp'})
    return HttpResponse('Hello, iim')
