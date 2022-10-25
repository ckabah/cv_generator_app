from django.db import models
from authentication.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True, verbose_name="photo de profile",upload_to='profile')
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=68, blank=True, null = True)
    adress = models.CharField(max_length=250, blank=True, null = True)
    email = models.EmailField()
    bio = models.TextField()

    IMAGE_MAX_SIZE = (300, 300)

    def resize_image(self):
        image = Image.open(self.photo)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.photo.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            self.resize_image()

    def __str__(self):
        return str(self.first_name)

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    level = models.CharField(max_length=120, blank=True, verbose_name="Niveau de formation")
    description = models.CharField(max_length=5000)
    etablisement = models.CharField(max_length=500)
    start_at = models.DateField(verbose_name='Start date ', null=True, blank=True)
    end_at = models.DateField(verbose_name='End date' , null=True, blank=True)
    etab_website = models.URLField(blank=True, null=True)
    
class ProfExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=120)
    description = models.CharField(max_length=2000)
    company = models.CharField(max_length=500)
    poste = models.CharField(max_length=120, blank=True, verbose_name="Niveau de formation")
    start_at = models.DateField(verbose_name='Start date ', null=True, blank=True)
    end_at = models.DateField(verbose_name='End date' , null=True, blank=True)
    etab_website = models.URLField(blank=True, null=True)

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    detail = models.TextField()

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)

class TechnicalSkill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    level = models.IntegerField()
    
class Langue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    level = models.IntegerField()