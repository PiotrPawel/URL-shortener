from django.db import models
from .utils import generate_short_code


class UserUrl(models.Model):
    long_url = models.URLField('URL', max_length=200)
    short_url = models.CharField(max_length=30, blank=True, unique=True)

    def __str__(self):
        return self.long_url

    def save(self, *args, **kwargs):
        if self.short_url is None or self.short_url == "":
            self.short_url = generate_short_code()
        super(UserUrl, self).save(*args, **kwargs)

    def get_short_url(self):
        return f"http://www.shortenlink.com/{self.short_url}"

    def get_full_url(self):
        return f"http://www.shortenlink.com/{self.short_url}"
