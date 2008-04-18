#!/usr/bin/env python
from django.core.management import execute_manager
try:
    import settings
except ImportError, e:
    import sys
    sys.stderr.write("canot find settings: %s\n" % e)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)
