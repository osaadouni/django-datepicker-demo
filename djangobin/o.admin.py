from django.contrib import admin
from . import models


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_on', 'private')
    search_fields = ('first_name', 'last_name', 'email',)
    ordering = ['-last_name']
    list_filter = ('created_on', 'private',)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'lang_code', 'slug', 'mime',  'created_on')
    search_fields = ['name', 'mime']
    ordering = ['name']
    list_filter = ['created_on']
    date_hierarchy = 'created_on'  # allowed fieldtypes: DateField & DateTimeField


class SnippetAdmin(admin.ModelAdmin):
    list_display = ('language', 'title', 'expiration', 'exposure', 'author')
    search_fields = ['title', 'author']
    ordering = ['-created_on']
    list_filter = ['created_on']
    date_hierarchy = 'created_on'
    #filter_horizontal = ('tags',)
    raw_id_fields = ('tags',)
    readonly_fields = ('highlighted_code', 'hits', 'slug',)
    fields = ('title', 'original_code', 'highlighted_code', 'expiration', 'exposure',
              'hits', 'slug', 'language', 'author', 'tags')


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_on')
    search_fields = ('name',)
    ordering = ['-created_on']
    # prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('slug',)

#admin.site.register(models.Author)
#admin.site.register(models.Language)
#admin.site.register(models.Snippet)
#admin.site.register(models.Tag)

#admin.site.register([models.Author, models.Language, LanguageAdmin,  models.Snippet, models.Tag])
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Language, LanguageAdmin)
admin.site.register(models.Snippet, SnippetAdmin)
admin.site.register(models.Tag, TagAdmin)


