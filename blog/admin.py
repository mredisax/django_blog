from django.contrib import admin
from .models import Post, Category, Author, Comment
from ckeditor.widgets import CKEditorWidget
from django.db import models

class PostAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Title/date/img', {'fields': ['title','slug',('published','thumbnail','category','author') ]}),
        ('Content', {'fields': ['content']})
    ]

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
        }

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Category', {'fields': ['name', 'slug']})
    ]


class AuthorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Author', {'fields': ['user','avatar', 'bio']})
    ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'content')

admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)