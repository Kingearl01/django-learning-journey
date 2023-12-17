import os
from urllib.parse import urljoin

from django.conf import settings
from django.core.files.storage import FileSystemStorage


class CustomStorage(FileSystemStorage):
    """Custom storage for django_ckeditor_5 images"""

    location = os.path.join(settings.MEDIA_ROOT, "blog/images/uploads")
    base_url = urljoin(settings.MEDIA_URL, "blog/images/uploads/")

def get_filename(filename, request):
    return filename.upper()