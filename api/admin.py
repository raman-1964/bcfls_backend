from django.contrib import admin
from .models import Opportunities,Banner,Gallery,NewsEvents,User,NewsLetter


# Register your models here.
@admin.register(Opportunities)
class OpportunityModal(admin.ModelAdmin):
    list_display = ['id','name','institute', 'email','phone','created_at', 'updated_at']

@admin.register(Banner)
class BannerModal(admin.ModelAdmin):
    list_display = ['id','title','image','created_at', 'updated_at']

@admin.register(Gallery)
class GalleryModal(admin.ModelAdmin):
    list_display = ['id','image', 'is_home_page','created_at', 'updated_at']

@admin.register(NewsEvents)
class NewsEventsModal(admin.ModelAdmin):
    list_display = ['id','title','date','mode','venue','is_home_page','created_at', 'updated_at']

@admin.register(User)
class UserModal(admin.ModelAdmin):
    list_display = ['id','name','title','created_at', 'updated_at']

@admin.register(NewsLetter)
class NewsLetterModal(admin.ModelAdmin):
    list_display = ['email','created_at', 'updated_at']