from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class MovieReview(models.Model):
    created_by = models.ForeignKey(
        User, related_name="movie_reviews", on_delete=models.CASCADE, null=True
    )
    title = models.CharField(max_length=200)
    headline = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    link = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(
        verbose_name="image", upload_to="reviews/images", blank=True
    )

    def __str__(self):
        return f"{self.title} - {self.headline}"

    def save(self, **kwargs):
        if not self.pk and self.publication_date is None:
            self.publication_date = timezone.now().date()

        return super().save(kwargs)
