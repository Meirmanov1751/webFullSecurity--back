from django.db import models


# Create your models here.
class Post(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post")
    title = models.CharField(max_length=200)
    short_description = models.TextField(blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'name:{self.title} create at:{self.created_at} update at:{self.updated_at}'

    class Meta:
        ordering = ["title"]
        verbose_name = "Пост"
        verbose_name_plural = "Посттар"
