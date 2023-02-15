from django.urls import path
from django.conf.urls import url
from .views import RegisterView, LoginApiView, LogoutView

urlpatterns = [
    url(r'^register/', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginApiView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),

]