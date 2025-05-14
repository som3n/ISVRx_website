from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "main/index.html")
    
def about(request):
    return render(request, "main/about.html")

def training(request):
    return render(request, "main/training.html")

def join(request):
    return render(request, "main/index.html")

def contact(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(firstname=firstname, lastname=lastname, subject=subject, email=email, message=message)
        contact.save()
        
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')  # Redirect to the contact page or another page

    return render(request, "main/contact.html")