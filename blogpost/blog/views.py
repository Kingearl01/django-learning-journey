from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect

from next_prev import next_in_order, prev_in_order

from .models import Post, Comment, Author, PostView
from .form import CommentForm, PostCreationForm
from marketing.models import SignUp
# Create your views here.

# Global variables
queryset= Post.objects.all()
latest = queryset.order_by('-timestamp')[0:3]

def get_categery_count():
    queryset = Post \
        .objects \
        .values('categories__title') \
        .annotate(Count('categories__title'))
    return queryset

category_count = get_categery_count()

def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


def search(request):
    queryset= Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset,
    }
    return render(request, 'blog/search.html', context)



def index(request):
    featured = queryset.order_by('-timestamp').filter(featured=True)[0:3]
    latest = queryset.order_by('-timestamp')[0:3]
    context = {
        'posts': queryset,
        'featured': featured,
        'latest': latest
    }

    if request.method == "POST":
        email = request.POST['email']
        new_signing = SignUp()
        new_signing.email = email
        new_signing.save()

    return render(request, 'blog/index.html', context)

def blog(request):
    
    paginator = Paginator(queryset, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginator_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginator_queryset = paginator.page(1)

    except EmptyPage:
        paginator_queryset = paginator.page(paginator.num_pages )
    
    

    context = {
        'posts': paginator_queryset,
        'latest': latest,
        'page_request_var': page_request_var,
        'category_count': category_count
        }

    

    return render(request, 'blog/blog.html', context)


def post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.user.is_authenticated:
        PostView.objects.get_or_create(user=request.user, post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            user = request.user
            comment = Comment(
                user=user,
                post=post,
                content = form.cleaned_data['content']
            )

            comment.save()
            return redirect('post-detail', id=id)
    else:
        form = CommentForm()
    context = {
        'form': form,
        'post': post,
        'category_count': category_count,
        'latest': latest
    }

  
    return render(request, 'blog/post.html', context)
    """
    next and prevoius post
    """
    # try:
    #     prev_post = post.get_previous_by_timestamp() if hasattr(post, 'get_previous_by_timestamp') else None
    # except Post.DoesNotExist:
    #     prev_post = post

    # try:
    #     next_post = post.get_next_by_timestamp() if hasattr(post, 'get_next_by_timestamp') else None
    # except Post.DoesNotExist:
    #     next_post = post

def post_create(request):
    if request.method == "POST":
        form = PostCreationForm(request.POST, request.FILES)
        author = get_author(request.user)
        if form.is_valid():
            form.instance.author = author
            new_post = form.save()
            return redirect('post-detail', id=new_post.id)
    else:
        form = PostCreationForm()    
    
    context = {
        'form': form

    }
    return render(request, 'blog/create_post.html', context)

def post_update(request, id):
    pass


def post_delete(request, id):
    pass
   



