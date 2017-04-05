from django.shortcuts import render


# Create your views here.
def index(request):
    
    return render(request,'vuejs/index.html')

def zhiling(request):
    
    return render(request,'vuejs/zhiling.html')
def vueform(request):
    return render(request,'vuejs/zhiling.html')
 

    