from django.contrib import admin
# from app.models import GeneralInfo, Service, Testimonial, FrequentlyAskQns
from app.models import (
    GeneralInfo,
    Service, 
    Testimonial, 
    FrequentlyAskQns,
    ContactFormLog,
    Blog,
    Author,
)

# Register your models here.
@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    
    list_display = [
        'company_name',
        'location',
        'email',
        'phone',
        'open_hours',
    ]
    
    # Show you can set specific field to disable update permission
    readonly_fields = [
        'email'
    ]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description',
    ]

    #Django's Inbuild SearchBar
    search_fields = [
        "title",
        "description",
    ]


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    list_display = [
        "username",
        "user_job_title",
        # "rating_count",
        "display_rating_count",
    ]

    def display_rating_count(self, obj):
        full_stars = int(obj.rating_count)  # Number of full stars
        half_star = obj.rating_count - full_stars >= 0.5  # Check if there's a half-star
        return '★' * full_stars + ('☆' if half_star else '')



    display_rating_count.short_description = "Rating"


@admin.register(FrequentlyAskQns)
class FrequentlyAskQnsAdmin(admin.ModelAdmin):
     
     list_display = [
        "question",
        "answer",
    ]
     

# Register your models here.
@admin.register(ContactFormLog)
class ContactFormLogAdmin(admin.ModelAdmin):
    
    list_display = [
        'email',
        'is_success',
        'is_error',
        'action_time',
    ]

    def has_add_permission(self, request, object = None):
        return False
    
    # Show to disable update permission
    def has_change_permission(self, request, object = None):
        return False
    
    #Show to disable delete permission
    def has_delete_permission(self, request, object = None):
        return False
    
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = [
        'first_name',
        'last_name',
    ]

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    list_display = [
        'category',
        'author',
        'title',
        'blog_image',
        'created_at',
    ]