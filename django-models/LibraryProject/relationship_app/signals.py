from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile, UserRole

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver to create or update a UserProfile whenever a User is saved.
    If a new User is created, a UserProfile is automatically created with a default role.
    """
    if created:
        # Create a new UserProfile for the newly created User
        UserProfile.objects.create(user=instance, role=UserRole.MEMBER)
    # If the user already exists, ensure their profile exists (e.g., if created via loaddata)
    instance.profile.save()