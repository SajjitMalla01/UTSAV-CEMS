import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cems.settings")
django.setup()

from django.contrib.auth.models import User
from accounts.models import Profile, EmailVerification
from tenants.models import College
from django.utils import timezone


def rebuild():
    print("--- Rebuilding UTSAV Account Directory ---")

    # 1. Clean up all existing users (ensures pristine directory)
    print("Clearing out old user accounts...")
    User.objects.all().delete()

    # 2. Get all active colleges
    colleges = College.objects.filter(status="ACTIVE")
    if not colleges.exists():
        print("Error: No active colleges found. Run setup_colleges.py first.")
        return

    # Find Herald College for the default global super admin context
    herald = College.objects.filter(slug="herald-college").first() or colleges.first()

    # 3. Create the global Super Admin (utsav_admin)
    print("\nCreating Global Super Admin...")
    su = User.objects.create_user(
        username="utsav_admin",
        email="np03cs4a230357@heraldcollege.edu.np",
        password="UtsavPass123!",
    )
    su.is_superuser = True
    su.is_staff = True
    su.save()

    # Create profile for super admin
    su_profile, _ = Profile.objects.get_or_create(user=su)
    su_profile.role = "ADMIN"
    su_profile.college = herald
    su_profile.is_approved = True
    su_profile.save()

    # Verify super admin email
    EmailVerification.objects.update_or_create(
        user=su,
        defaults={
            "is_verified": True,
            "expires_at": timezone.now() + timezone.timedelta(days=365),
        },
    )
    print(
        f"   [OK] Created global super admin: utsav_admin (Default portal: {herald.name})"
    )

    # Create the global Demo Student (utsav_student)
    student = User.objects.create_user(
        username="utsav_student",
        email="np03cs4a230357@heraldcollege.edu.np",
        password="UtsavPass123!",
    )
    student.is_superuser = False
    student.is_staff = False
    student.save()

    stud_profile, _ = Profile.objects.get_or_create(user=student)
    stud_profile.role = "STUDENT"
    stud_profile.college = herald
    stud_profile.is_approved = True
    stud_profile.save()

    EmailVerification.objects.update_or_create(
        user=student,
        defaults={
            "is_verified": True,
            "expires_at": timezone.now() + timezone.timedelta(days=365),
        },
    )
    print("   [OK] Created demo student: utsav_student")

    # 4. Create 1 Admin and 2 Staff for EACH college
    print("\nGenerating College-Level Accounts (1 Admin, 2 Staff per college)...")
    for college in colleges:
        # Clean slug representation: herald-college -> herald
        clean_slug = college.slug.replace("-college", "").replace("-", "_")

        accounts_to_create = [
            {
                "username": f"{clean_slug}_admin",
                "role": "ADMIN",
                "is_staff": False,  # Normal portal users, not django-admin users
            },
            {
                "username": f"{clean_slug}_staff1",
                "role": "STAFF",
                "is_staff": False,
            },
            {
                "username": f"{clean_slug}_staff2",
                "role": "STAFF",
                "is_staff": False,
            },
        ]

        for data in accounts_to_create:
            user = User.objects.create_user(
                username=data["username"],
                email="np03cs4a230357@heraldcollege.edu.np",  # Standard notification email
                password="UtsavPass123!",
            )
            user.is_superuser = False
            user.is_staff = data["is_staff"]
            user.save()

            # Create matching Profile
            profile, _ = Profile.objects.get_or_create(user=user)
            profile.role = data["role"]
            profile.college = college
            profile.is_approved = True  # Auto-approve initial golden profiles
            profile.save()

            # Verify Email
            EmailVerification.objects.update_or_create(
                user=user,
                defaults={
                    "is_verified": True,
                    "expires_at": timezone.now() + timezone.timedelta(days=365),
                },
            )
            print(
                f"   [OK] Created {data['role']}: {data['username']} (College: {college.name})"
            )

    print("\nDATABASE ACCOUNT REBUILD SUCCESSFUL.")
    print("All college-level admins & staff accounts created.")
    print("Password for all accounts: UtsavPass123!")


if __name__ == "__main__":
    rebuild()
