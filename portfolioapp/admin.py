from django.contrib import admin

from .models import Project, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'link']


admin.site.site_header = 'Portfolio'
admin.site.index_title = 'Admin Portal'
admin.site.register(Project)
admin.site.register(Contact, ContactAdmin)
