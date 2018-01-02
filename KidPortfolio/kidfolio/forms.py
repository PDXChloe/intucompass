from django.forms import ModelForm
from .models import KidPicPost,Portfolio
from django import forms

# class KidpicpostForm(forms.ModelForm):
#     class Meta:
#         model = KidPicPost
#         fields = ['image', 'title', 'caption', 'portfolio','category']

class KidPicForm(forms.ModelForm):
    class Meta:
        model = KidPicPost
        fields = ['image', 'title', 'caption', 'portfolio', 'category']

        widgets = {
            # 'title':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
            # 'caption':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }




class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['portfolio_name', 'author']

        widgets = {
            'portfolio_name':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
            'author': forms.HiddenInput()
        }

#need to figure out this widget, has a problem with the forms. says its undefined. perhaps need to import it. not sure from where.