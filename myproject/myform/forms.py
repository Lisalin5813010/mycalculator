from django import forms

class BalanceForm(forms.Form):
    
    balance = forms.IntegerField(required=False)