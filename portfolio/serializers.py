from rest_framework import serializers

from .models import Profile, Skill, Project, Experience, Testimonial, ContactMessage


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "full_name", "title", "bio", "email", "location",
            "avatar", "github_url", "linkedin_url",
        ]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["name", "category", "proficiency"]


class ProjectSerializer(serializers.ModelSerializer):
    tech_stack = serializers.ListField(source="tech_list", read_only=True)

    class Meta:
        model = Project
        fields = [
            "title", "slug", "summary", "description", "tech_stack",
            "repo_url", "live_url", "cover_image", "featured",
        ]


class ExperienceSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source="title", read_only=True)

    class Meta:
        model = Experience
        fields = ["company", "role", "location", "description", "start_date", "end_date"]


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ["quote", "author_name", "author_role"]


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
