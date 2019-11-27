from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def getinput(request):
    return render(request,'GETINPUT.HTML.html')
def postinput(request):
    return render(request,'POSTINPUT.html')
def add(request):
    if request.method=='GET':
        try:
            x=request.GET["t1"]
            y=request.GET["t2"]
            i=int(x)
            j=int(y)
            k=i+j
            return HttpResponse("""<html><body bgcolor=cyan>sumis:"""+str(k)+"""</body></html>""")
        except(ValueError):
            return render(request,'GETINPUT.HTML.html')
    else:
        try:
            x=request.POST['t1']
            y=request.POST['t2']
            i=int(x)
            j=int(y)
            k=i+j
            return HttpResponse("<html><body bgcolor=red>sumis:"+str(k)+"</body></html>")
        except(ValueError):
            return render(request,'POSTINPUT.html')


