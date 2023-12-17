from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator


from .models import *

# 3rd Party

# Create your views here.
# def count_category_usage(category):
#     return Post.objects.filter(category=category).count()

def HomePage(request):
    
    recent_posts = Post.objects.order_by('-date_created')[0:3]
    trending_posts = get_list_or_404(Post.objects.order_by('-view_count'))[0:6]
    popular_posts = get_list_or_404(Post.objects.order_by('-view_count'))[0:4]
    
    category = Category.objects.get(slug='video')
    video_posts = Post.objects.filter(category=category)
   
    context = {
        'recent_posts': recent_posts,
        'trending_posts': trending_posts,
        'popular_posts': popular_posts,
        'video_posts': video_posts,
    }
    return render(request, 'blog/index.html', context)

def Post_detail(request, year, month, slug):
    post = get_object_or_404(Post, slug=slug)
    post.view_count += 1
    post.save()
    related_posts = Post.objects.filter(category=post.category)

    context = {
        'post': post,
        'related_posts': related_posts,
            }
    return render(request, 'blog/post_detail.html', context)




def category_view(request, slug):
    try:
        # cat = Category.objects.get(slug=slug)
        cat = get_object_or_404(Category, slug=slug)
        posts_obj = Post.objects.filter(category=cat)
    except:
        pass
        posts_obj = []
    
    p = Paginator(posts_obj, 10)
    page_number = request.GET.get('page', 1)


    try:
        posts = p.get_page(page_number)
    except PageNotAnInteger:
        posts = p.page(1)
    except EmptyPage:
        posts = p.page(p.num_pages)

    context = {
        'posts': posts,
        'category': cat,
    }
    return render(request, 'blog/category.html', context)


def author_view(request, pk):
    author = Author.objects.get(pk=pk)
    posts_obj = Post.objects.filter(author=author)

    p = Paginator(posts_obj, 10)

    page_number = request.GET.get('page', 1)

    try:
        posts = p.get_page(page_number)
    except PageNotAnInteger:
        posts = p.page(1)
    except EmptyPage:
        posts = p.page(p.num_pages)
    

    context = {
        'posts': posts,
        'author': author,
    }
    return render(request, 'blog/author.html', context)