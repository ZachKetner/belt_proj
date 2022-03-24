from django.db import models
from login_and_reg_app.models import *
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class QuoteManager(models.Manager):
    def quote_validator(self, postData):
        errors = {}
        if len(postData['author']) < 3:
            errors['authorShort'] = "Author name entered must be longer than three characters.            "
        if len(postData['description']) < 10:
            errors['descShort'] = "Quote must be longer than 10 characters please."
        return errors

class Quotes(models.Model):
    author = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quoter = models.ForeignKey(User, related_name="quotes", on_delete=models.CASCADE)
    quote_likes = models.ManyToManyField(User, related_name='liked_quotes')

    objects = QuoteManager()
# Create your models here.
