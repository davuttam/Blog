from django.contrib import admin
from .models import Blog

# it decorate the admin page
class BlogModelAdmin(admin.ModelAdmin):
	list_display = ['title', 'updated', 'timestamp']
	list_display_links = ['updated']
	list_filter = ['updated', 'timestamp']
	search_fields = ['title', 'content']
	class Meta:
		model = Blog

admin.site.register(Blog, BlogModelAdmin)
