from django.db import models

# Create your models here.
PARTY = [
    ('R', 'Republican'),
    ('D', 'Democratic')
]

class State(models.Model):
    name = models.CharField(max_length=100, unique=True)
    abbreviation = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.name

class District(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    district = models.IntegerField() 
    republican_votes = models.IntegerField()
    democratic_votes = models.IntegerField()
    area = models.FloatField()
    perimeter = models.FloatField()
    congress = models.IntegerField()
    party = models.CharField(max_length=1, default="", choices=PARTY)
    
    
    def district_name(self):
        return self.name