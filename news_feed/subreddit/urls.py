from django.conf.urls import url

from .views import CreateSubredditView, ListSubredditView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'create/?$', csrf_exempt(CreateSubredditView.as_view()), name='create'),
    url(r'list/?$', csrf_exempt(ListSubredditView.as_view()), name='list'),
]
