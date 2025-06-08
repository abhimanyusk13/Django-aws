from django.db import models


class Example(models.Model):
    """Simple model used for demonstrations."""
    name = models.CharField(max_length=50)

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.name
