from dao.main import GenresDAO
from dao.main import MoviesDAO
from dao.main import DirectorsDAO
from dao.main import UsersDAO

from services import GenresService
from services import MoviesService
from services import DirectorsService
from services import UsersService

from setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
movie_dao = MoviesDAO(db.session)
director_dao = DirectorsDAO(db.session)
user_dao = UsersDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
movie_service = MoviesService(dao=movie_dao)
director_service = DirectorsService(dao=director_dao)
user_service = UsersService(dao=user_dao)
