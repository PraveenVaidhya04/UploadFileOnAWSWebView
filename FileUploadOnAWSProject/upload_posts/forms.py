from django import forms
from .models import Posts


class PostsForm(forms.ModelForm):
    title = forms.CharField(label="Name", widget=forms.TextInput(attrs={"placeholder": "Posts Name"}))
    file = forms.FileField(label="File", widget=forms.FileInput(attrs={"placeholder": "Posts File"}))

    class Meta:
        model = Posts
        fields = ('title', 'file')

