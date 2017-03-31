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