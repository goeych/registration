from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
#from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
# Create your views here.


def mainPage(request):

    context={}
    return render(request,'appRegister/main.html',context)


    
def loginPage(request):
    page = 'login'

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        print('user:',user)

        if user is not None:
            login(request,user)
            

    context={'page':page}
    return render(request,'appRegister/login_register.html',context)


def signupPage(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user = authenticate(request,username=user.username,password=request.POST['password1'])
            if user is not None:
                login(request,user)
                return redirect('mainPage')
            
    context={'form':form,'page':page}
    return render(request,'appRegister/login_register.html',context)


def logoutPage(request):
    logout(request)
    return redirect('login')
