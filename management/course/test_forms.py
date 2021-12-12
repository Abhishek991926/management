from django.test import TestCase
from .models import Orgdetail
from .forms import OrgdetailForm,EmpdetailForm


class OrgdetailFormTest(TestCase):
    def test_valid_forms(self):
        form_data={'name':'Jaxl'}
        form=OrgdetailForm(data=form_data)
        self.assertTrue(form.is_valid())
    

class EmpdetailFormTest(TestCase):
    def test_valid_forms(self):
        rec=Orgdetail.objects.create(name="Jaxl")
        form_data={'name':'Abhishek Kumar Yadav','orgdetail':rec}
        form=EmpdetailForm(data=form_data)
        self.assertTrue(form.is_valid())

    