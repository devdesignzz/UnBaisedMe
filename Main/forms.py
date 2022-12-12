from django import forms
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for items in choices:
    choice_list.append(items)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'question', 'category','author')
        labels = {
            'title':'Title For Your Post ',
            'question':'Body Of Your Post ',
            'category':"Post's Category "
        }

        widgets = {
            'title': forms.TextInput(attrs={'class':"form-control"}),
            'question': forms.Textarea(attrs={'class':"form-control"}),
            'category': forms.Select(choices=choices, attrs={'class':"form-control"}),
            'author': forms.TextInput(attrs={'class':"form-control", 'value':'', 'id':'current_user', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class':"form-control"})
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'question', 'category')
        labels = {'title':'Change Title ', 'question':'Update Your Question ', 'category':'Change The Post Category '} 

        widgets = {
            'title': forms.TextInput(attrs={'class':"form-control"}),
            'question': forms.Textarea(attrs={'class':"form-control"}),
            'category': forms.Select(choices=choices, attrs={'class':"form-control"}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'name', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class':"form-control"}),
            'name': forms.TextInput(attrs={'class':"form-control"}),
            'body': forms.Textarea(attrs={'class':"form-control"}),
            'author': forms.TextInput(attrs={'class':"form-control", 'value':'', 'id':'current_user', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class':"form-control"})
        }
