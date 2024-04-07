from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable':'this is sent',
        'variable2':'request found'
    }
    return render(request,'index.html', context)
    #return HttpResponse("this is homepage")

def contact(request):
    return HttpResponse('this is contact page')

def service(request):
    return HttpResponse('this is service page')

def about(request):
    return HttpResponse('this is about page')
    

