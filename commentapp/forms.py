from django.forms import ModelForm

from articleapp.models import Article
from commentapp.models import Comment


class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
