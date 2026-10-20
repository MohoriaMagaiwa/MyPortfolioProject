

"""
Cloudflare-specific settings.
The original config/settings.py remains unchanged.
"""

from .settings import *
from workers import env

DEBUG = False
SECRET_KEY = env.DJANGO_SECRET_KEY

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".workers.dev",
]

# Cloudflare serves static assets separately.
MIDDLEWARE = [
    item for item in MIDDLEWARE
    if item != "whitenoise.middleware.WhiteNoiseMiddleware"
]

# Initial portfolio test only: no persistent database.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# Keep sessions independent of the temporary database.
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"


# Static assets are served directly by Cloudflare.
STATICFILES_DIRS = []
STATIC_ROOT = BASE_DIR / "staticfiles"

# Do not use WhiteNoise storage on Cloudflare.
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}
