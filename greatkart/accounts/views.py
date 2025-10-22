from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import account
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    form = RegistrationForm()
    print("rest")
    if request.method == 'POST':
        print("POST")
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("vaild")
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            # username = form.cleaned_data['username']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            user=account.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)   
            user.phone_number=phone_number
            user.save()
            # form.save()
            messages.success(request,'Registration successful.')
            return redirect('register')
        else:
            # Invalid form -> show errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")      
    else:
        form = RegistrationForm()
    context={'form':form}
    return render(request,'accounts/register.html',context)

def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']

        user=auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in.')
            return redirect('home')
        else:
            messages.error(request,'Invalid login credentials')
            return redirect('login')
    return render(request,'accounts/login.html')    

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request,'You are logged out.')
    return redirect('login')
    