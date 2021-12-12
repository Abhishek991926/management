from django .test import SimpleTestCase
from django.urls import reverse,resolve
from course .views import org_page,emp_page


class TestUrls(SimpleTestCase):
    def test_orglist_url_is(self):
        # Test that when the /orglist url is hit, it serves back the org_page view only.
        # org_page() from the view is responsible for serving the content of the org list page
        url=reverse('orglist')
        self.assertEquals(resolve(url).func,org_page)

    def test_emplist_url_is(self):
        url=reverse('emplist')
        self.assertEquals(resolve(url).func,emp_page)
    
