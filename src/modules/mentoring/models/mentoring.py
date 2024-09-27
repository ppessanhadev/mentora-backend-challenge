from django.db import models


class MentoringModel(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "mentories"
        verbose_name = "Mentoring"
        verbose_name_plural = "Mentories"
