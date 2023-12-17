from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# Create your views here.

def account_login(request):
    if request.user.is_authenticated:
        return redirect("portal:home")
    
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        password = request.POST.get('password')

        user = authenticate(request, username=student_id, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in")
            return redirect('portal:home')
      
    return render(request, 'account/login.html')


def account_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect('account:account_login')