from django.shortcuts import render

# Create your views here.
def index(request):
    print "sadf"
    return render(request,'css/index.html')
