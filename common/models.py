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
        managed = False 
        db_table = 'Person'
        unique_together = ('FirstName', 'LastName', 'birthday')
        ordering = ['FirstName', 'LastName']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Photo(models.Model):
    photo_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    photo_path = models.CharField(max_length=30)

    class Meta:
        managed = False 
        db_table = 'Photo'

    def __str__(self):
        return f"Photo {self.photo_id} for {self.person}"

class Interests(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    interest = models.CharField(max_length=40)

    class Meta:
        managed = False 
        db_table = 'Interests'
        unique_together = ('person', 'interest')

    def __str__(self):
        return f"{self.person}'s Interest: {self.interest}"

class Spouse(models.Model):
    spouse1 = models.ForeignKey(Person, related_name='spouse1', on_delete=models.CASCADE)
    spouse2 = models.ForeignKey(Person, related_name='spouse2', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Spouse'
        unique_together = ('spouse1', 'spouse2')

    def __str__(self):
        return f"{self.spouse1} & {self.spouse2}"

class Household(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly define id field
    parents = models.ForeignKey(Person, related_name='parents', on_delete=models.CASCADE)
    child = models.ForeignKey(Person, related_name='child', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'Household'
        unique_together = ('parents', 'child')

    def __str__(self):
        return f"{self.parents} & {self.child}"

