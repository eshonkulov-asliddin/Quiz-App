from django.shortcuts import render, redirect
from .forms import RegisterUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def registerUser(request):
    form = RegisterUserForm()

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You are successfully signed in.')
            return redirect('home')

    context = {'form': form}
    return render(request, 'account/sign_up.html', context)

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "You are logged in.")
            return redirect('quiz-card')
        else:
            print(messages.get_level(request))
            messages.error(request, 'Username or Password is incorrect!')    
    context = {}
    return render(request, 'account/sign_in.html', context)

def logoutUser(request):
    logout(request)
    messages.warning(request, "You are logged out.")   
    return redirect('home')

