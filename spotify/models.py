from django.db import models

# Create your models here.
GENRE_CHOICES = [
    ("B", "Blues"),
    ("AB", "Afrobeats"),
    ("C", "Country"),
    ("P", "POP"),
    ("HP", "HIP HOP")
]

class Artist(models.Model):
    name = models.CharField(max_length=100)
    images = models.ImageField(upload_to='artist_images', blank=True, null=True)



    class Meta:
        verbose_name_plural = "Artist"

    def __str__(self):
        return self.name
    


class Songs(models.Model):
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    images = models.ImageField(upload_to='songimages', blank=True, null=True)
    lyrics = models.TextField(max_length=10000, blank=True, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    rating = models.IntegerField()
    genre = models.CharField(max_length=5, choices=GENRE_CHOICES )


    class Meta:
        verbose_name_plural = "Songs"

    def __str__(self):
        return self.name