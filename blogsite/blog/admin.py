from django.contrib import admin
from .models import Post, Keyword

from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'keyword', 'status', 'created_on')
    list_filter = ("status", "keyword")
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


admin.site.register(Keyword)
admin.site.register(Post, PostAdmin)
