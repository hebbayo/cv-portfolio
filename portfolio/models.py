from django.db import models

# Create your models here.
class Profile(models.Model):
    """Singleton-ish: one row holds your identity/bio."""
    
    full_name=models.CharField(max_length=120)
    title=models.CharField(max_length=150)
    bio=models.TextField()
    email=models.EmailField()
    location=models.CharField(max_length=150, blank=True)
    avatar=models.ImageField(upload_to="avatar/",blank=True,null=True)
    github_url=models.URLField(blank=True)
    linkedin_url=models.URLField(blank=True)
    
    def __str__(self):
        return self.full_name
    
class Skill(models.Model):
    CATEGORY_CHOICES=[
        ("backend","Backend"),
        ("frontend","Frontend"),
        ("devops","DevOps"),
        ("other","Other"),
    ]
    name = models.CharField(max_length=60)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="other")
    proficiency = models.PositiveSmallIntegerField(default=3)  # 1-5 scale
    order = models.PositiveSmallIntegerField(default=0)  # For ordering skills in the UI
    
    class Meta:
        ordering = ['order', 'name']
        
    def __str__(self):
        return self.name
    
    
class Project(models.Model):
    title=models.CharField(max_length=150)
    slug=models.SlugField(unique=True)
    summary=models.CharField(max_length=250)
    description=models.TextField()
    tech_stack = models.CharField(max_length=200, help_text="Comma separated, e.g. Django,PostgreSQL,JS")
    repo_url=models.URLField(blank=True)
    live_url=models.URLField(blank=True)
    cover_image = models.ImageField(upload_to="projects/", blank=True, null=True)
    featured=models.BooleanField(default=False)
    order=models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', '-created_at']
        
    def tech_list(self):
        """Return a list of technologies from the tech_stack string."""
        return [t.strip() for t in self.tech_stack.split(",") if t.strip()]
    def __str__(self):
        return self.title


class Experience(models.Model):
    title=models.CharField(max_length=150)
    company=models.CharField(max_length=150)
    location=models.CharField(max_length=150, blank=True)
    start_date=models.DateField()
    end_date=models.DateField(blank=True, null=True)
    description=models.TextField()
    order=models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-start_date']

    def __str__(self):
        return f"{self.title} @ {self.company}"


class Testimonial(models.Model):
    quote = models.TextField()
    author_name = models.CharField(max_length=120)
    author_role = models.CharField(max_length=150, blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.author_name}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} <{self.email}>"