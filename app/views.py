from django.shortcuts import render, redirect
from app.models import GeneralInfo, Service, Testimonial, FrequentlyAskQns, ContactFormLog, Blog
from django.core.mail import send_mail
from django.conf import settings

from django.template.loader import render_to_string
from django.contrib import messages

from django.utils import timezone

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

def index(request):

    # General information
    general_info = GeneralInfo.objects.first()

    # Services
    services = Service.objects.all()

    # Testimonials with star ratings preprocessed
    testimonials = Testimonial.objects.all()

    processed_testimonials = []
    for testimonial in testimonials:

        rating_count = testimonial.rating_count
        full_stars = int(rating_count)  # Number of full stars
        half_star = (rating_count - full_stars) >= 0.5  # True if there's a half star
        empty_stars = 5 - full_stars - (1 if half_star else 0)  # Remaining empty stars

        processed_testimonials.append({
            "username": testimonial.username,
            "user_image": testimonial.user_image,
            "user_job_title": testimonial.user_job_title,
            "review": testimonial.review,
            "full_stars": range(full_stars),  # Precalculate ranges
            "half_star": half_star,          # Boolean
            "empty_stars": range(empty_stars),  # Precalculate ranges
        })

    # Frequently Asked Questions
    frequentlyAskQns = FrequentlyAskQns.objects.all()

    # Recent Blogs
    recent_blogs = Blog.objects.all().order_by("-created_at")[:3]
    # for blog in recent_blogs:
    #     print(f"blog : {blog}")
    #     print(f"blog.created_at : {blog.created_at}")
    #     print(f"blog.author : {blog.author}")
    #     print("")
    

    default_value = ""
    # Context
    context = {
        # "company_name": general_info.company_name,
        "company_name": getattr(general_info, "company_name", default_value),
        #This is the syntax..

        "location": getattr(general_info, "location", default_value),
        "email": getattr(general_info, "email", default_value),
        "phone": getattr(general_info, "phone", default_value),
        "open_hours": getattr(general_info, "open_hours", default_value),
        "video_url": getattr(general_info, "video_url", default_value),
        "X_url": getattr(general_info, "twitterX", default_value),
        "insta_url": getattr(general_info, "instagram_url", default_value),
        "linkedin_url": getattr(general_info, "linkedin_url", default_value),

        "services": services,
        "testimonials": processed_testimonials,
        "frequentlyAskQns": frequentlyAskQns,
        "recent_blogs" : recent_blogs,
    }

    return render(request, "index.html", context)


def contact_form(request):
    
    # print(f"request.POST : {request.POST}")

    if request.method == 'POST':

        # name = request.POST['name']   # Raises KeyError if 'name' is missing

        name = request.POST.get('name')  # Returns None if 'name' is missing

        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # print(f"name : {name}")
        # print(f"request.POST : {request.POST}")

        context = {
            "name" : name,
            "email" : email,
            "subject" : subject,
            "message" : message
        }

        html_content = render_to_string('email.html', context)
        
        is_success = False
        is_error = False
        error_message = ""

        try:
            send_mail (
            subject = subject, #appears as email title
            # message = f"{name} - {email} - {message}",
            message = None,
            html_message = html_content,
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [settings.EMAIL_HOST_USER],
            fail_silently = False
        )
        except Exception as e:

            is_error = True
            error_message = str(e)

            # print(f"email is failed")
            messages.error(request, "There's an error occured, retry to send the email..!!")

        else:
            is_success = True
            
            # print(f"Email has been send out")
            messages.success(request, "Email has been sent successfully")

        ContactFormLog.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message,
            action_time = timezone.now(),
            is_error = is_error,
            is_success = is_success,
            error_message = error_message,
        )

    return redirect('home')


def blog_detail(request, blog_id):
    blog = Blog.objects.get(id = blog_id)

    # recent_blogs = Blog.objects.all().order_by("-created_at")[:2]
    recent_blogs = Blog.objects.all().exclude(id = blog_id).order_by("-created_at")[:2]

    context = {
        "blog" : blog,
        "recent_blogs" : recent_blogs,
    }
    return render(request, "blog_details.html", context)


def blogs(request):

    all_blogs = Blog.objects.all().order_by("-created_at")
    paginator = Paginator(all_blogs, 3)

    # print(f"paginator.num_pages : {paginator.num_pages}")

    # blogs = paginator.page(1)
    # blogs = paginator.page(2)

    page = request.GET.get('page')

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    context = {
        "blogs" : blogs,
    }

    return render(request, "blogs.html", context)
