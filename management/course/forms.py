from django import forms
from .models import Orgdetail

class OrgdetailForm(forms.Form):
    name=forms.CharField()

class EmpdetailForm(forms.Form):
    name=forms.CharField()
    orgdetail=forms.ModelChoiceField(Orgdetail.objects.all(),widget=forms.Select)