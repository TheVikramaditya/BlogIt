from django.shortcuts import render,redirect,get_object_or_404
from . models import Blog
from . forms import CreateBlog

# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required 


@login_required
def ListBlogs(request):
    if request.user.is_superuser:
        blogs = Blog.objects.all()
    else:
        blogs = Blog.objects.filter(user=request.user)
    return render(request,'blogs/list.html',{"blogs":blogs})

@login_required
def PostBlog(request):
    if request.method=="POST":
        form = CreateBlog(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('/blog/')
    else:
        form = CreateBlog()
    
    return render(request,"blogs/post-blog.html",{"form":form})


@login_required
def BlogDetail(request,pk):
    if request.user.is_superuser:
        blogs = Blog.objects.get(pk=pk)
    else:
        blogs = Blog.objects.get(user=request.user,pk=pk)
    return render(request,'blogs/blog-detail.html',{"blog":blogs})

@login_required
def BlogUpdate(request,pk):
    blog = get_object_or_404(Blog,pk=pk)
    if request.method == "POST":
        form = CreateBlog(request.POST,instance=blog)
        if form.is_valid():
            form.save(user=request.user)
            messages.success(request,"Successfully updated")
    else:
        form = CreateBlog(instance=blog)
    return render(request,'blogs/updateblog.html',{"form":form})

@login_required
def BlogDeleteConfirmation(request,pk):
    blog = get_object_or_404(Blog,pk=pk)
    return render(request,'blogs/delete-confirmation.html',{"blog":blog})

@login_required
def BlogDelete(request,pk):
    blog = get_object_or_404(Blog,pk=pk)
    blog.delete()
    return redirect('/blog/')