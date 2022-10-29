from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .utilitis import *
from .forms import *
from django.views.generic import View
from wkhtmltopdf.views import PDFTemplateResponse

def home(request):
    return render(request, 'home.html', {})

@login_required()
def dashbord(request):
    context  = get_all_context(request)
    return render(request, 'dashbord.html', context=context)

class HtmlToPdf(View):
    template_name = 'cv.html'
    
    def get(self, request):
        context  = get_all_context(request)
        response = PDFTemplateResponse(
            request=request,
            template=self.template_name,
            filename='cv.pdf',
            context=context,
            show_content_in_browser = True,
            cmd_options={'margin-top': 0,'disable-javascript': True, 'quiet': None, 'enable-local-file-access': True},
        )
        return response

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
    edit_form = edit(request,id, TechnicalSkill, TechnicalSkillForm,)
    return render(request,"edit.html", context={"form":edit_form})

@login_required()
def edit_experience(request, id):
    edit_form= edit(request,id, ProfExperience, ExperienceForm,)
    return render(request,"edit.html", context={"form":edit_form})

@login_required()
def edit_project(request, id):
    edit_form = edit(request,id, Project,ProjectForm,)
    return render(request,"edit.html", context={"form":edit_form})

@login_required()
def edit_langue(request,id):
    edit_form= edit(request,id,Langue, LangueForm,)
    return render(request,"edit.html", context={"form":edit_form})

# delete views
@login_required()
def del_profile(request, id):
    response=delete(request, id, Profile)
    return response

@login_required()
def del_education(request, id):
    response=delete(request, id, Education,)
    return response

@login_required()
def del_skill(request, id):
    response=delete(request, id, Skill)
    return response

@login_required()
def del_technical_skill(request, id):
    response = delete(request,id, TechnicalSkill)
    return response

@login_required()
def del_experience(request,id):
    response = delete(request, id, ProfExperience)
    return response

@login_required()
def del_project(request, id):
    response=delete(request,id, Project,)
    return response

@login_required()
def del_langue(request, id):
    response= delete(request,id, Langue)
    return response