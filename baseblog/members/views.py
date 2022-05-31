import django.views
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView
from .forms import SignUpForm, EditProfileForm, Password_Change_Form
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
# noinspection PyUnresolvedReferences
from baseapp.models import Profile
from .forms import ProfilePageForm


# Create your views here.
class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'
    # fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePageView(UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'

    # fields = '__all__'
    fields = ['bio', 'profile_pic', 'website_url', 'twitter_url', 'linkedin_url']

    success_url = reverse_lazy('home')


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        cur_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["cur_user"] = cur_user

        return context


class Password_ChangeView(PasswordChangeView):
    # form_class = PasswordChangeForm
    form_class = Password_Change_Form
    success_url = reverse_lazy('pass-success')



def PassSuccess(request):
    return render(request, 'registration/password_success.html', {})


class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/user_edit.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user
