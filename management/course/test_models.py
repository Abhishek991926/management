from datetime import datetime
from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from .models import Orgdetail,Empdetail

# Create your tests here.

class OrgdetailModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.rec=Orgdetail.objects.create(name="Jaxl")


    def test_all_field_datatypes(self):
        self.assertIsInstance(self.rec.name, str)
        self.assertIsInstance(self.rec.register_on, datetime)
        self.assertIsInstance(self.rec.last_modified, datetime)


    def test_its_name_field_is_its_string_representation(self):
        self.assertEquals(str(self.rec),self.rec.name)

    def test_name_field_unique_constraint(self):
        test_name="Jaxl"
        new_org=Orgdetail(name=test_name)
        with self.assertRaises(IntegrityError):
            new_org.save()  

    def test_name_field_max_length_constraint(self):
        test_name="*"*100
        new_org=Orgdetail.objects.create(name=test_name)
        with self.assertRaises(ValidationError):
            new_org.full_clean()


class EmpdetailModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.org_for_test=Orgdetail.objects.create(name="Google")
        cls.rec=Empdetail.objects.create(name="Abhishek Kumar Yadav",orgdetail=cls.org_for_test)


    def test_all_field_datatypes(self):
        self.assertIsInstance(self.rec.name, str)
        self.assertIsInstance(self.rec.orgdetail, type(Orgdetail()))
        self.assertIsInstance(self.rec.register_on, datetime)
        self.assertIsInstance(self.rec.last_modified, datetime)

    def test_its_name_field_is_its_string_representation(self):
        self.assertEquals(str(self.rec),self.rec.name)

    def test_name_field_max_length_constraint(self):
        test_name="*"*100
        new_emp=Empdetail.objects.create(name=test_name,orgdetail=self.org_for_test)
        with self.assertRaises(ValidationError):
            new_emp.full_clean()

