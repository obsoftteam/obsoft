from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'obapp/home.html')
def form(request):
    return render(request, 'obapp/form.html')
