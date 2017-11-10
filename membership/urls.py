from django.conf.urls import url
from membership import views

urlpatterns = [
    url(r'login/$', views.user_login, name='login')
]
