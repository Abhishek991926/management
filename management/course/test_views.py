from django .test import TestCase,Client
from django .urls import reverse

class TestViews(TestCase):

    def test_org_page_list_POST(self):
        client= Client()
        response=client.get(reverse('orglist'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'course/org.html')
        
    def test_emp_page_list_POST(self):
        client= Client()
        response=client.get(reverse('emplist'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'course/emp.html')