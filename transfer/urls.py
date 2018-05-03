from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'lk/', views.lk, name='lk'),
    url(r'^register/$', views.RegisterFormView.as_view()),
]