from .views import VoteCreateView
from django.urls import path

urlpatterns = [
    path('vote/', VoteCreateView.as_view(), name='vote_create'),
]
