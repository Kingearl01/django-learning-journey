from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView



from .models import Post, Author, Category
# Create your views here.

class HomeView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/index.html'

    # def get_queryset(self):
    #     return Post.objects.all().order_by('-published')

    def get_ordering(self):
        return ['-published']
    
class CatListView(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        context = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category'])
        }
        print(context)
        return context

def get_category_list(retquest):
    category_list = Category.objects.all()
    context = {
        'category_list': category_list
    }

    return context

class DetailPostView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'
    # success_url = 'home'

class CreatePostView(CreateView):
    model = Post
    fields = ['title', 'thumbnail', 'body']
    template_name = 'blog/add_post.html'
    # success_url = reverse('blog:post-detail')

    def form_valid(self, form):
        author = Author.objects.get(user=self.request.user)
        form.instance.created_by = author
        return super().form_valid(form)

class UpdatePostView(UpdateView):
    model= Post
    template_name = 'blog/update_post.html'
    fields = ['title', 'thumbnail', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog:home')