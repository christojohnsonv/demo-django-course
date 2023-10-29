from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views.generic.base import TemplateView


class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse('dashboard')


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'profile.html'

    def get_success_url(self) -> str:
        return reverse('dashboard')


@method_decorator(login_required, name="dispatch")
class DashboardView(TemplateView):
    template_name = "index.html"
