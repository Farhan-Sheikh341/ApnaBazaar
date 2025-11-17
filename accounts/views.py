from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse


# Create your views here.

def login_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = email)

        if not user_obj.exists():
            messages.error(request, "user not found")
            return HttpResponseRedirect(request.path_info)

        
        user_obj = authenticate(username = email , password= password)
            
        if user_obj:
            login(request,user_obj)
            return redirect('/')
        
        messages.error(request,"Invalid Credential")
        return HttpResponseRedirect(request.path_info)


    return render(request,'accounts/login.html')

def logout_page(request):
    logout(request)
    return redirect('/')


def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = email)

        if user_obj.exists():
            messages.error(request,'Email has already been taken!')
            return HttpResponseRedirect(request.path_info)
        
        user_obj = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            username = email
            )
        
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request, "Account created successfully!")
        return redirect('/accounts/login/')

    return render(request,'accounts/register.html')
