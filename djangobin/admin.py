from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models
from users.models import CustomUser



# Register your models here.
#UserAdmin.list_display = ('email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff')
#UserAdmin.fields = ('first_name', 'last_name', 'email')


class AuthorInline(admin.StackedInline):
    model = models.Author

class CustomUserAdmin(UserAdmin):
    #fields = ('first_name', 'last_name', 'email')
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', )
        }),

    )
    inlines = (AuthorInline,)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'lang_code', 'slug', 'mime', 'created_on')
    search_fields = ['name', 'mime']
    ordering = ['name']
    list_filter = ['created_on']
    date_hierarchy = 'created_on'


class SnippetAdmin(admin.ModelAdmin):
    list_display = ('language', 'title', 'expiration', 'exposure', 'user')
    search_fields = ['title', 'user']
    ordering = ['-created_on']
    list_filter = ['created_on']
    date_hierarchy = 'created_on'
    #filter_horizontal = ('tags', )
    raw_id_fields = ('tags', )

    readonly_fields = ('highlighted_code', 'hits', 'slug',)
    fields = ('title', 'original_code', 'highlighted_code', 'expiration', 'exposure',
              'hits', 'slug', 'language', 'user', 'tags')


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_on',)
    search_fields = ('name',)
    ordering = ['-created_on']
    # prepopulated fields = {'slug': ('name', )}
    readonly_fields = ('slug', )


#
admin.site.unregister(CustomUser)
admin.site.register(CustomUser, CustomUserAdmin)


# admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Snippet, SnippetAdmin)
admin.site.register(models.Tag, TagAdmin)


