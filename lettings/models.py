from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """Adresses model
    Inherited from the Model class of Django
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        """Called when user need an address to string for display

        Returns:
            A string
        """
        return f"{self.number} {self.street}"

    class Meta:
        """Generate correct plural for this model"""

        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """Lettings model
    inherited from the Model class of django
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """Return the letting title"""
        return self.title
