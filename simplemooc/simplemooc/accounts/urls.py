from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from simplemooc.accounts import views

app_name="accounts"

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^entrar/$', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^sair/$', LogoutView.as_view(), name='logout'),
    url(r'^cadastre-se/$', views.register, name='register'),
    url(r'^editar/$', views.edit, name='edit'),
    url(r'^editar-senha/$', views.edit_password, name='edit_password'),
    url(r'^nova-senha/$', views.password_reset, name='password_reset'),
    url(r'^confirmar-nova-senha/(?P<key>\w+)/$', views.password_reset_confirm, name='password_reset_confirm'),
]