from .models import Review
from .models import Post
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content','featured_image',)
