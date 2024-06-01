from django.db import models

class Person(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Non-binary', 'Non-binary'),
    ]

    id = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=40)
    LastName = models.CharField(max_length=40)
    birthday = models.DateField()
    IsAlive = models.BooleanField(default=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=11, choices=GENDER_CHOICES, null=True, blank=True)
    pronouns = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    cell = models.CharField(max_length=20, null=True, blank=True)
    CityBorn = models.CharField(max_length=30, null=True, blank=True)
    StateBorn = models.CharField(max_length=30, null=True, blank=True)
    CountryBorn = models.CharField(max_length=30, null=True, blank=True)
    CityCurrent = models.CharField(max_length=30, null=True, blank=True)
    StateCurrent = models.CharField(max_length=30, null=True, blank=True)
    CountryCurrent = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        managed = False  # This tells Django not to manage the table's schema
        db_table = 'Person'
        unique_together = ('FirstName', 'LastName', 'birthday')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Photo(models.Model):
    photo_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    photo_path = models.CharField(max_length=30)

    class Meta:
        db_table = 'Photo'

    def __str__(self):
        return f"Photo {self.photo_id} for {self.person}"