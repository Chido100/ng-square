from .base import * #noqa
from .base import env



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY", default="lvMTCrYQrMCWziGFvvD_up_lg3eD6y2VMrk0lf4fUi2-rrM9WjY",)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

