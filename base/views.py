from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, ListView
from django_summernote.widgets import SummernoteWidget

from base.models import Course


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


@method_decorator(login_required, name="dispatch")
class CourseListView(ListView):
    model = Course
    template_name = "course_list.html"
    context_object_name = 'courses'
    paginate_by = 10



@method_decorator(login_required, name="dispatch")
class CourseCreateView(CreateView):
    description = SummernoteWidget()
    model = Course
    template_name = 'course_form.html'
    fields = [
        'title', 'subtitle', 'description', 'amount', 'image', 'is_active',
        'details'
    ]

    def get_success_url(self) -> str:
        return reverse('course_list')

    def post(self, request, *args, **kwargs):
        self.object = None
        return super().post(request, *args, **kwargs)
