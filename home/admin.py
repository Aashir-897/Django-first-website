from django.contrib import admin
from home.models import Blog, Contact, Project  # Import Project model

# Register your models here.
from home.models import Blog,Contact

class BlogAdmin(admin.ModelAdmin):

    list_display = ('title', 'date_created', 'last_modified', 'is_draft')
admin.site.register(Blog,BlogAdmin)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('name', 'date_created', 'last_modified', 'is_draft')

admin.site.register(Contact,ContactAdmin)

# Admin class for Project
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technologies', 'date_created', 'image') 
    search_fields = ('title', 'description')  
    list_filter = ('technologies',) 

admin.site.register(Project, ProjectAdmin) 

