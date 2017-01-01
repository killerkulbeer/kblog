from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Post
from .forms import PostForm
# Create your views here.

def posts_list(request):
    #return HttpResponse("<h1>list</h1>")
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 5)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
    "objlist" : queryset
    }
    return render(request, "postlist.html", context)


def posts_create(request):
    if not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form
    }
    return render(request, "postcreate.html", context)


def posts_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    context = {
        "instance" : instance
    }
    return render(request, "postdetail.html", context)

def posts_update(request, slug=None):
    if not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "instance" : instance,
        "form": form,
    }
    return render(request, "postedit.html", context)

def posts_delete(request, slug=None):
    if not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("posts:list")

def about(request):
    context = {}
    return render(request, "about.html", context)
