from django import forms
# from tinymce.widgets import TinyMCE
from .models import Post, Comment

# class  TinyMCEWidget(TinyMCE):
#     def use_required_attribute(self, *args):
#         return False




class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(
        attrs = {
            'rows': 4,
            'placeholder': 'Add your comment',
            'id': 'demo-message'
        }
    
    ))

    class Meta: 
        model = Comment
        fields = ['content']