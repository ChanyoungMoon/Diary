from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content',)
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'title',
                    'placeholder': '제목',
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'content',
                    'placeholder': '일기',
                }
            ),
        }


