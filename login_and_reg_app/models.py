from django.db import models
import re, bcrypt
from datetime import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class userManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        email_check = self.filter(email=postData['email'])
        if email_check:
            errors['email'] = "Email already in use"
        if len(postData['fName']) < 2:
            errors['fNameShort'] = "First Name must be longer than 2 characters"
        if len(postData['lName']) < 2:
            errors['lNameShort'] = "Last Name must be longer than 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors['passwordShort'] = "Password must be at least 8 characters"
        if postData['password'] != postData['confirm_password']:
            errors['passwordMatch'] = "Password and Confirm Password do not match"
        return errors
    def login_validator(self, postData):
        print(postData)
        errors = {}
        checkuser = User.objects.filter(email = postData['email'])
        if len(checkuser)<1:
            errors['noUser'] = "Invaild Email and Password combination"
        elif not bcrypt.checkpw(postData['password'].encode(),checkuser[0].password.encode()):
            errors['passwordNoMatch'] = "Invalid Email and Password combination"
        return errors
    def update_validator(self, postData):
        errors = {}
        email_check = self.filter(email=postData['email'])
        if email_check:
            errors['email'] = "Email already in use please choose another"
        if len(User.objects.filter(email=postData['email']))>0:
            if User.email != postData['email']:
                errors['EmailExists'] = "There's a user already using this email address."
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData['fName']) < 2:
            errors['fNameShort'] = "First Name must be longer than 2 characters"
        if len(postData['lName']) < 2:
            errors['lNameShort'] = "Last Name must be longer than 2 characters"
        return errors

class User(models.Model):
    fName = models.CharField(max_length=32)
    lName = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = userManager()
