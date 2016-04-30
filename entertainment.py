import media
import fresh_tomatoes

frozen_movie = media.Movie('Frozen',
	'the film tells the story of a fearless princess who sets off on' +
	'an epic journey alongside a rugged iceman, his loyal pet reindeer,' +
	'and a snowman to find her estranged sister, whose icy powers have '+
	'inadvertently trapped the kingdom in eternal winter.',
	'https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg',
	'https://www.youtube.com/watch?v=TbQm5doF_Uc',
	2, 3)
	
gladiator_movie = media.Movie('Gladiator',
	'Story of true warrior',
	'http://cfile221.uf.daum.net/image/037B4A34511F4A0902E712',
	'https://www.youtube.com/watch?v=IvTT29cavKo',
	2.5, 1)
	
avengers_movie = media.Movie('Lagaan',
	'Story of super heros, saving the world',
	'http://downloadsfreemovie.cc/wp-content/uploads/2015/04/Avengers-2-Age-of-Ultron-Poster-2.jpg',
	'https://www.youtube.com/watch?v=bMP-FLmiIM0',
	1.8, 2)
	
lagaan_movie = media.Movie('Lagaan',
	'Cricket for freedom. Cricket for dreams.',
	'https://upload.wikimedia.org/wikipedia/en/9/9c/Lagaan_Soundtrack.JPG',
	'https://www.youtube.com/watch?v=oSIGQ0YkFxs',
	2.5, 3)
	
	
movies = [frozen_movie, gladiator_movie, avengers_movie, lagaan_movie]

fresh_tomatoes.open_movies_page(movies)
