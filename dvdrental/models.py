from django.db import models

class Actor(models.Model):
    class Meta:
        db_table = 'actor'
    
    actor_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)

    def __str__(self):
        return "[{}] - {} {}".format(self.actor_id,     self.first_name, self.last_name)

    
class Film(models.Model):
    class Meta:
        db_table = 'film'
    
    film_id = models.IntegerField(primary_key=True)
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
    special_features = models.CharField(max_length=255)
    last_update = models.DateTimeField()
    
    def __str__(self):
        return "[{}] - {}, {}".format(self.film_id, self.title, self.release_year)