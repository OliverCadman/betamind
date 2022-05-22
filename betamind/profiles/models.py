from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings


class UserProfile(models.Model):
    """
    Represents a User Profile Model

    Attributes:
        alias (CharField) - Option for a user to provide a custom username
        is_anonymous (Boolean) - Option for user to remain anonymous.
        profile_image (ImageField) - Profile image for user.
    """

    auth_user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_profile")
    alias = models.CharField(max_length=100, null=True, blank=True)
    is_anonymous = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to="uploads", null=True, blank=True)


    def __str__(self):
        if self.alias:
            return self.alias
        else:
            return "Default Alias"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user(sender, instance, created, **kwargs):
    """
    Create a User Profile when a user registers,
    or update the profile if it's already been created.
    """
    if created:
        UserProfile.objects.create(auth_user=instance)
        print(UserProfile.objects.get(auth_user=instance))

    # Otherwise, save the profile.
    instance.user_profile.save()

