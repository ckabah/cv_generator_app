from cgitb import reset
from django.test import TestCase
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from authentication.models import User
from ..utilitis import account_token_generation
from django.contrib.auth.tokens import default_token_generator

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
        response = self.client.post(reverse('login'), data={'email':'cs.ttrx@gmail.com','password':'coull1515fdf'})
        self.assertEqual(response.status_code, 404 ) # will for account acctivation
        response = self.client.post(reverse('login'), data={'email':'coul@gmail.com','password':'godejeroien583'})
        self.assertEqual(response.status_code, 302 ) # superuser have a active account, so test will be successfully
        self.assertEqual(response.url, reverse('dashbord'))# logged user name
        login = self.client.login(user_name='coul@gmail.com', password = 'godejeroien583') # user name field is user_name
        self.assertTrue(login)

    def test_password_reset_viwew(self):
        response = self.client.post(reverse('password_reset'), data={'email':'coul@gmail.com'})
        self.assertEqual(response.status_code, 200)
    
    def test_password_reset_confirm_view(self):
        uid = urlsafe_base64_encode(force_bytes(self.superuser.pk))
        token = default_token_generator.make_token(self.superuser)
        response = self.client.post(reverse('password_reset_confirm', args=[uid, token]), data={
                                            'new_password1':'tejzoiej57', 
                                            'new_password2':'tejzoiej57'})
        self.assertEqual(response.status_code, 302)
        response = self.client.post(response.url, data={
                                            'new_password1':'tejzoiej57', 
                                            'new_password2':'tejzoiej57'})

        self.assertRedirects(response, reverse('password_reset_complete'))
        login = self.client.login(user_name='coul@gmail.com', password = 'godejeroien583')
        self.assertFalse(login)
        login = self.client.login(user_name='coul@gmail.com', password = 'tejzoiej57')
        self.assertTrue(login)