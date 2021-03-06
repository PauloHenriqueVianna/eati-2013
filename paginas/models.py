# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _


class Pagina(models.Model):
    url = models.CharField(_('URL'), max_length=100, db_index=True)
    desc = models.CharField(u"descrição do título",max_length = 100)
    title = models.CharField(_('title'), max_length=200)
    content = models.TextField(_('content'), blank=True)
    enable_comments = models.BooleanField(_('enable comments'))
    template_name = models.CharField(_('template name'), max_length=70, blank=True,
        help_text=_("Example: 'flatpages/contact_page.html'. If this isn't provided, the system will use 'flatpages/default.html'."))
    registration_required = models.BooleanField(_('registration required'), help_text=_("If this is checked, only logged-in users will be able to view the page."))
    sites = models.ManyToManyField(Site)

    class Meta:
        db_table = 'django_pagina'
        verbose_name = _('Pagina')
        verbose_name_plural = _('Paginas')
        ordering = ('title',)

    def __unicode__(self):
        return u"Página: %s" % (self.title)

    def get_absolute_url(self):
        return self.url
