from django.db import models


# ---------------- ContactMessage Model ----------------
class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} — {self.email} — {self.created_at:%Y-%m-%d %H:%M}"


# ---------------- Service Model ----------------

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('Database', 'Database'),
        ('Tool', 'Tool / Software'),
        ('Other', 'Other'),
    ]
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50, help_text="Example: Beginner, Intermediate, Expert")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')

    def __str__(self):
        return f"{self.name} ({self.level})"


class Education(models.Model):
    degree = models.CharField(max_length=150)
    institution = models.CharField(max_length=150)
    start_year = models.CharField(max_length=10)
    end_year = models.CharField(max_length=10, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} - {self.institution}"



# ---------------- Project Model ----------------
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_7/')
    github_url = models.URLField(blank=True, default='')
    live_url = models.URLField(blank=True, default='')
    technologies = models.CharField(max_length=200, blank=True, default='', help_text="Comma-separated technologies, e.g. React, Node.js, MongoDB")

    def __str__(self):
        return self.title

    def tech_list(self):
        if self.technologies:
            return [tech.strip() for tech in self.technologies.split(',')]
        return []


# ---------------- Blog Model ----------------
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
