import requests
import magic

def get_content_type_ext (content_type, req=None):
    content_type = content_type.lower()
    if content_type.startswith('image/jpeg') or content_type.startswith('image/jpg'):
        return '.jpg'
    elif content_type.startswith('image/png'):
        return '.png'
    elif content_type.startswith('image/gif'):
        return '.gif'
    elif content_type.startswith('image/webp'):
        return '.webp'
    elif content_type.startswith('image/svg'):
        return '.svg'
    elif content_type.startswith('image/bmp'):
        return '.bmp'
    elif req:
        return get_content_type_ext(magic.from_buffer(req.content, mime=True))
    elif content_type.startswith('text/html'):
        return '.html'
    elif content_type.startswith('application/pdf'):
        return '.pdf'
    else:
        return ''
