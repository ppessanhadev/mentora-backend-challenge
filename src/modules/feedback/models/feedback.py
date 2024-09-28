from django.db import models
from ...mentoring.models import MentoringModel


stars_choices = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
]


class FeedbackModel(models.Model):
    name = models.CharField(max_length=30)
    message = models.TextField()
    stars = models.IntegerField("stars", choices=stars_choices)
    mentoring = models.ForeignKey(MentoringModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        "created_at", auto_now_add=True, blank=True, null=True
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "feedbacks"
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"
