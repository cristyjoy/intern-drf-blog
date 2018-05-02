from django.db import models
STATUS_CHOICES = (('published', 'Published'), ('draft', 'Draft'), ('archived', 'Archived'),)
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    sub_Title = models.CharField(max_length=150)
    banner_Photo = models.ImageField(upload_to = 'static/media')
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag',related_name="Post")
    status = models.CharField(max_length=10, default='published', choices=STATUS_CHOICES)

    def __str__(self):
        return '{}'.format(self.title)

class Category(models.Model):
   title                   = models.CharField(max_length=120)
   date_created            = models.DateTimeField(auto_now_add=True)
   date_modified           = models.DateTimeField(auto_now=True)

   def __str__(self):
       return '{}'.format(self.title)
        
class Tag(models.Model):
   title                   = models.CharField(max_length=120)
   date_created            = models.DateTimeField(auto_now_add=True)
   date_modified           = models.DateTimeField(auto_now=True)

   def __str__(self):
       return '{}'.format(self.title)

   class Meta:
       ordering = ['title',]

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.TextField()
    author = models.CharField(max_length=150)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.title)