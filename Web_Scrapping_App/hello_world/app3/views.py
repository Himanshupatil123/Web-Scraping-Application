from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.urls import reverse
from django.contrib.auth import login as login_func
import datetime
from django.contrib import auth
from django.contrib.auth.models import User
from app1.models import WishList
from django.contrib import messages
# Create your views here.


flag=False

@login_required(login_url='login')
def homepage(request):
    return redirect('home page')
    #return render(request, 'login.html', {'flag': flag})
def login(request):

    global flag

    print("Flag="+str(flag))
    if flag=='True':
        return redirect('home page')

    if request.method == 'POST':
        username1 = request.POST['uname']
        password1 = request.POST['psw']

        print("I am in Login Page")
        print(username1)
        print(password1)


        from django.contrib import auth
        x = auth.authenticate(username=username1, password=password1)
        if x is None:
            return redirect('login')

        else:
            print("BOSS")
            flag=True
            auth_table_field=User.objects.get(username=username1).pk
            print("AAuth table_field=",auth_table_field)

            # field=User.objects.get_by_natural_key(pk=auth_table_field)

            obj=get_object_or_404(User,pk=auth_table_field)

            login_func(request,obj)
            #updating the login time and date fields
            # current_date=datetime.date.today()
            current_time=datetime.datetime.now()
            #
            # print("current_date:",current_date)
            print("current_datetime",current_time)

            # obj.last_login_date=current_date
            obj.last_login=current_time
            obj.save()
            if obj.username=="Admin":
                return redirect('admin_user')


            param1=''+obj.username
            param2=''+obj.email
            url=reverse('home page')
            url_with_params=f'{url}?param1={param1}&param2={param2}'
            return redirect(url_with_params)


            #return redirect('home page')
            #return render(request,'index.html',{'Username':username1})
            # #return render(request,'index.html',{'titles':'Django o','link':' http://127.0.0.1:8000/home'})

    else:
        return render(request,'login.html')


@login_required(login_url='login')
def admin_user(request):
    username1="Admin"

    user_data = User.objects.all()

    context = {
        'user': user_data,
    }

    print(user_data)
    for i in user_data:
        print(i.username)
        print(i.email)
        print(i.last_login)
        # print(i.last_login_date)
        # print(i.last_login_time)
    # print(user_data.username)
    # print(user_data.last_login_date)
    # print(user_data.last_login_time)

    return render(request,'admin_home.html',context)


@login_required(login_url='login')
def delete(request,id):
    user_data=User.objects.filter(id=id)
    user_data.delete()
    context={
        'user':user_data,
    }
    return redirect('admin_user')

@login_required(login_url='login')
def delete_admin_wish(request,id):
    wish=WishList.objects.filter(id=id)
    wish.delete()

    return redirect('admin_wishlist')



@login_required(login_url='login')
def admin_wishlist(request):
    wish = WishList.objects.all()

    context = {
        'wish': wish,
    }

    return render(request, 'admin_wishlist.html', context)
    #
    # return render(request,'')


def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password = request.POST['psw']

        print(username)
        print(email)


        if User.objects.filter(username=username).exists():
            messages.error(request,'Username Already Exist')
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.error(request,'Email Already Exist')
            return redirect('signup')

        data = User.objects.create_user(username=username, email=email, password=password)
        data.save()
        messages.success(request, 'Success')
        return render(request, 'login.html')

        #return redirect('http://127.0.0.1:8000')

    return render(request,'b.html')

def forgot_password(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']


        print(username)
        print(email)


        if User.objects.filter(username=username).exists():
            auth_table_field = User.objects.get(username=username).pk

            users = User.objects.get(pk=auth_table_field)

            print("Hello")

            print("users.username", users.username)
            print("users.email", users.email)

            if users.username == username:
                if users.email == email:
                    users.set_password(password)
                    users.save()
                    print("I am in")
                    return redirect('login')
                # else:
                #     messages.error(request, 'Username and Email is not matching')
                #     print("I am out")
                #     return redirect('forgot_password')

            print("World")
            messages.error(request, 'Username and Email is not matching')
        else:
            messages.error(request, 'Username and Email is not matching')
            return render(request, 'forgot_password.html')

    return render(request, 'forgot_password.html')



def logout(request):
    auth.logout(request)
    return redirect('login')
