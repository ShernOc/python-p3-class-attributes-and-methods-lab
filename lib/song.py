#Song to produce individual songs:
#song class to produce individual songs 


#Song class to keep track of the number of songs in that class. 
class Song:
    count = 0
    genres = [] #genre list to hold the genre 
    artists = []
    genre_count = {} # dictionary for each genre
    artist_count = {} # dictionary for artists 
    
    def __init__(self,name,artist,genre):
        self.name = name 
        self.artist = artist 
        self.genre = genre
        #refactor the class methods 
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
        
    @classmethod
    def add_song_to_count(cls,increment =1):
        cls.count += increment
    
    #define class method: 
    #adds genre to genre list 
    @classmethod
    def add_to_genres(cls,genre):
        cls.genres.append(genre)
    
    @classmethod
    def add_to_artists(cls,artist):
        cls.artists.append(artist)
        
    @classmethod
    def add_to_genre_count(cls,genre):
        # cls.genre_count.update({name:cls.count})
        if genre in cls.genre_count:
            cls.genre_count[genre] +=1
        else:
            cls.genre_count[genre]=1
            
    @classmethod
    def add_to_artist_count(cls,artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] +=1
        else: 
            cls.artist_count[artist] =1
        
    
    
# music = Song()
# print(Song.count)