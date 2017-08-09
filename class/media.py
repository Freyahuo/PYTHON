import webbrowser

class Movie(): #类名要首字母大写
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self,movie_title,movie_storyline,postrer_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_imaage
        self.trailer_youtube = trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube)
