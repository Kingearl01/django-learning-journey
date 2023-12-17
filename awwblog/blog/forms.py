from django.forms import ModelForm

from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

    # overriding defaults form settings and adding bootstrap class
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'placeholder': 'Enter name',
            'class': 'form-control',
        }
        self.fields['email'].widget.attrs = {
            'placeholder': 'Enter email',
            'class': 'form-control',
        }
        self.fields['body'].widget.attrs = {
            'placeholder': 'Comment here...',
            'class': 'form-control',
        }