from django.shortcuts import render, HttpResponse, redirect
from .models import Post, BlogComment
from django.contrib import messages
from blog.templatetags import extras

# Create your views here.
def blogHome(request):
    allposts=Post.objects.all()
    context={"allposts":allposts}
    return render(request,'blog/blogHome.html',context)

def blogPost(request, slug):
    post=Post.objects.filter(slug=slug).first()
    post.views=post.views+1
    post.save()
    comments=BlogComment.objects.filter(post=post,parent=None)
    replies=BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.serialNo not in replyDict.keys():
            replyDict[reply.parent.serialNo]=[reply]
        else:
            replyDict[reply.parent.serialNo].append(reply)

    context={"post":post,"comments":comments,"user":request.user,"replyDict":replyDict}
    return render(request,'blog/blogPost.html',context)

def postComment(request):
    if request.method=="POST":
        comment=request.POST.get("comment")
        user=request.user
        serialNo=request.POST.get('serialNo')
        post=Post.objects.get(serialNo=serialNo)
        parentSerialNo=request.POST.get('parentserialNo')

        if parentSerialNo=="":
            comm=BlogComment(comment=comment,user=user,post=post)
            comm.save()
            messages.success(request,"Your comment has been posted successfully")
        else:
            parent=BlogComment.objects.get(serialNo=parentSerialNo)
            comm=BlogComment(comment=comment,user=user,post=post,parent=parent)
            comm.save()
            messages.success(request,"Your reply has been posted successfully")
        
    return redirect('/blog/'+post.slug)