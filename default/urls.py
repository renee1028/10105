from django.urls import path
#from . import views
from .views import *


urlpatterns = [
   path('poll/',PollList.as_view(),name='poll_list'),
    path('poll/<int:pk>/', PollDetail.as_view(), name ='poll_views'),
    path('poll/vote/<int:oid>',PollVote.as_view(), name='poll_vote'),
    path('poll/create/', PollCreate.as_view(),name='poll_create'),
    path('poll/<int:pk>/update/', PollUpdate.as_view(),name='poll_edit'),
    path('option/<int:pk>/', PollVote.as_view()),
    path('option/create/<int:pid>/', OptionCreate.as_view(), name= 'option_create'),
    path('option/<int:pk>/',OptionEdit.as_view(), name='option_edit'), 
    path('option/<int:pk>/delete/', OptionDelete.as_view(), name='option_delete' ),   
    path('poll/<int:pk>/delete/', PollDelete.as_view(), name='poll_delete'),
]