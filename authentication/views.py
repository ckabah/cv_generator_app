import email
from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm, UserCreationForm
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .utilitis import account_token_generation
from django.contrib.sites.shortcuts import get_current_site
from .models import User
from django.contrib.auth import login, authenticate,views

def register(request):
    register_form = UserCreationForm()
    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.save()
            from_email = register_form.cleaned_data['email']
            to_email = 'csttrx@gmail.com'
            subject = 'account activation'
            message = render_to_string('account_activation_email.html',
                {
                    'user':user,
                    'domain':get_current_site(request),
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':account_token_generation.make_token(user)
                }
            )
            try:
                send_mail(subject=subject, message=message, from_email=from_email, recipient_list=[to_email])
                return HttpResponse('Please confirme your email', status=200)
            except:
                return HttpResponse('Something wrong', status=500)
    return render(request, 'register.html', context={'register_form':register_form})

def account_activation(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
    
    if user is not None and account_token_generation.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Your account is active now', status=200)
    else:
        return HttpResponse('Your link is invalid', status=404)
        
class LoginView(views.LoginView):
    form_class = LoginForm
    template_name = 'login.html'