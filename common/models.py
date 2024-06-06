from django.db import models

class Person(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Non-binary', 'Non-binary'),
    ]

    Id = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=40)
    LastName = models.CharField(max_length=40)
    Birthday = models.DateField()
    Nickname = models.CharField(max_length=40)
    YearDied = models.IntegerField()
    Gender = models.CharField(max_length=11, choices=GENDER_CHOICES, null=True, blank=True)
    Pronouns = models.CharField(max_length=20, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Cell = models.CharField(max_length=20, null=True, blank=True)
    CityBorn = models.CharField(max_length=30, null=True, blank=True)
    StateBorn = models.CharField(max_length=30, null=True, blank=True)
    CountryBorn = models.CharField(max_length=30, null=True, blank=True)
    CityCurrent = models.CharField(max_length=30, null=True, blank=True)
    StateCurrent = models.CharField(max_length=30, null=True, blank=True)
    CountryCurrent = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        managed = False 
        db_table = 'Person'
        unique_together = ('FirstName', 'LastName', 'Birthday')
        ordering = ['FirstName', 'LastName']

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

class Photo(models.Model):
    PhotoID = models.AutoField(primary_key=True)
    PersonID = models.ForeignKey(Person, on_delete=models.CASCADE)
    PhotoPath = models.CharField(max_length=30)

    class Meta:
        managed = False 
        db_table = 'Photo'

    def __str__(self):
        return f"Photo {self.PhotoID} for {self.Person}"

class Interests(models.Model):
    PersonID = models.ForeignKey(Person, db_column='PersonID', on_delete=models.CASCADE, primary_key=True)
    Interest = models.CharField(max_length=40)

    class Meta:
        managed = False  # Assuming you're managing this table externally
        db_table = 'Interests'
        unique_together = ('PersonID', 'Interest')

    def __str__(self):
        return f"{self.PersonID}'s Interest: {self.Interest}"

class Spouse(models.Model):
    Spouse1ID = models.ForeignKey(Person, related_name='spouse1_set', db_column='Spouse1ID', on_delete=models.CASCADE)
    Spouse2ID = models.ForeignKey(Person, related_name='spouse2_set', db_column='Spouse2ID', on_delete=models.CASCADE)

    class Meta:
        db_table = 'Spouse'
        unique_together = ('Spouse1ID', 'Spouse2ID')

    def __str__(self):
        return f"{self.Spouse1ID} & {self.Spouse2ID}"


class Household(models.Model):
    Parent1ID = models.ForeignKey(
        Person,
        related_name='parent1_relationships',
        db_column='Parent1ID',
        on_delete=models.CASCADE
    )
    Parent2ID = models.ForeignKey(
        Person,
        related_name='parent2_relationships',
        db_column='Parent2ID',
        null=True,  # Parent2ID can be NULL in the database
        blank=True,  # Allow Parent2ID to be blank
        on_delete=models.CASCADE
    )
    ChildID = models.ForeignKey(
        Person,
        related_name='child_relationships',
        db_column='ChildID',
        on_delete=models.CASCADE
    )

    class Meta:
        managed = False  # Tells Django not to manage this table (since it's managed by SQL directly)
        db_table = 'Household'
        unique_together = ('Parent1ID', 'ChildID')

    def __str__(self):
        return f"{self.Parent1ID} & {self.ChildID}"
