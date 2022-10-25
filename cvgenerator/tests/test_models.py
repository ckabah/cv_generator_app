from django.test import TestCase
from authentication.models import User
from ..models import *

class TestModel(TestCase):
    @classmethod
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
        
    def test_profile(self):
        self.assertEqual(Profile.objects.count(), 1)
        profile = Profile.objects.get(id=1)
        max_length = profile._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 120 )
        self.assertEqual(profile.first_name, 'Coulibaly')
        self.assertEqual(profile.last_name, 'Soumaila')

    def test_education(self):
        self.assertEqual(Education.objects.count(), 1)
    
    def test_experience(self):
        self.assertEqual(ProfExperience.objects.count(), 1)

    def test__project(self):
        self.assertEqual(Project.objects.count(), 1)
    
    def test_skill(self):
        self.assertEqual(Skill.objects.count(), 1)
    
    def test_technical_skill(self):
        self.assertEqual(TechnicalSkill.objects.count(), 1)

    def test_lange(self):
        self.assertEqual(Langue.objects.count(), 1)