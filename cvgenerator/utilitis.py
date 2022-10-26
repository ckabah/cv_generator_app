from django.shortcuts import get_object_or_404
from django.contrib import messages

def add(request,form):
    add_form = form()
    if request.method == "POST":
        if 'is_file' in request.POST:
            add_form = form(request.POST, request.FILES)
        else:
            add_form = form(request.POST)
        if add_form.is_valid():
            new_model = add_form.save(commit=False)
            new_model.user_id = request.user.pk
            new_model.save()
            add_form = form()
    return add_form

def delete(request, id, model, model_form):
    obj = get_object_or_404(model, id = id)
    del_form = model_form(instance = obj)
    if request.method == "POST":
        del_form = model_form(request.POST, instance = obj)
        obj.delete()
        messages.error(request, "Votre Article a bien été supprimé")
    return del_form

def edit(request, id, model,model_form):
    obj = get_object_or_404(model, id=id)
    edit_form = model_form(instance = obj)
    if request.method == "POST":
        if 'is_file' in request.POST:
            edit_form = model_form(request.POST, request.FILES, instance = obj)
        else:
            edit_form = model_form(request.POST, instance = obj)
        edit_form.save()
        messages.success(request, 'Votre Article a bien été modifié')
    return edit_form