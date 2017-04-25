import media
import fresh_tomatoes

toy_story = media.Movie('Toy Story',
    'A story of a boy and his toys that come to life',
    'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
    'https://www.youtube.com/watch?v=KYz2wyBy3kc&t=3s')

avatar = media.Movie('Avatar',
    'A marine on an alien planet',
    'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
    'https://www.youtube.com/watch?v=5PSNL1qE6VY')

matrix = media.Movie('Matrix',
    'Neo believes that Morpheus, an elusive figure considered to be the most' +
    'dangerous man alive, can answer his question -- What is the Matrix?',
    'https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg', # NOQA
    'https://www.youtube.com/watch?v=m8e-FF8MsqU')

school_of_rock = media.Movie('School of Rock',
    'Using rock music to learn',
    'https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg',
    'https://www.youtube.com/watch?v=XCwy6lW5Ixc')

ratatouille = media.Movie('Ratatouille',
    'A rat is a chef in Paris',
    'http://www.pixartalk.com/wp-content/uploads/2009/06/ratus1.jpg',
    'https://www.youtube.com/watch?v=c3sBBRxDAqk')

midnight_in_paris = media.Movie('Midnight in Paris',
    'Going back in time to meet authors',
    'https://images-na.ssl-images-amazon.com/images/I/61uuYEUFw4L._SY450_.jpg',
    'https://www.youtube.com/watch?v=FAfR8omt-CY')

movies = [toy_story, avatar, matrix, school_of_rock, ratatouille, midnight_in_paris]
fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)