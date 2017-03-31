from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def angularindex(request):
    print "asjkdf"
    print "sdaf"
  
    print "sadf"
  #  print t
    return render(request,'angular/index.html')
def angular1(request):
    print "1111"
    return render(request,'angular/angular1.html')

def angular4(request):
    return render(request,'angular/angular4.html')
