from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Blog
from .forms import BlogForm


def index(request):
	blog_posts = Blog.objects.all()
	context = {
		'lists_posts': blog_posts,
	}
	return render(request, 'blogapp/index.html', context)

def create(request):
	form = BlogForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	
	context = {
		'form': form
	}
	return render(request, 'blogapp/blog_form.html', context)

def post_detail(request, id=None):
	post = get_object_or_404(Blog, id=id)
	context = {
		'post': post
	}
	return render(request, 'blogapp/details.html', context)

def post_update(request, id=None):
	instance = get_object_or_404(Blog, id=id)
	form = BlogForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Updated")
		return HttpResponseRedirect(instance.get_absolute_url())
	
	context = {
		'instance': instance,
		'form': form,
	}
	return render(request, 'blogapp/blog_form.html', context)

def edit(request):
	return HttpResponse("<h1>edit</h1>")

def delete(request, id=None):
	instance = get_object_or_404(Blog, id=id)
	instance.delete()
	messages.success(request, "Successfully Deleted")
	return redirect('blogapp:index')