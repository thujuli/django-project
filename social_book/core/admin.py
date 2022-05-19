from django.contrib import admin
from .models import Profile, Post, LikePost
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('id_user',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post)
admin.site.register(LikePost)
