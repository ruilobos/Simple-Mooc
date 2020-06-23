from django.conf.urls import url
from simplemooc.core import views

app_name="core"

urlpatterns = [
    url(r'^about/$',views.about, name='about'),
    url(r'^$',views.home, name='home'),
    url(r'^contato/$',views.contact, name='contact'),
]