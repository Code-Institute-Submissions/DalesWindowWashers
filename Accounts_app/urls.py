from django.conf.urls import url
import views


urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^account/$', views.account_details, name='account_details'),
]