from django.test import TestCase
from authentication.models import User
from django.urls import reverse
from cvgenerator.models import *

class TestCvView(TestCase):

    def setUpTestData(cls):
        user =  User.objects.create_superuser('coul@gmail.com', user_name='cscoul', password='godejeroien583')
        Profile.objects.create(user=user,first_name = 'Coulibaly', last_name='Soumaila', bio="Coulibaly Soumaila bio")
        Education.objects.create(user=user, name = 'AI and Multi-media', 
                                etablisement='University of Batna2', 
                                description='Ai and Multi-media',  )
        ProfExperience.objects.create(user=user, type='stage', description = 'Machine engeneer stage', company='google')

        Project.objects.create(user=user, name='Laon prediction using ML', 
                        detail = 'This project use Machine learning to build a model to predict laon eligibiliy')
        Skill.objects.create(user=user, name='Data analyse')
        TechnicalSkill.objects.create(user=user, name='python', level='90')
        Langue.objects.create(user=user, name='English', level='70' )

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
    
    def test_dashbord(self):
        login = self.client.login(user_name="coul@gmail.com", password = "godejeroien583")
        self.assertTrue(login)
        response = self.client.get(reverse('dashbord'))
        self.assertEqual(response.status_code, 200)