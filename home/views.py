from django.shortcuts import render,redirect
from django.contrib import messages
from .models import userinfo
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import cache_control
# Create your views here.



@cache_control(no_cache = True,must_revaliddate = True,no_store = True)
def index(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == 'POST':
            name = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = name , password = password)

            if user is not None:
                login(request,user)
                return redirect("home")
            messages.error(request,'invalid username')
            return redirect('index')
            
        else:
            return render(request,'index.html')



@cache_control(no_cache = True,must_revaliddate = True,no_store = True)
def home(request):
    """home page"""
    if request.user.is_authenticated:
        return render(request,"home.html")
    else:
        return redirect("index")


def user_logout(request):
    """delete session"""
    logout(request)
    return redirect("index")












# user = authenticate(username = username , password = password)

            # try:
            #     table_value = userinfo.objects.get(name = username)
            # except userinfo.DoesNotExist:
            #     messages.error(request,'invalid username')
            #     return redirect('index')
            # else:
            #     if password == table_value.password:
                    
            #         request.session['username'] = username
            #         return redirect("home")
            #     else:
            #         messages.error(request,'invalid password')
            #         return redirect('index')