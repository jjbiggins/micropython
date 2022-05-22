import os

# Directory that the project lives in, aka ../..
SITE_ROOT = '/'.join(os.path.dirname(__file__).split('/')[:-2])

TEMPLATE_DIRS = (
    f"{SITE_ROOT}/templates/",
    f"{SITE_ROOT}/readthedocs/templates/",
)
