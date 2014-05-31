from django.contrib import admin
from django.db import models
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.models import Attachment
from django_summernote.settings import summernote_config

__widget__ = SummernoteWidget if summernote_config['iframe'] \
    else SummernoteInplaceWidget

__all__ = ['SummernoteInlineModelAdmin',
           'SummernoteModelAdmin',
           'AttachmentAdmin',
           ]


class SummernoteInlineModelAdmin(admin.options.InlineModelAdmin):
    """SummernoteInlineModelAdmin"""
    formfield_overrides = {models.TextField: {'widget': __widget__}}


class SummernoteModelAdmin(admin.ModelAdmin):
    """SummernoteModelAdmin"""
    formfield_overrides = {models.TextField: {'widget': __widget__}}


class AttachmentAdmin(admin.ModelAdmin):
    """AttachmentAdmin"""
    list_display = ['name', 'file', 'uploaded']
    search_fields = ['name']
    ordering = ('-id',)

admin.site.register(Attachment, AttachmentAdmin)
