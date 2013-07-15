from django.contrib import admin
from models import Pagina
from django.utils.translation import ugettext_lazy as _
from forms import PaginaForm
from tinymce.widgets import AdminTinyMCE
from django.db import models

class PaginaAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminTinyMCE},
    }
    form = PaginaForm
    fieldsets = (
        (None, {'fields': ('url', 'title','desc', 'content', 'sites')}),
        (_('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments', 'registration_required', 'template_name')}),
    )
    list_display = ('title', 'url')
    list_filter = ('sites', 'enable_comments', 'registration_required')
    search_fields = ('url', 'title')

admin.site.register(Pagina, PaginaAdmin)
