from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Profile, Skill, Project, Experience, Testimonial
from .serializers import (
    ProfileSerializer, SkillSerializer, ProjectSerializer,
    ExperienceSerializer, TestimonialSerializer, ContactMessageSerializer,
)


@api_view(["GET"])
def resume_view(request):
    """Single endpoint returning everything the frontend needs in one round trip."""
    ctx = {"request": request}
    profile = Profile.objects.first()
    return Response({
        "profile": ProfileSerializer(profile, context=ctx).data if profile else None,
        "skills": SkillSerializer(Skill.objects.all(), many=True, context=ctx).data,
        "projects": ProjectSerializer(Project.objects.all(), many=True, context=ctx).data,
        "experience": ExperienceSerializer(Experience.objects.all(), many=True, context=ctx).data,
        "testimonials": TestimonialSerializer(Testimonial.objects.all(), many=True, context=ctx).data,
    })


class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = "slug"


class ContactView(generics.CreateAPIView):
    serializer_class = ContactMessageSerializer
