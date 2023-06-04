from django.contrib.auth.views import LoginView
from django.views.generic import  RedirectView
from django.contrib.auth import  logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
import core.settings as setting

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ingrese un username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Ingrese una contraseña'})

class LoginFormView(LoginView):

    form_class = CustomAuthenticationForm
    template_name = "login.html"

    def form_valid(self, form, **kwargs):
        user = form.get_user()

        if not user.is_superuser:

            return redirect('login')

        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect(setting.LOGIN_REDIRECT_URL)

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar Sesion'

        return context

class LogoutFormView(RedirectView):

    pattern_name = "login"
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)

