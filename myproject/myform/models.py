from django.db import models
from django.forms import ModelForm
from django import forms
# Create your models here.

class Cost(models.Model):

    #id = models.AutoField(primary_key=True)
    #username = models.ForeignKey(Username, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=True)
    widgets = {
            'title': forms.TextInput(attrs={'placeholder': "How much did you spend today?"}),
            'description': forms.Textarea(attrs={'placeholder': "Describe your payment ..", 'cols': 80, 'rows': 3}),
        }


class CostForm(ModelForm):
    class Meta:
        model = Cost
        fields = '__all__'
        exclude = ['complete', 'date_of_creation', 'username']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': "How much did you spend today?"}),
            'description': forms.Textarea(attrs={'placeholder': "Describe your payment ..", 'cols': 80, 'rows': 3}),
        }