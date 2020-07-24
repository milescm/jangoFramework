from django.db import models
from django.conf import settings
from django.utils import timezone

## Define Object (= model)
class Post(models.Model):
    # Foreignkey = Link for other models
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # CharField is limit
    title = models.CharField(max_length=200)
    # TextField is unlimit
    text = models.TextField()
    created_date = models.DateTimeField(
        default = timezone.now
    )    
    published_date = models.DateTimeField(
        blank = True, null = True
    )

def publish(self):
    self.published_date = timezone.now()
    self.save()


def __str__(self):
    return self.title


