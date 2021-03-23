from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from blog.models import Post
# Create your views here.
def home(request):
    return render(request,'home/index.html')

def about(request):
    return render(request,'home/about.html')

def search(request):
    query=request.GET['query']
    if len(query)>73 or len(query)==0:
        post=Post.objects.none()
    else:
        postTitle=Post.objects.filter(title__icontains=query)
        postContent=Post.objects.filter(content__icontains=query)
        postAuthor=Post.objects.filter(author__icontains=query)
        posts=postTitle.union(postContent)
        post=posts.union(postAuthor)
    if len(post)==0:
        messages.warning(request,'No search results found. Please write correct keyword.')
    context={'allposts':post,'query':query}
    return render(request,'home/search.html',context)

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']

        if len(name)<1 or len(phone)<10 or len(email)<5 or len(subject)<1 or len(message)<2:
            messages.error(request,'Please fill the form correctly!')
        else:
            contact=Contact(name=name,phone=phone,email=email,subject=subject,message=message)
            contact.save()
            messages.success(request,'Form Submitted')
    return render(request,'home/contact.html')

def handleSignup(request):
    if request.method=="POST":
        # Get all details
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        #Checks
        if len(username)>20:
            messages.error(request,"Username must be under 20 characters")
            return redirect('/')
        if password1!=password2:
            messages.error(request,"Passwords do not match")
            return redirect('/')

        #database storage
        myuser=User.objects.create_user(username,email,password1)
        myuser.first_name=firstname
        myuser.last_name=lastname
        myuser.is_staff=True
        myuser.save()
        messages.success(request,"Your account has been successfully created")
        return redirect('/')
    else:
        return HttpResponse("404 NOT FOUND")

def handleLogin(request):
    if request.method=="POST":
        user=request.POST['user']
        mypass=request.POST['password']

        myuser=authenticate(username=user,password=mypass)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Sucessfully Logged In")
            return redirect('/')
        else:
            messages.error(request,"Invalid credentials, Please try again!")
            return redirect('/')
    return HttpResponse("404 NOT FOUND")


def handleLogout(request):
    logout(request)    
    messages.success(request,"Sucessfully Logged Out")    
    return redirect('/')