from django import forms
from .models import*

class EducationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Education Name"}))
    level = forms.CharField(required=False, widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Bac, Master, or .."}))
    etablisement = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Etablisement name"}))
    start_at = forms.DateField(required=False,widget=forms.DateInput(format=('%Y-%m-%d'),attrs={"class":"form_date", "placeholder":"Start date", 'type':'date'}))
    end_at = forms.DateField(required=False, widget=forms.DateInput(format=('%Y-%m-%d'),attrs={"class":"form_date", "placeholder":"End date", 'type':'date'}))
    etab_website = forms.URLField(required=False, widget=forms.URLInput(attrs={"class":"form_input", "placeholder":"website url off etablisement"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"class":"form_area", "placeholder":"Education description", 'rows':'5'}))
    class Meta:
        model = Education
        fields = ['name', 'level',"start_at", "end_at",'etablisement',"etab_website", 'description']
    
class SkillForm(forms.ModelForm): 
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Skill name (web developement)"}))
    class Meta:
        model = Skill
        fields = ["name",]

class TechnicalSkillForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Name (Python)"}))
    level = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Level (between 0 and 100)"}))
    class Meta:
        model = TechnicalSkill
        fields = ["name", "level",]

class ProjectForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Project name"}))
    detail = forms.CharField(widget=forms.Textarea(attrs={"class":"form_area", "placeholder":"Project detail",'rows':'5'}))
    class Meta:
        model = Project
        fields = ["name","detail"]

class LangueForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Langage name (English)"}))
    level = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Level (between 0 and 100)"}))
    class Meta:
        model = Langue
        fields = ["name", "level",]

class ExperienceForm(forms.ModelForm):
    #type = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Stage, Job ou .."}))
    company = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Company name"}))
    poste = forms.CharField(required=False,widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Job (developer)"}))
    start_at = forms.DateField(required=False,widget=forms.DateInput(format=('%Y-%m-%d'),attrs={"class":"form_date", "placeholder":"Start date", 'type':'date'}))
    end_at = forms.DateField(required=False,widget=forms.DateInput(format=('%Y-%m-%d'),attrs={"class":"form_date", "placeholder":"End date", 'type':'date'}))
    etab_website = forms.URLField(required=False,widget=forms.URLInput(attrs={"class":"form_input", "placeholder":"Website url of Company"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"class":"form_area", "placeholder":"Description",'rows':'5'}))
    class Meta:
        model = ProfExperience
        fields = fields = ["start_at", "end_at","poste",'company',"etab_website",'description']

class ProfileForm(forms.ModelForm):
    photo = forms.ImageField(required=False,widget=forms.FileInput)
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"First name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Last name"}))
    phone = forms.CharField(required=False,widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Phone number"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form_input", "placeholder":"Email"}))
    adress = forms.CharField(required=False,widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Adress"}))
    github = forms.URLField(required=False,widget=forms.URLInput(attrs={"class":"form_input", "placeholder":"Github url"}))
    website = forms.URLField(required=False,widget=forms.URLInput(attrs={"class":"form_input", "placeholder":"Your website url"}))
    bio = forms.CharField(widget=forms.Textarea(attrs={"class":"form_area", "placeholder":"Who are you",'rows':'5'}))
    is_file = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Profile
        fields = ["photo","first_name", "last_name","bio",'phone', "email", "adress","github", "website", "is_file"]