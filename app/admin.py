from django.contrib import admin
from .models import posts,contact

@admin.register(posts)
class postsA(admin.ModelAdmin):
    list_display = ('title','slug','date')
    list_filter = ('date',)
    #fields = ('title','content',('date','slug','img_file',),'sub_heading')
    fieldsets = (
        ('Details',{'fields':('title','sub_heading','content')}),
        ('Extras',{'fields':('date','slug','img_file','image_upl')})
    )
@admin.register(contact)
class contactA(admin.ModelAdmin):
    pass

