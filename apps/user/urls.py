from django.urls import path

from apps.user import views

urlpatterns = [
    path("consultants/", views.ConsultantsListView.as_view())
]
