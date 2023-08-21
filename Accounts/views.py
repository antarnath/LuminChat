"""
View configuration for the 'accounts' app.
"""
from django.shortcuts import render

# Create your views here.
def register(request):
    """
    Register a user.
    """
    return render(request, 'Accounts/register.html')

def signin(request):
    """
    Signin a user.
    """
    return render(request, 'Accounts/signin.html')
