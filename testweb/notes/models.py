from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=300, blank=True)

# The methods below allow for the UserProfile class to update alongside
# the User table inside of Django

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

class note(models.Model):
    user = models.ForeignKey(User, default=1, null=True) #Each note belongs to a user
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=200)


    def get_absolute_url(self):
        return reverse('notes:detail', kwargs={'pk': self.pk})
        #kwargs is keyword argument

    def __str__(self):
        return self.title + ", " + self.content


class mention(models.Model):
    mention_name = models.CharField(max_length=150)
    note_in = models.ForeignKey(note, on_delete=models.CASCADE)
   # is_favorite = models.BooleanField(default=False)

    # if the not is deleted, the mention is unimportant
    # so delete it also
    def __str__(self):
        return str(self.mention_name)
        # note_in returns an note object
