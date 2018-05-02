from django.db import models

# Create your models here.

class Tag(models.Model):
    title               = models.CharField(max_length=255)
    date_created        = models.DateTimeField(auto_now_add=True)
    date_modified       = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)

class Category(models.Model):
    title               = models.CharField(max_length=255)
    date_created        = models.DateTimeField(auto_now_add=True)
    date_modified       = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)

STATUS_CHOICES =(
        ('published', 'Published'),
        ('draft', 'Draft'),
        ('archived', 'Archived'),
        ('hidden', 'Hidden')
    )

class Post(models.Model):
    title               = models.CharField(max_length=255)
    subtitle            = models.CharField(max_length=255)
    banner_photo        = models.ImageField()
    tags                = models.ManyToManyField(Tag)
    category            = models.ForeignKey('Category', on_delete=models.CASCADE)
    body                = models.TextField()
    status              = models.CharField(
                                            max_length=9,
                                            choices=STATUS_CHOICES,
                                            default='published'
                                        )
    date_created        = models.DateTimeField(auto_now_add=True)
    date_modified       = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)
