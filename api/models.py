from django.db import models
# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token


class Book(models.Model):
    owner = models.ForeignKey('auth.User', related_name='books', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=False)
    author = models.CharField(max_length=50, blank=False)
    add_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{} by {}'.format(self.name, self.author)


# @receiver(post_save, sender=User)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
