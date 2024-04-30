from django.contrib import admin
from .models import Opportunities,Banner,Gallery,NewsEvents,User

# Register your models here.
@admin.register(Opportunities)
class OpportunityModal(admin.ModelAdmin):
    list_display = ['id','name','institute', 'email','phone']

@admin.register(Banner)
class BannerModal(admin.ModelAdmin):
    list_display = ['id','title','image']

@admin.register(Gallery)
class GalleryModal(admin.ModelAdmin):
    list_display = ['id','image', 'is_home_page']

@admin.register(NewsEvents)
class NewsEventsModal(admin.ModelAdmin):
    list_display = ['id','title','date','mode','venue','is_home_page']

@admin.register(User)
class UserModal(admin.ModelAdmin):
    list_display = ['id','name','title']