from urllib import response
from django.test import TestCase
from django.urls import reverse
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from authentication.models import User
from ..utilitis import account_token_generation


class AuthTest(TestCase):
    
    def setUp(self):
        User.objects.create_user(email='cs.ttrx@gmail.com', user_name='csttrx', password='coull1515fdf')
        self.superuser = User.objects.create_superuser('coul@gmail.com', user_name='cscoul', password='godejeroien583')

    def test_register_view_url_accessibility(self):
        response = self.client.get('/auth/register')
        response1 = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response1.status_code, 200)
    
    def test_register_view_post(self):
        response = self.client.post(
            reverse('register'), 
            data={'email':'cccc@gmail.com',
            'user_name':'csttrx', # will fail for user_name is unique field
            'password1':'vkjoierjio7', 'password2':'vkjoierjio7'})
        self.assertEqual(response.status_code, 200)
        self.failUnless(response.context['register_form'])
        self.failUnless(response.context['register_form'].errors)
        self.assertEqual(User.objects.count(), 2)

        response = response = self.client.post(
            reverse('register'), 
            data={'email':'cccc@gmail.com', 
            'user_name':'coul',
            'password1':'vkjoierjio7', 'password2':'vkjoierjio7'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 3)
    
    def test_activation_view(self):
        user = User.objects.get(user_name='csttrx')
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = account_token_generation.make_token(user)
        self.assertEqual(user.email, 'cs.ttrx@gmail.com')
        response = self.client.get(reverse('activate', args=[uid ,token]))
        self.assertEqual(response.status_code, 200)
        user = User.objects.get(user_name='csttrx')
        self.assertTrue(user.is_active)

    def test_login_view(self):
        # response = self.client.post(reverse('login'), data={'email':'c.ttrx@gmail.com','password':'coull1515fdf'})
        # self.assertNotEqual(str(response.context['user']), 'csttrx' )
        # response = self.client.post(reverse('login'), data={'email':'coul@gmail.com','password':'godejeroien583'})
        # self.assertEqual(str(response.context['user']), 'cscoul' )
        self.assertTrue(self.superuser.is_active)
        login = self.client.login(email = self.superuser.email, password = self.superuser.password)
        #self.assertTrue(login)