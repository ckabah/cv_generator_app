from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import *


def add(request, form):
    add_form = form()
    if request.method == "POST":
        if "is_file" in request.POST:
            add_form = form(request.POST, request.FILES)
        else:
            add_form = form(request.POST)
        if add_form.is_valid():
            new_model = add_form.save(commit=False)
            new_model.user_id = request.user.pk
            new_model.save()
            add_form = form()
    return add_form


def delete(request, id, model):
    obj = get_object_or_404(model, id=id)
    if request.method == "POST":
        obj.delete()
        messages.error(request, "Votre Article a bien été supprimé")
        return redirect("dashbord")
    return render(request, "del.html")


def edit(request, id, model, model_form):
    obj = get_object_or_404(model, id=id)
    edit_form = model_form(instance=obj)
    if request.method == "POST":
        if "is_file" in request.POST:
            edit_form = model_form(request.POST, request.FILES, instance=obj)
        else:
            edit_form = model_form(request.POST, instance=obj)
        edit_form.save()
        messages.success(request, "Votre Article a bien été modifié")
    return edit_form


def get_all_context(request):
    profile = Profile.objects.filter(user=request.user)
    if profile.exists():
        profile = profile[0]
    experiences = ProfExperience.objects.filter(user=request.user)
    educations = Education.objects.filter(user=request.user)
    langues = Langue.objects.filter(user=request.user)
    skills = Skill.objects.filter(user=request.user)
    technical_skills = TechnicalSkill.objects.filter(user=request.user)
    projects = Project.objects.filter(user=request.user)
    context = {
        "profile": profile,
        "experiences": experiences,
        "educations": educations,
        "langues": langues,
        "skills": skills,
        "technical_skills": technical_skills,
        "projects": projects,
    }
    return context
