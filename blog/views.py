from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Category, Author, Comment
from .forms import CommentForm
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages


def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

def homepage_views(request):
    post_list = Post.objects.all().order_by('-published')
    paginator = Paginator(post_list, 2) # Show x post per page.
    post_number = request.GET.get('page')
    post = paginator.get_page(post_number)
    category = Category.objects.all()

    context = {
        'post': post,  
        'category': category
    }
    return render(request, 'index.html', context)

def post_views(request, slug, id):
    post = Post.objects.get(slug=slug, id=id)
    comment = Comment.objects.all()
    
    new_comment = None
    if request.method == "POST":
        form = CommentForm(request.POST or None)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            comment = CommentForm()
            messages.success(request, 'The form is valid.')
            return HttpResponseRedirect(reverse('post', kwargs={'slug': slug, 'id': id}))
    else:
        form = CommentForm()
    context = {
        'post': post,
        'comment': comment,
        'form': form,
        'new_comment': new_comment
    }
    return render(request, 'single.html', context)



def category_views(request, slug):
    category = get_object_or_404(Category, slug=slug)
    post = Post.objects.filter(category=category)

    context = {
        'category': category,
        'post': post
    }
    return render(request, 'category.html',context)