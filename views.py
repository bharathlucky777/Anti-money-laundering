from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def bankregister(request):
    return render(request, 'bankregister.html')

def userregister(request):
    return render(request, 'userregister.html')

# def banklogin(request):
#     return render(request, 'banklogin.html')

# def userlogin(request):
#     return render(request, 'userlogin.html')