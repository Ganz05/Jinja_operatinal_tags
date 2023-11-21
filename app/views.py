from django.shortcuts import render

# Create your views here.
def operation(request):
    d={'a':400,'b':2340,'c':154}
    return render(request,'operation.html',d)
