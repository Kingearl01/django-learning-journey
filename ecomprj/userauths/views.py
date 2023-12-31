from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from django.conf import settings

from .forms import UserRegisterForm
# Create your views here.
User = settings.AUTH_USER_MODEL


def register_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f'You have already sign in')
        return redirect('core:index')

    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hey {username}. Your acount was created successfilly!")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1'])
            
            login(request, new_user)
            return redirect('core:index')
       
    else:
        form = UserRegisterForm()

    context = {
            'form': form,
        }
    
    return render(request, 'userauths/sign-up.html', context)

def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f'You have already sign in')
        return redirect('core:index')
    

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')


        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'You have successfully sign in')
            return redirect('core:index')
            
        else:
            messages.warning(request, f'User does not exist, create an account')
       

    return render(request, 'userauths/sign-in.html')


def logOut_view(request):
    logout(request)
    messages.success(request, "You have Logged Out")
    return redirect('userauths:sign-in')