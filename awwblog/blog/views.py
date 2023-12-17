from django.db.models import Count,Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect

from .models import *
from .forms import CommentForm

from taggit.models import Tag
# Create your views here.
def post_list(request, tag_slug=None):
    posts = Post.published.all()

    paginator = Paginator(posts, 10)
    page = request.GET.get('page', 1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page is out of range deliver last page of results-
        posts = paginator.page(paginator.num_pages)
    
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
    # serach
    query =request.GET.get('q')
    if query:
        posts = Post.published.filter(Q(title__icontains=query) | Q(tags__name__icontains=query)).distinct()
   
    context = {
        'posts': posts,
        'page': page,
        'tag': tag
    }

    return render(request, 'blog/post_list.html', context)

def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create comment object but dont save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            # redirect to same page and focus on that comment
            return redirect(post.get_absolute_url()+'#'+str(new_comment.id))
    else:
        comment_form = CommentForm()

     # list of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:6]
    context = {
        'post': post,
        'comment_form': comment_form,
        'similar_posts': similar_posts,
    }
    return render(request, 'blog/post_detail.html', context)


def reply_page(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            post_id = request.POST.get('post_id')
            parent_id = request.POST.get('parent')
            post_url = request.POST.get('post_url')

            reply = form.save(commit=False)

            reply.post = Post(id=post_id)
            reply.parent = Comment(id=parent_id)
            reply.save()

            return redirect(post_url+'#'+str(reply.id))

    return redirect('/')