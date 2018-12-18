import json
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .tokens import account_activation_token
from .forms import SignupForm
from .models import CustomUser


User = get_user_model()


def signup(request):
    response_data = {}
    print(request.POST.get('is_portal_checker', None), request.POST.get('portal_code', ''))
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            if request.POST.get('is_portal_checker', None) == 1:
                user.portal_code = request.POST.get('portal_code', '')
            user.save()
            response_data['signup'] = True
            response_data['message'] = 'Користувач успішно зареєстрований.'
        else:
            email = request.POST.get('email', '')
            is_old_user = CustomUser.objects.filter(email=email).exists()
            if is_old_user:
                response_data['signup'] = False
                response_data['message'] = 'Користувач з такою поштою вже зареєстрований!'
            else:
                response_data['signup'] = False
                response_data['message'] = 'Дані форми введено неправильно!'
        return HttpResponse(json.dumps(response_data), content_type="application/json")



# class SignUp(CreateView):
#     form_class = SignupForm
#     # success_url = reverse_lazy('accounts:account_activation_sent')
#     # template_name = 'accounts/signup.html'
#
#     def form_valid(self, form):
#         user = form.save(commit=False)
#         print(user, '-----------------')
#         user.is_active = True
#         user.save()
#         # current_site = get_current_site(self.request)
#         # subject = 'Account activation at e-schools.com'
#         # message = render_to_string('accounts/account_activation_email.html', {
#         #     'user': user,
#         #     'domain': current_site.domain,
#         #     'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
#         #     'token': account_activation_token.make_token(user),
#         # })
#         # user.email_user(subject, message)
#         return super(SignUp, self).form_valid(form)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_valid = True
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('shop:home')
    else:
        return render(request, 'accounts/account_activation_invalid.html')


def account_activation_sent(request):
    return render(request, 'accounts/account_activation_sent.html')


# @csrf_exempt
def user_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        response_data = {}
        if login_form.is_valid():
            email = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    response_data['auth'] = True
                    response_data['message'] = 'Авторизовано!!'

                else:
                    response_data['auth'] = False
                    response_data['message'] = 'Ваш аккаунт не активований'
            else:
                response_data['auth'] = False
                response_data['message'] = 'Пошта або пароль введені некоректно'
        else:
            response_data['auth'] = False
            response_data['message'] = 'Неправильна форма'

        return HttpResponse(json.dumps(response_data), content_type="application/json")
















