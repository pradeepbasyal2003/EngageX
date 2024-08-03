from django.shortcuts import render
from django.views import View
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect

def home(request):
     
     return render(request,'index.html')

# Create your views here.


def signup(request):
     if request.method == "POST":
          username = request.POST["username"]
          fname = request.POST["fname"]
          lname = request.POST["lname"]
          email = request.POST["email"]
          password = request.POST["password"]
          cpassword = request.POST["cpassword"]

          
          if password == cpassword :
               if User.objects.filter(username = username).exists():
                    messages.error(request , "the username is not available")
                    return redirect('/signup')
               
               elif User.objects.filter(email = email).exists():
                    messages.error(request , "the email is already in use")
                    return redirect('/signup')
               
               else:
                    data = User.objects.create_user(
                         first_name = fname,
                         last_name = lname,
                         email = email,
                         username = username,
                         password = password
                    )
                    data.save()
                    messages.success(request , "the account was sucessfully registered.")
                    return redirect('/account/login')
          else:
               messages.error(request , "the passwords doesn't match")
               return redirect('/signup')


     return render(request,"signup.html")




def profile(request):
     if request.method == "POST":
          username = request.POST["username"]
          email = request.POST["email"]
          channel_id = request.POST["channel_id"]
          profile_img = request.POST["profile_img"]
          description = request.POST["description"]
          data = Profile.objects.filter(user = request.user).update(
               # user = request.user,
               username = username,
               email = email,
               channel_id = channel_id,
               profile_img = profile_img,
               description = description
          )
          # data.save()
          return redirect('/account/profile')

     return render(request , 'profile.html')