from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status')
    list_filter = ('status', 'created', 'updated')
    search_fields = ('author__username', 'tilte')
    prepopulated_fields = {'slug':('title',)}
    list_editable = ('status',)
    date_hierarchy = ('created')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
