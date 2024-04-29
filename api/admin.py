from django.contrib import admin
from .models import Opportunities,Banner,Gallery,NewsEvents,User

# Register your models here.
@admin.register(Opportunities)
class OpportunityModal(admin.ModelAdmin):
    pass

@admin.register(Banner)
class BannerModal(admin.ModelAdmin):
    pass

@admin.register(Gallery)
class GalleryModal(admin.ModelAdmin):
    pass

@admin.register(NewsEvents)
class NewsEventsModal(admin.ModelAdmin):
    pass

@admin.register(User)
class UserModal(admin.ModelAdmin):
    pass