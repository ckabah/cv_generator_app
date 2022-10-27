from django import forms
from .models import*

class EducationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Non de la formation"}))
    level = forms.CharField(required=False, widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Bac, Licence ou .."}))
    etablisement = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Non de l'entreprise"}))
    start_at = forms.DateField(required=False,widget=forms.DateInput(format=('%Y-%m-%d'),attrs={"class":"form_date", "placeholder":"Date de début",'type':'date'}))
    end_at = forms.DateField(required=False, widget=forms.DateInput(format=('%Y-%m-%d'),attrs={"class":"form_date", "placeholder":"Date de fin",'type':'date'}))
    etab_website = forms.URLField(required=False, widget=forms.URLInput(attrs={"class":"form_input", "placeholder":"url du site web de l'entreprice"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"class":"form_area", "placeholder":"Une brêve description de la formation"}))
    class Meta:
        model = Education
        fields = ['name', 'level',"start_at", "end_at",'etablisement',"etab_website", 'description']
    
class SkillForm(forms.ModelForm): 
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Le nom (python)"}))
    class Meta:
        model = Skill
        fields = ["name",]

class TechnicalSkillForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Le nom (python)"}))
    level = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Niveau (entre 0 et 100)"}))
    class Meta:
        model = TechnicalSkill
        fields = ["name", "level",]

class ProjectForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Le nom (python)"}))
    detail = forms.CharField(widget=forms.Textarea(attrs={"class":"form_area", "placeholder":"Project detail"}))
    class Meta:
        model = Project
        fields = ["name","detail"]

class LangueForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Le nom de la langue (français)"}))
    level = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Niveau (entre 0 et 100)"}))
    class Meta:
        model = Langue
        fields = ["name", "level",]

class ExperienceForm(forms.ModelForm):
    type = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Stage, Emploie ou .."}))
    company = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Company name"}))
    poste = forms.CharField(required=False,widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Poste (developer)"}))
    start_at = forms.DateField(required=False,widget=forms.DateInput(format=('%Y-%m-%d'),attrs={"class":"form_date", "placeholder":"Started date",'type': 'date'}))
    end_at = forms.DateField(required=False,widget=forms.DateInput(format=('%Y-%m-%d'),attrs={"class":"form_date", "placeholder":"Date de fin",'type':'date'}))
    etab_website = forms.URLField(required=False,widget=forms.URLInput(attrs={"class":"form_input", "placeholder":"url du site web de l'entreprice"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"class":"form_area", "placeholder":"Une brêve description"}))
    class Meta:
        model = ProfExperience
        fields = fields = ['type', "start_at", "end_at","poste",'company',"etab_website",'description']

class ProfileForm(forms.ModelForm):
    photo = forms.ImageField(required=False,widget=forms.FileInput)
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Nom"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Prénom"}))
    phone = forms.CharField(required=False,widget=forms.NumberInput(attrs={"class":"form_input", "placeholder":"Numéro de mobile"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form_input", "placeholder":"Email"}))
    adress = forms.CharField(required=False,widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Adresse"}))
    bio = forms.CharField(widget=forms.Textarea(attrs={"class":"form_input", "placeholder":"qui êtes vous ?"}))
    is_file = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Profile
        fields = ["photo","first_name", "last_name","bio",'phone', "email", "adress", "is_file"]