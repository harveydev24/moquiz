from django.db.models import *

# Create your models here.


class Actor(Model):
    name = CharField(max_length=30)

    def __str__(self):
        return self.name


class Movie(Model):
    title = CharField(max_length=50)
    title_initial = CharField(max_length=50, null=True)
    actors = ManyToManyField(Actor, related_name="movies")

    def __str__(self):
        return self.title


class Movie_Image(Model):
    movie = ForeignKey(Movie, on_delete=CASCADE)
    image_url = TextField()

    def __str__(self):
        return self.movie.title


class Famous_Line(Model):
    movie = ForeignKey(Movie, on_delete=CASCADE)
    line = TextField()
    line_initial = TextField(null=True)

    def __str__(self):
        return self.line
