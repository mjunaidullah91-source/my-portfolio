from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError

from .models import Skill, Education, Project, Blog
from .forms import ContactForm
from django.db.models import Case, When, Value, IntegerField


# ✅ Home Page
def home(request):
    skills = Skill.objects.annotate(
        custom_order=Case(
            When(category='Frontend', then=Value(1)),
            When(category='Backend', then=Value(2)),
            When(category='Database', then=Value(3)),
            default=Value(4),
            output_field=IntegerField(),
        )
    ).order_by('custom_order', 'id')
    education = Education.objects.all().order_by('-start_year')
    blogs = Blog.objects.all().order_by('-created_at')
    projects = Project.objects.all()
    return render(request, 'home.html', {
        'skills': skills,
        'education': education,
        'blogs': blogs,
        'projects': projects,
    })


# ✅ About Page
def about(request):
    return render(request, 'about.html')


# ✅ Navbar (optional direct view)
def navbar(request):
    return render(request, 'navbar.html')


# ✅ Projects Page
def projects(request):
    projects = Project.objects.all()
    return render(request, 'project.html', {'projects': projects})


# ✅ Blog Page
def blog_view(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog.html', {'blogs': blogs})

# ✅ Blog Detail Page
def blog_detail_view(request, blog_id):
    from django.shortcuts import get_object_or_404
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})


# ✅ Skills & Education Page (optional separate view)
def skills_education_view(request):
    skills = Skill.objects.annotate(
        custom_order=Case(
            When(category='Frontend', then=Value(1)),
            When(category='Backend', then=Value(2)),
            When(category='Database', then=Value(3)),
            default=Value(4),
            output_field=IntegerField(),
        )
    ).order_by('custom_order', 'id')
    education = Education.objects.all().order_by('-start_year')
    return render(request, 'skills_education.html', {
        'skills': skills,
        'education': education,
    })


import threading

def send_email_in_background(subject, body, from_email, recipient_list):
    try:
        send_mail(subject, body, from_email, recipient_list, fail_silently=False)
    except Exception as e:
        print(f"Email failed to send. Please check your App Password in settings.py. Error: {e}")

# ✅ Contact Page
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            message_obj = form.save()
            
            subject = f"New Contact: {message_obj.subject or 'No subject'}"
            body = (
                f"Name: {message_obj.name}\n"
                f"Email: {message_obj.email}\n"
                f"Phone: {message_obj.phone}\n\n"
                f"Message:\n{message_obj.message}\n"
            )
            recipient = getattr(settings, 'CONTACT_RECEIVER_EMAIL', settings.DEFAULT_FROM_EMAIL)

            # Send email in background so it doesn't freeze the website
            email_thread = threading.Thread(
                target=send_email_in_background, 
                args=(subject, body, settings.DEFAULT_FROM_EMAIL, [recipient])
            )
            email_thread.start()
            
            # Show success message (handled by SweetAlert in base.html)
            messages.success(request, "Thank you for your interest! Your message has been received, and I'll get back to you shortly.")

            return redirect('/#contactSection')
        else:
            messages.error(request, "Form me kuch masla hai — barah-e-karam sari fields check karein.")
            return redirect('/#contactSection')
    else:
        return redirect('/#contactSection')
