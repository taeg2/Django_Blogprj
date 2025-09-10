from django.db import models

# Create your models here.
class Posting(models.Model):
    title = models.CharField()
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title


class Reples(models.Model):
    post = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name="reples")
    comments = models.CharField()
    date = models.DateField()

    def __str__(self):
        return f"댓글({self.post.title})"
    
