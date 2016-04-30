import webbrowser

class Video:
	
	"""This is a Video Class, which holds title and duration of a video.
    
    Attributes:
        title (str): This is title of the video.
        duration (int): This is duration of the video in hours.
    """
	def __init__(self, title, duration):
		"""This is a constructor with initiates the Video Object by taking video information."""
		self.title = title
		self.duration = duration #Duration in hours
		
class Movie(Video):
	"""This is a Movie Class, which holds all the information of a movie. It inherits Video class.
    
    Attributes:
        title (str): This is title of the video.
        duration (int): This is duration of the video in hours.
		storyline (str): This holds storyline of the movie
		poster_image_url (str): This holds url for movie poster.
		trailer_youtube_url (str): This holds url for movie youtube trailer.
		rating (int): Movie rating
	Methods:
		show_trailer: Open trailer of the movie in browser
    """
	
	VALID_RATINGS = ["BAD", "NICE", "VERY NICE", "AWESOME"]
	def __init__(self, title, storyline, image, trailer, duration, rating):
		"""This is a constructor with initiates the Movie Object by taking movie information as input (title, storyline, duration, rating, poster_image_url, trailer_youtube_url)"""
		Video.__init__(self, title, duration)
		self.storyline = storyline
		self.poster_image_url = image
		self.trailer_youtube_url = trailer
		self.rating = self.VALID_RATINGS[rating]
	
	def show_trailer(self):
		"""This is a method, which on invocation open up browser window with youtube trailer of the movie"""
		webbrowser.open(self.trailer)
	
