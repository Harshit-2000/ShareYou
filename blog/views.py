from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from . import forms

from .models import Photo, Blog
from blog import models
# Create your views here.


@login_required(login_url='login')
def home_view(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog/home.html', context)


@login_required(login_url='login')
def upload_blog_view(request):
    image_form = forms.ImageUploadForm()
    blog_form = forms.BlogUploadForm()
    if request.method == 'POST':
        image_form = forms.ImageUploadForm(request.POST, request.FILES)
        blog_form = forms.BlogUploadForm(request.POST)
        if all([blog_form.is_valid(), image_form.is_valid()]):
            photo = image_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            blog = blog_form.save(commit=False)
            blog.image = photo
            blog.author = request.user
            blog.save()
            return redirect('home')

    context = {
        'image_form': image_form,
        'blog_form': blog_form,
    }

    return render(request, 'blog/image_upload.html', context)


@login_required(login_url='login')
def blog_view(request, id):
    blog = get_object_or_404(models.Blog, id=id)

    context = {
        'blog': blog
    }

    return render(request, 'blog/blog.html', context)


@login_required(login_url='login')
def edit_delete_view(request, id):
    blog = get_object_or_404(models.Blog, id=id)

    if (request.user != blog.author):
        return redirect('view_blog', id=id)

    editForm = forms.BlogEditForm(instance=blog)
    deleteForm = forms.BlogDeleteForm()
    if request.method == 'POST':
        if 'edit_blog' in request.POST:
            editForm = forms.BlogEditForm(request.POST, instance=blog)
            if editForm.is_valid():
                editForm.save()
                return redirect('view_blog', id=id)
        if 'delete_blog' in request.POST:
            deleteForm = forms.BlogDeleteForm(request.POST)
            if deleteForm.is_valid():
                blog.delete()
                return redirect('view_blog', id=id)
    context = {'delete_form': deleteForm, 'edit_form': editForm, 'blog': blog}
    return render(request, 'blog/edit_delete.html', context)
