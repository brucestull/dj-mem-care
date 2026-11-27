from django.db import models


class Confabulation(models.Model):
    """Something a loved one with dementia says that reflects a distorted or
    invented memory. Shared by all users (no user link yet)."""

    text = models.TextField(
        unique=True,
        help_text="What the loved one says, e.g. 'I need to pick the kids up from school.'",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["text"]

    def __str__(self):
        return self.text if len(self.text) <= 60 else self.text[:57] + "..."
