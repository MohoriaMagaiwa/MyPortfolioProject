
import sys
from pathlib import Path

import os

# Make the repository root available for Django imports.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.cloudflare_settings",
)

from django.core.wsgi import get_wsgi_application
from workers import wsgi

django_app = get_wsgi_application()

Default = wsgi.entrypoint(django_app)
