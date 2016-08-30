class Song(object):
#how can this count words in song?
	number_of_words = 0

	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line	
			
	def count_words(self):
		print "I have %s words" % self.words
					
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there",
					"Happy birthday to you\n"])
					
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells\n"])	
						
twinkle_twinkle = Song(["Twinkle, twinkle, little star",
						"How I wonder what you are",
						"Up above the world so high",
						"Like a diamond in the sky",
						"Twinkle, twinkle, little star\n"])
									
Itsy_bitsy = Song(["The itsy bitsy spider",
					"Climbed up the water spout",
					"Down came the rain and washed the spider out",
					"Up came the sun and dried out all the rainbows",
					"And the itsy bitsy spider climbed up the spout again\n"])
			
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()	

twinkle_twinkle.sing_me_a_song()	

Itsy_bitsy.sing_me_a_song()	

lullaby = Song(["lullaby and goodnight",
				"Go to sleep little baby",
				"I don't know how this song goes",
				"because I don't have a kid"])
				
lullaby.sing_me_a_song() 

happy_bday.count_words()

lullaby.count_words()



