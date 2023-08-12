from django.urls import path

from apps.user import views

urlpatterns = [
    path("consultants/", views.ConsultantsList.as_view()),
    path("consultations/", views.ConsultationsList.as_view()),
    path("consultations/create/", views.ConsultantsCreate.as_view()),
    path("consultations/<str:pk>/", views.ConsultationsDetail.as_view()),
]
