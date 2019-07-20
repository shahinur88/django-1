from django.conf.urls import url
from basicapp import views

app_name='basicapp'

urlpatterns=[
    url(r'^register/$',views.registration,name='registration'),
    url(r'^user_login/$',views.user_login,name='user_login')
]