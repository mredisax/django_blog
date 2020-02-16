from django.db import models
from datetime import datetime
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.contrib import admin
from ckeditor_uploader.fields import RichTextUploadingField

User = get_user_model()


class Category(models.Model):
    name = models.CharField('Category name', max_length=100)
    slug = models.SlugField('Url', max_length=300, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        kwarg={
            'slug': self.slug
        }
        return reverse("post_views", kwargs=kwargs)


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField('Avatar', upload_to='blog/static/img/avatar', null=True, blank=True)
    bio = models.TextField('Enter your bio details here.', max_length=400)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now)
    content = models.TextField()
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField('Title',max_length=200)
    thumbnail = models.ImageField('Thumbnail', upload_to='blog/static/img', blank=True,)
    content = RichTextUploadingField()
    published = models.DateTimeField('date published', default=datetime.now)
    slug = models.SlugField('Url', max_length=300, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name="Category", default=1, on_delete=models.SET_DEFAULT)

    def get_absolute_url(self):
        kwargs={
            'pk': self.pk,
            'slug': self.slug
            }
        return reverse("post_views", kwargs=kwargs)
    
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    @property
    def count_comment(self):
        return Comment.objects.filter(post=self).count()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

        

    
