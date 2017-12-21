from django.forms import ModelForm
from .models import KidPicPost

# class KidpicpostForm(forms.ModelForm):
#     class Meta:
#         model = KidPicPost
#         fields = ['image', 'title', 'caption', 'portfolio','category']

class KidPicForm(ModelForm):
    class Meta:
        model = KidPicPost
        fields = ['image', 'title', 'caption', 'portfolio', 'category']


