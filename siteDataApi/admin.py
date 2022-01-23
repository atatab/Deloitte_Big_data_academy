from django.contrib import admin
from siteDataApi.models import Service, TeamMember, BlogPost

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = [ 'name' ]

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'service_area' )
    search_fields = ['first_name', 'last_name', 'service_area__name']

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pub_date', 'author' )
    search_fields = [ 'headline', 'pub_date', 'content', 'author__first_name', 'author__last_name' ]

admin.site.register(Service, ServiceAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(BlogPost, BlogPostAdmin)