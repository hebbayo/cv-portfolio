from django.contrib import admin

from .models import Profile, Skill, Project, Experience, Testimonial, ContactMessage

admin.site.site_header = "Portfolio"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Content"


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "title", "email", "location")

    # One profile row feeds the whole site, so hide "Add" once it exists.
    def has_add_permission(self, request):
        return not Profile.objects.exists()


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "proficiency", "order")
    list_editable = ("category", "proficiency", "order")
    list_filter = ("category",)
    search_fields = ("name",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "featured", "order", "tech_stack", "created_at")
    list_editable = ("featured", "order")
    list_filter = ("featured",)
    search_fields = ("title", "summary", "tech_stack")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "start_date", "end_date", "order")
    list_editable = ("order",)
    search_fields = ("title", "company")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("author_name", "author_role", "order")
    list_editable = ("order",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at", "read")
    list_editable = ("read",)
    list_filter = ("read",)
    search_fields = ("name", "email", "message")
    readonly_fields = ("name", "email", "message", "created_at")

    def has_add_permission(self, request):
        return False
