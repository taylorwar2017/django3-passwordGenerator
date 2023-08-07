from django.shortcuts import render
from django.http import HttpResponse
import random

# Create home page
def home(request):
    return render(request, "generator/home.html", {"password": "jkfld"})

def password(request):

# Define a list of charachters
    charachters = list("abcdefghijklmnopqrstuvwxyz")
    
# If statements that appends charachters based on user input
    if request.GET.get("uppercase"):
        charachters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get("special"):
        charachters.extend(list("!@#$%&"))
    if request.GET.get("numbers"):
        charachters.extend(list("1234567890"))
    
# Define the length of the password as the input from the user request
    length = int(request.GET.get("length", 12))

# Define thepassword as an empty string
    thepassword = ""

# For loop to generate random password based on charachter string
    for x in range (length):
        thepassword += random.choice(charachters)
    return render(request, "generator/password.html", {"password": thepassword})

