from django.test import TestCase
from authentication.models import User
from django.urls import reverse
from cvgenerator.models import Education, Langue, ProfExperience, Profile

class TestCvView(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('coul@gmail.com', user_name='cscoul', password='godejeroien583')
        self.user.is_active = True
        self.user.save()
    
    def test_add_view(self):
        response = self.client.post(reverse('add_education'), data={
            'name':'cumputer system', 'description':'education description', 'level':'master'
        })
        self.assertNotEqual(response.status_code, 200) # will fail for login required

        login = self.client.login(user_name="coul@gmail.com", password = "godejeroien583")
        self.assertTrue(login)

        response = self.client.post(reverse('add_education'), data={
            'name':'cumputer system', 
            'description':'education description', 
            'level':'master',
            'etablisement':'Univ of Batna2',
        })
        self.assertEqual(response.status_code, 200) # will pass now 
        self.assertEqual(Education.objects.count(), 1)

        response = self.client.post(reverse('add_profile'), data={
            'first_name':'Coulibaly', 
            'last_name':'Soumaila',
            'email':'cs.ttrx@gmail.com', 
            'bio':'AI engenneer',
            'is_file':True,
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Profile.objects.count(), 1)
    
    def test_edit_view(self):
        login = self.client.login(user_name="coul@gmail.com", password = "godejeroien583")
        self.assertTrue(login)
        response = self.client.post(reverse('add_experience'), data={
            'type':'Stage', 
            'company':'google',
            'description':'expencience description', 
        })
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('edit_experience', args=[1]), data={
            'type':'Stage', 
            'company':'facebook',
            'description':'expencience description', 
        })
        experience = ProfExperience.objects.get(id=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(experience.company, 'facebook')
    
    def test_delete_view(self):
        login = self.client.login(user_name="coul@gmail.com", password = "godejeroien583")
        self.assertTrue(login)
        response = self.client.post(reverse('add_langue'), data={
            'name':'English', 
            'level':90
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Langue.objects.count(), 1)
        response = self.client.post(reverse('del_langue', args=[1]))
        self.assertEqual(Langue.objects.count(), 0)