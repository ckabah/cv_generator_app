from django.urls import path, re_path
from django.views.static import serve
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('dashbord', dashbord, name='dashbord'),

    path('add/profile/', add_profile, name = 'add_profile'),
    path('add/formation/', add_education, name = 'add_education'),
    path('add/skill/', add_skill, name = 'add_skill'),
    path('add/technical-skill/', add_technical_skill, name = 'add_technical_skill'),
    path('add/experience/', add_experience, name = 'add_experience'),
    path('add/langue/', add_langue, name = 'add_langue'),
    path('add/project/', add_project, name='add_project'),

    path('edit/profile/<int:id>', edit_profile, name = 'edit_profile'),
    path('edit/formation/<int:id>', edit_education, name = 'edit_education'),
    path('edit/skill/<int:id>', edit_skill, name = 'edit_skill'),
    path('edit/technical-skill/<int:id>', edit_technical_skill, name = 'edit_technical_skill'),
    path('edit/experience/<int:id>', edit_experience, name = 'edit_experience'),
    path('edit/langue/<int:id>', edit_langue, name = 'edit_langue'),
    path('edit/project/<int:id>', edit_project, name='edit_project'),


    path('delete/profile/<int:id>', del_profile, name = 'del_profile'),
    path('delete/formation/<int:id>', del_education, name = 'del_education'),
    path('delete/skill/<int:id>', del_skill, name = 'del_skill'),
    path('delete/technical-skill/<int:id>', del_technical_skill, name = 'del_technical_skill'),
    path('delete/experience/<int:id>', del_experience, name = 'del_experience'),
    path('delete/langue/<int:id>', del_langue, name = 'del_langue'),
    path('delete/project/<int:id>', del_project, name='del_project'),
    path('download-pdf/', HtmlToPdf.as_view(), name='download')
]