from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.login_registration.urls')),
    url(r'^dashboard/', include('apps.handy_helper.urls')),
]
