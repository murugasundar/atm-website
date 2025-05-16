from app1.models import ATM
from django import forms


class Bankform(forms.ModelForm):
    class Meta:
        model=ATM
        fields=['name','acc','ifsc','mobile','password','balance']


class acc_pass(forms.ModelForm):
    class Meta:
        model=ATM
        fields=['acc','password']
        

class amount(forms.Form):
    amount=forms.IntegerField()


class pin_form(forms.Form):
    new_password = forms.CharField( max_length=10)
