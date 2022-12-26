from django.shortcuts import redirect, render
from .models import PostModel
from .forms import PostModelForm, PostUpdateForm, CommentForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def index(request):
    posts = PostModel.objects.all()
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('App-index')
    else:
        form = PostModelForm()
    context = {
        'posts':posts,
        'form': form
    }
    return render(request, 'App/index.html', context)

def post_detail(request, pk):
    post = PostModel.objects.get(id=pk)
    print(post)
    print(pk)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = request.user
            instance.Post = post
            instance.save()
            return redirect('App-post_detail', pk=post.id)
    else:
        c_form = CommentForm()
    context = {
        'post':post,
        'c_form':c_form,
    
    }
    return render(request,'App/post_detail.html', context)

def post_edit(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('App-post_detail', pk=post.id)
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'post':post,
        'form':form,

    }
    return render(request, 'App/post_edit.html', context)
   
def post_delete(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('App-index')
    context = {
        'post': post,

    }
    return render(request, 'App/post_delete.html',context)