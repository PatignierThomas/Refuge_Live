from django.urls import path, re_path
from contact.views import nav

app_name = "contact"

urlpatterns = [
    re_path(r'^$', nav, name="nav-test"),
]