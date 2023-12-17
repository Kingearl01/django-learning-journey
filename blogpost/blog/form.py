from django import forms
# from tinymce import TinyMCE
from .models import Comment, Post

# class TinyMCEWidget(TinyMCE):
#     def use_required_attribute(self, *args):
#         return False

# class PostForm(forms.ModelForm):
#     content = forms.CharField(
#         widget=TinyMCEWidget(
#             attrs={
#                 'required': False,
#                 'cols': 30,
#                 'rows': 10,
#             }
#         )
#     )

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # exclude = ['view_count', 'comment_count', 'author']
        # fields = ['title', 'overview', 'content', 'thumbnail', 'categories', 'featured']

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Your comment here',
        'class': 'form-control',
        'id': 'username',
        'rows': '4',
    }))
    class Meta:
        model = Comment
        fields = ["content",]
        # exclude = ['content']
