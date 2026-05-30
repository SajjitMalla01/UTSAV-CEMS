import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cems.settings")
django.setup()

from tenants.models import College

print("=== College Accounts ===")
colleges = College.objects.all()
for college in colleges:
    print(f"\n[{college.name}]")
    profiles = college.profiles.select_related("user").all()
    if not profiles:
        print("  (No accounts found)")
    for profile in profiles:
        print(
            f"  - {profile.user.username:<15} | Role: {profile.role:<10} | Email: {profile.user.email}"
        )
