from django.urls import path
from . import views

urlpatterns = [
   path('poll/', views.PollList.as_view()),
    path('poll/<int:pk>/', views.PollDetail.as_view()),
    path('poll/vote/<int:oid',views.PollVote.as_view()),
    path('poll/create/', views.PollCreate.as_view()),
    path('poll/<int:pk>/update/', views.PollUpdate.as_view()),
    path('option/<int:pk>/', views.PollVote.as_view()),
]