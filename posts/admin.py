from django.contrib import admin


from .models import Post, Comment

class PostDetailAdmin(admin.ModelAdmin):
    list_display = ('title', 'date',)



# Register your models here.
admin.site.register(Post, PostDetailAdmin)
admin.site.register(Comment)