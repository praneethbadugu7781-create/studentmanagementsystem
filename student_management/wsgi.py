"""
WSGI config for student_management project.
Production and Vercel serverless compatible entrypoint.
"""

import os
import shutil
from pathlib import Path
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management.settings')

# Automatic SQLite initialization for Vercel Serverless
if os.environ.get('VERCEL'):
    base_dir = Path(__file__).resolve().parent.parent
    src_db = base_dir / 'db.sqlite3'
    dst_db = Path('/tmp/db.sqlite3')
    
    if src_db.exists() and not dst_db.exists():
        try:
            shutil.copyfile(src_db, dst_db)
        except Exception:
            pass

application = get_wsgi_application()

# If running on Vercel and DB tables need migration fallback
if os.environ.get('VERCEL'):
    try:
        from django.core.management import call_command
        call_command('migrate', interactive=False)
        try:
            call_command('create_admin', interactive=False)
        except Exception:
            pass
        try:
            from students.models import Student
            if Student.objects.count() == 0:
                call_command('seed_students', interactive=False)
        except Exception:
            pass
    except Exception as e:
        print(f"Startup migration status: {e}")

app = application
