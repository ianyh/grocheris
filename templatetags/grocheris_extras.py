from django import template
from django.conf import settings

register = template.Library()

def media(path=''):
    import urlparse
    url = settings.MEDIA_URL or ''
    if path:
        return urlparse.urljoin(url, path)
    elif not url.endswith('/'):
        return '%s/' % url
    return url

media = register.simple_tag(media)
