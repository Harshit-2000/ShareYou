from django.db import models
from django.conf import settings

# Create your models here.


class Photo(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length=300, blank=True)
    uploader = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    upladed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.caption


class Blog(models.Model):
    image = models.ForeignKey(
        Photo, null=True, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=3000)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)
    word_count = models.IntegerField(null=True, blank=True)

    def count_words(self):
        count = 0
        for char in self.content:
            if char == " ":
                count += 1

        self.word_count = count

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.count_words()
        super(Blog, self).save(*args, **kwargs)
