from django.urls import path

from . import views

urlpatterns = [
    path("resume/", views.resume_view, name="resume"),
    path("projects/<slug:slug>/", views.ProjectDetailView.as_view(), name="project-detail"),
    path("contact/", views.ContactView.as_view(), name="contact"),
]
