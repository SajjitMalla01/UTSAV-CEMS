import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cems.settings")
django.setup()

from django.contrib.auth.models import User
from accounts.models import Profile


def stabilize_admins():
    print("Stabilizing Admin accounts...")

    # Target only utsav_admin as the global superadmin
    admin_usernames = ["utsav_admin"]

    for username in admin_usernames:
        try:
            user = User.objects.get(username=username)
            user.is_staff = True
            user.is_superuser = True
            user.save()

            profile, created = Profile.objects.get_or_create(user=user)
            profile.role = "ADMIN"
            profile.is_approved = True
            profile.save()

            print(f"   [OK] Stabilized {username} as global super admin")
        except User.DoesNotExist:
            print(f"   [SKIP] User {username} not found")


if __name__ == "__main__":
    stabilize_admins()
