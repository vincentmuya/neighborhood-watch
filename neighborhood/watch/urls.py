from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name ='index'),
    url(r'^edit/profile/(\d+)$', views.update_profile, name='update-profile'),
    url(r'^profile/(\d+)$', views.profile, name ='profile'),
    ]
