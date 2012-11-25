# -*- coding: utf-8 -*-
from django.conf import settings
from django.template import Context
from django.core.urlresolvers import reverse, set_script_prefix
from django.contrib.sites.models import Site


class NoticeContext(Context):
    def __init__(self, dict_=None, **kwargs):
        super(NoticeContext, self).__init__(dict_, **kwargs)

        protocol = getattr(settings, 'DEFAULT_HTTP_PROTOCOL', 'http')
        current_site = Site.objects.get_current()
        site_url = u"%s://%s" % (protocol, unicode(current_site.domain))

        if not settings.MEDIA_URL.startswith('http'):
            settings.MEDIA_URL = u'%s%s' % (site_url, settings.MEDIA_URL)

        set_script_prefix(site_url)

        self.update({
            'current_site': current_site,  # backward-compatibility
            'site': current_site,
            'site_url': site_url,
            'STATIC_URL': settings.STATIC_URL,
        })