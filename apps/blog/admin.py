from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'published', 'reading_time']
    list_filter = ['published', 'created_at']
    search_fields = ['title', 'content', 'tags']
    prepopulated_fields = {'slug': ('title',)}
    
    fields = [
        'title', 
        'slug', 
        'excerpt', 
        'content', 
        'tags',
        'meta_description',
        'published'
    ]
    
    def reading_time(self, obj):
        return f"{obj.reading_time()} min"
    reading_time.short_description = 'Tempo de leitura'
