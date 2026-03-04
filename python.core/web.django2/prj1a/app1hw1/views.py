from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime as dt

def homePage(request):
    return HttpResponse("<h1>Hello World</h1>")

def getDate(request):
    dn = dt.now()
    d = str(dn.strftime("%y/%m/%d"))
    hc = f"<h1>Date: %s</h1>" %(d)
    return HttpResponse(hc)

def getTime(request):
    dn = dt.now()
    t = str(dn.strftime("%H:%M:%S.%f"))
    hc = f"<h1>Date: %s</h1>" %(t)
    return HttpResponse(hc)

def getDateTime(request):
    dn = dt.now()
    dtn = str(dn.strftime("%y/%m/%d %H:%M:%S,%f"))
    hc = f"<h1>Date: %s</h1>" %(dtn)
    return HttpResponse(hc)
