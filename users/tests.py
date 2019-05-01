from django.test import TestCase
from django.test import Client
from django.urls import reverse, resolve

from .forms import UserForm
from .models import CustomUser

# Create your tests here.
class Setup_Class(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(email='user@mp.com', password='user',
                                              first_name='user', phone='12345678')


class User_Form_Test(TestCase):

    # Valid Form Data
    def test_UserForm_valid(self):
        form = UserForm(data={'email': 'user@mp.com', 'password': 'user',
                              'first_name': 'user', 'phone': '12345678'})
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = UserForm(data={'email':'', 'password':'', 'first_name':'mp', 'phone':''})
        self.assertFalse(form.is_valid())


class User_Views_Test(Setup_Class):

    def test_home_view(self):
        user_login = self.client.login(email='user@mp.com', password='user')
        self.assertTrue(user_login)
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 302)

    def test_add_user_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    # Invalid data
    def test_add_user_invalidform_view(self):
        response = self.client.post(reverse('signup'),
                                    {'email': 'admin@mp.com', 'password': '', 'first_name': 'mp',
                                     'phone':'12345678'})
        self.assertTrue('"error": true' in response.content)

    # Valid data
    def test_add_admin_form_view(self):
        user_count = CustomUser.objects.count()
        response = self.client.post(reverse('signup'),
                                    {'email': 'user@mp.com', 'password':'user', 'first_name':'user'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(CustomUser.objects.count(), user_count+1)
        self.assertTrue('"error": false' in response.content)


