from peewee import *
from datetime import datetime
import hashlib

# Conexión a la base de datos
database = MySQLDatabase('fastapi_project',
                         user='root',
                         password='rN#e7$BGG6rv&f',
                         host='localhost',
                         port=3306)


class User(Model):
    username = CharField(max_length=50, unique=True)
    password = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.now)

    def __str__(self):
        return self.username

    class Meta:
        database = database
        table_name = 'users'

    @classmethod
    def authenticate(cls, username, password):
        user = cls.select().where(User.username == username).first()

        if user and user.password == cls.create_password(password):
            return user

    @classmethod
    def create_password(cls, password):
        h = hashlib.md5()
        h.update(password.encode('utf-8'))
        return h.hexdigest()


class Movie(Model):
    title = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        database = database
        table_name = 'movies'

# Relaciones
# Un usuario puede tener muchas reseñas
# Una reseña le pertenece a un usuario
# Una pelicula puede tener muchas reseñas
# Una reseña le pertenece a una pelicula
# Nos apoyaremos de 2 llaves foráneas para crear las relaciones


class UserReview(Model):
    # Utilizando el atributo reviews un usuario podrá acceder a todas sus reseñas
    user = ForeignKeyField(User, backref='reviews')
    movie = ForeignKeyField(Movie, backref='reviews')
    review = TextField()
    score = IntegerField()
    created_at = DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'

    class Meta:
        database = database
        table_name = 'user_reviews'
