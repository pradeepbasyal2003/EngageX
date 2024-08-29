from django.shortcuts import render
from django.views import View
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
import re



def home(request):
     
     return render(request,'index.html')

# Create your views here.

views={}


def signup(request):
     if request.method == "POST":
          username = request.POST["username"]
          fname = request.POST["fname"]
          lname = request.POST["lname"]
          email = request.POST["email"]
          password = request.POST["password"]
          cpassword = request.POST["cpassword"]

          email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$'

          if password == cpassword :
               if User.objects.filter(username = username).exists():
                    messages.error(request , "the username is not available")
                    return redirect('/signup')
               
               elif User.objects.filter(email = email).exists():
                    messages.error(request , "the email is already in use")
                    return redirect('/signup')
               
               elif not re.match(email_pattern, email):
                    messages.error(request , "the email pattern is wrong")
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
          # username = request.POST["username"]
          email = request.POST["email"]
          channel_id = request.POST["channel_id"]
          profile_img = request.POST["profile_img"]
          description = request.POST["description"]
          if email != "":
               data = Profile.objects.filter(user = request.user).update(
               # user = request.user,
               email = email,
               )
          if channel_id != "":
               data = Profile.objects.filter(user = request.user).update(
               # user = request.user,
               channel_id = channel_id,
               )
          if profile_img != "":
               data = Profile.objects.filter(user = request.user).update(
               # user = request.user,
               profile_img = profile_img,
               )
          if description != "":
               data = Profile.objects.filter(user = request.user).update(
               # user = request.user,
               description = description,
               )
          # data.save()
          return redirect('/account/profile')



     views['profile'] = Profile.objects.filter(username = request.user)
    
     return render(request , 'profile.html' ,views)


def search(request):
     if request.method == "GET":
          query = request.GET["query"]
          if query != "":
               views["search"] = Profile.objects.filter(description__icontains = query)

          elif query == "":
               redirect('/home')
                    

     views['profiles'] = Profile.objects.all()
     return render(request,'search.html' ,views)


def search_profile(request):
     if request.method == "POST":
          username = request.POST.get("username")
          views['profile'] = Profile.objects.filter(username = username)


     return render(request , 'search_profile.html' , views)


