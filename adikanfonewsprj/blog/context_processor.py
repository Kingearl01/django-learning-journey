from django.shortcuts import get_list_or_404
from django.db.models import Count

from blog.models import Category, Post


def default(request):
    latest_posts = Post.objects.order_by('-date_created')[0:6]
    featured_posts = Post.objects.filter(featured=True).order_by('-date_created')[0:6]
    trending_post = get_list_or_404(Post.objects.order_by('-view_count'))[0:2]
    categories = Category.objects.annotate(post_count=Count('category'))
    

    # footer
    category = Category.objects.filter(slug='campus-news')
    featured_posts_footer = Post.objects.filter(featured=True).order_by('-date_created')[0:3]
    campus_posts = Post.objects.order_by('-date_created').filter(category__in=category)
    
    context = {
        'latest_posts': latest_posts,
        'featured_posts': featured_posts,
        'trending_post': trending_post,
        'categories': categories,
        'featured_posts_footer': featured_posts_footer,
        'campus_posts': campus_posts
    }
    return context