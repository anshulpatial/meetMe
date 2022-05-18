from django.shortcuts import render,redirect
# import personal_portfolio
from personal_portfolio.models import Contact
# from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html")
# Create your views here.
def about(request):
    return render(request, "about.html")
# Create your views here.
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        number = request.POST.get('number')
        contact = Contact(name=name, email=email, message=message, number=number,)
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, "contact.html")
# Create your views here.
def resume(request):
    return render(request, "resume.html")

def projects(request):
    return render(request, "projects.html")