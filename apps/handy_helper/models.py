from django.db import models
from apps.login_registration.models import User
from django.contrib import messages

class JobManager(models.Manager):
    def validateNewJob(self, postData):
        print("\n\n** Validating Job")
        errors = {}

        if len(postData['title']) < 4:
            errors['title'] = "Title is too short."

        if len(postData['description']) < 11:
            errors['description'] = "Description is too short."

        if len(postData['location']) < 1:
            errors['location'] = "Title must not be blank"

        return errors

class Job(models.Model):
    title = models.CharField(max_length = 32)
    description = models.TextField()
    location = models.CharField(max_length = 128)
    creator = models.ForeignKey(User, related_name='jobs', on_delete = models.CASCADE)
    workers = models.ManyToManyField(User, related_name='workers')
    created_on = models.DateField(auto_now_add=True)

    objects = JobManager()

    def __repr__(self):
        return (f'<Job: {self.title}>')
    def __str__(self):
        return (f'<Job: {self.title}>')
