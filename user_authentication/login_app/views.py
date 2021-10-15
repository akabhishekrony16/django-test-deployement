from django.shortcuts import render
from login_app.forms import UserForm,UserProfileform
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'login_app/index.html')


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileform(request.POST,request.FILES)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()#saving the user form to the database and grabbing it from the database
            user.set_password(user.password)#hashing the password
            user.save()


            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profle_pic' in request.FILES:#request.FILES grabs image from form
                profile.profle_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:

            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileform()

    return render(request,'login_app/registration.html',
    {'user_form':user_form,
    'profile_form':profile_form,
    'registered':registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return render(request,'login_app/index.html')
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            return HttpResponse("invalid login details supplied!")
    else:
        return  render(request,'login_app/login.html')

@login_required
def user_logout(request):
    logout(request)
    return render(request,'login_app/index.html')

@login_required
def other_page(request):
    return HttpResponse('Logged In!')
