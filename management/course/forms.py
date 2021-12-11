from django import forms
from .models import Orgdetail

class OrgdetailForm(forms.Form):
    name=forms.CharField(max_length=70)

class EmpdetailForm(forms.Form):
    name=forms.CharField(max_length=50)
    orgdetail=forms.ModelChoiceField(Orgdetail.objects.all(),widget=forms.Select)