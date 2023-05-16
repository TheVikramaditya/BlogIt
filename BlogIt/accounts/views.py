from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .forms import CreateUserForm,LogInForm
from django.contrib import messages
# Create your views here.



def SignUp(request):
    if request.user.is_authenticated:
        return redirect('/blog/')
    else:
        if request.method=="POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Account has been created successfully !')
        else:
            form = CreateUserForm()
        return render(request,'accounts/signup.html',{'form':form})

def LogIn(request):
    if request.user.is_authenticated:
        return redirect('blogs:list-blogs')
    else:
        if request.method=="POST":
            form=LogInForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username,password=password)
                if user:
                    login(request,user)
                    messages.success(request,"Logged in successfully")
                    return HttpResponseRedirect('/blog/')
        else:
            form = LogInForm()
        return render(request,'accounts/login.html',{'form':form})

def LogOut(request):
    logout(request)
    return redirect('/')