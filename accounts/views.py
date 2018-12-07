from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.urls import reverse_lazy

from .tokens import account_activation_token
from .forms import SignupForm
from .models import CustomUser

User = get_user_model()


class SignUp(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('accounts:account_activation_sent')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        subject = 'Account activation at e-schools.com'
        message = render_to_string('accounts/account_activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
            'token': account_activation_token.make_token(user),
        })
        user.email_user(subject, message)
        return super(SignUp, self).form_valid(form)


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





















