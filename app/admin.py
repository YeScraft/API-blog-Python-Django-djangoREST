from django.contrib import admin
from app.models import Post, Category
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'content', 'category',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
