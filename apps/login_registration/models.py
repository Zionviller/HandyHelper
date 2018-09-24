from django.db import models
import bcrypt, re

ALPHA_REGEX = re.compile(r'[a-zA-Z]')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validateNewUser(self, postData):
        print("\n\n** Validating Registration")
        errors = {}

        if len(postData['first_name']) < 2:
            errors['first_name'] = "first_name is too short."
        elif not ALPHA_REGEX.match(postData['first_name']):
            errors['first_name'] = 'first_name must contain only letters'

        if len(postData['last_name']) < 2:
            errors['last_name'] = "last_name is too short"
        elif not ALPHA_REGEX.match(postData['last_name']):
            errors['last_name'] = 'first_name must contain only letters'

        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'enter valid email.'

        print(len(postData['password']))
        if len(postData['password']) < 8:
            errors['password'] = "password must be 8 characters or longer"

        if postData['password'] != postData['pw_confirm']:
            errors['confirm'] = 'password and confirmation must match'

        return errors

    def validateLogin(self, postData):
        print('\n\n** Validating Login')

        errors = {}
        u = User.objects.filter(email = postData['email'])
        print(u)

        if len(u) <= 0:
            errors['login'] = "Can't find that email.."
            return errors

        if not bcrypt.checkpw(postData['password'].encode('utf-8'), u[0].pass_hash.encode('utf-8')):
            errors['password'] = "Password is bunk.."

        return errors
class User(models.Model):
    first_name = models.CharField(max_length = 32)
    last_name = models.CharField(max_length = 32)
    email = models.CharField(max_length = 128)
    pass_hash = models.CharField(max_length = 255)
    objects = UserManager()
    def __repr__(self):
        return f'User: { self.email }'
    def __str__(self):
        return f'{ self.email }'
