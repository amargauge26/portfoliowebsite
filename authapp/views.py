from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def signup(request):
    if request.method == 'POST':
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')
        get_confirm_password = request.POST.get('pass2')
        if get_password != get_confirm_password:
            messages.info(request, 'Passwords do not match')
            return redirect("/auth/signup/")
        try:
            if User.objects.get(username=get_email):
                messages.warning(request, 'Email is Taken')
                return redirect('/auth/signup/')
        except User.DoesNotExist:
            pass
        myuser = User.objects.create_user(get_email, get_email, get_password)
        myuser.save()
        myuser = authenticate(username=get_email, password=get_password)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Successful")
            return redirect("/")
    return render(request, 'signup.html')


def handleLogin(request):
    if request.method == 'POST':
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')
        myuser = authenticate(username=get_email, password=get_password)
        if myuser is not None:
            # allowing user to log in
            login(request, myuser)
            messages.success(request, "Login Successful")
            return redirect('/')
        else:
            messages.error(request, "Invalid email or password. Please try again.")
    return render(request, "login.html")


def handleLogout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('login')
