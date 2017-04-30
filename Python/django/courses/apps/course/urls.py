from django.conf.urls import url
from . import views

app_name='course_app'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.new, name='new'),
    url(r'destroy/(?P<id>\d+)$', views.destroy, name = 'destroy'),
    url(r'delete/(?P<id>\d+)$', views.delete, name = 'delete')
]
