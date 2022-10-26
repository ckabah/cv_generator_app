from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .utilitis import *
from .forms import *
from .models import *
def home(request):
    return render(request, 'home.html', {})

@login_required()
def dashbord(request):
    profile = Profile.objects.all()[0]
    experiences = ProfExperience.objects.all()
    educations = Education.objects.all()
    langues = Langue.objects.all()
    skills = Skill.objects.all()
    technical_skills = TechnicalSkill.objects.all()
    projects = Project.objects.all()
    context  = {
        "profile":profile,
        "experiences":experiences,
        "educations":educations,
        "langues":langues,
        "skills":skills,
        "technical_skills":technical_skills,
        "projects":projects,
    }
    return render(request, 'dashbord.html', context=context)

# add views
@login_required()
def add_profile(request):
    add_form = add(request, ProfileForm)
    return render(request,"add.html", context={"form":add_form})

@login_required()
def add_education(request):
    add_form = add(request, EducationForm,)
    return render(request,"add.html", context={"form":add_form})

@login_required()
def add_skill(request):
    add_form = add(request, SkillForm,)
    return render(request,"add.html", context={"form":add_form})

@login_required()
def add_technical_skill(request):
    add_form = add(request, TechnicalSkillForm,)
    return render(request,"add.html", context={"form":add_form})

@login_required()
def add_experience(request):
    add_form = add(request, ExperienceForm,)
    return render(request,"add.html", context={"form":add_form})

@login_required()
def add_project(request):
    add_form = add(request, ProjectForm,)
    return render(request,"add.html", context={"form":add_form})

@login_required()
def add_langue(request):
    add_form = add(request, LangueForm,)
    return render(request,"add.html", context={"form":add_form})

# edit views
@login_required()
def edit_profile(request, id):
    edit_form= edit(request, id, Profile, ProfileForm,)
    return render(request,"edit.html", context={"form":edit_form})

@login_required()
def edit_education(request,id):
    edit_form= edit(request, id, Education, EducationForm,)
    return render(request,"edit.html", context={"form":edit_form})

@login_required()
def edit_skill(request, id):
    edit_form= edit(request,id, Skill, SkillForm,)
    return render(request,"edit.html", context={"form":edit_form})

@login_required()
def edit_technical_skill(request, id):
    edit_form = add(request,id, TechnicalSkill, TechnicalSkillForm,)
    return render(request,"edit.html", context={"form":edit_form})

@login_required()
def edit_experience(request, id):
    edit_form= edit(request,id, ProfExperience, ExperienceForm,)
    return render(request,"edit.html", context={"form":edit_form})

@login_required()
def edit_project(request, id):
    edit_form = add(request,id, Project,ProjectForm,)
    return render(request,"edit.html", context={"form":edit_form})

@login_required()
def edit_langue(request,id):
    edit_form= edit(request,id,Langue, LangueForm,)
    return render(request,"edit.html", context={"form":edit_form})

# delete views
@login_required()
def del_profile(request, id):
    del_form = delete(request, id, Profile, ProfileForm,)
    return render(request,"del.html", context={"form":del_form })

@login_required()
def del_education(request, id):
    del_form = delete(request, id, Education, EducationForm,)
    return render(request,"del.html", context={"form":del_form })

@login_required()
def del_skill(request, id):
    del_form  = delete(request, id, Skill, SkillForm,)
    return render(request,"del.html", context={"form":del_form})

@login_required()
def del_technical_skill(request, id):
    del_form = add(request,id, TechnicalSkill, TechnicalSkillForm,)
    return render(request,"del.html", context={"form":del_form})

@login_required()
def del_experience(request,id):
    del_form  = delete(request, id, ProfExperience, ExperienceForm,)
    return render(request,"del.html", context={"form":del_form })

@login_required()
def del_project(request):
    del_form = add(request,id, Project,ProjectForm,)
    return render(request,"del.html", context={"form":del_form})

@login_required()
def del_langue(request, id):
    del_form  = delete(request,id, Langue, LangueForm,)
    return render(request,"del.html", context={"form":del_form})