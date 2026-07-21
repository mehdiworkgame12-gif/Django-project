from django.contrib import admin
from blog.models import Post, Category
from django_summernote.admin import SummernoteModelAdmin
from blog.models import Post, Category, Comment


class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'counted_view', 'status', 'published_date')
    list_filter = ('status',)
    ordering = ['-created_date']
    search_fields = ['title', 'content']
    summernote_fields = ('content',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)

