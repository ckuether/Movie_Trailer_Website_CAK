import webbrowser

class Movie():
    """This class provides a way to store movie related information including
    title, storyline, poster image, and the movie trailer.  This class also
    provides methods to open the trailer in a web browser"""

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    # This initializes a new movie instance, user must provide a movie title,
    # storyline, poster image url, and youtube trailer url
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)