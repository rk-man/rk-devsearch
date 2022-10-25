
import uuid
from django.db import models
from users.models import Profile

# Create your models here.


# by default DJango creates an id field
class Project(models.Model):
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    # null = True -> for the database

    description = models.TextField(null=True, blank=True)
    # blank = True -> it's for the django to know we can pass the data in the request with this property being empty

    featured_image = models.ImageField(
        null=True, blank=True, default="default.jpg")

    demo_link = models.CharField(max_length=2000, null=True, blank=True)

    source_link = models.CharField(max_length=2000, null=True, blank=True)

    tags = models.ManyToManyField('Tag', blank=True)

    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)

    # auto_now_add -> generates a new datetime field when a new doc is created
    created_at = models.DateTimeField(auto_now_add=True)

    # overriding the built in id field of Django
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    # __str__ when we call print or str on a object then the below code is executed

    def __str__(self):
        return self.title


class Review(models.Model):

    # enum values can be used liked this
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    VOTE_TYPE = (
        ("up", "Up Vote"),
        ("down", "Down Vote"),
    )

    # owner =
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    # there can't be two objects of Review Model with the same owner and same project
    class Meta:
        unique_together = [['owner', 'project']]

    def __str__(self):
        return self.value


# Projects -> <- Reviews > Many to Many
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name
