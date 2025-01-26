from django.db import models
from django.contrib.postgres.fields import ArrayField

class Actor(models.Model):
    class Meta:
        db_table = 'actor'
    
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField()

    # TODO sprawdzic jak ustawic relacje w obie strony
    # film = models.ManyToManyField('Film', db_table='film_actor')

    def __str__(self):
        return "[{}] - {} {}".format(self.actor_id,     self.first_name, self.last_name)


class Language(models.Model):
    class Meta:
        db_table = 'language'
    
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_update = models.DateTimeField()
    
    def __str__(self):
        return "[{}] - {}".format(self.language_id, self.name)

class Film(models.Model):
    class Meta:
        db_table = 'film'
    
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_year = models.IntegerField()
    # language_id = models.ForeignKey('Language', on_delete=models.CASCADE)
    # original_language_id = models.ForeignKey('Language', on_delete=models.CASCADE)
    rental_duration = models.IntegerField()
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.IntegerField()
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.CharField(max_length=5)
    special_features = ArrayField(models.CharField(max_length=255))
    last_update = models.DateTimeField()

    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    actor = models.ManyToManyField(Actor)
    
    def __str__(self):
        return "[{}] - {}, {}".format(self.film_id, self.title, self.release_year)
    
