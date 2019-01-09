import webbrowser
class Trailers():
    def __init__(self,title,story_line,poster,movie_trailer):
        self.movie_name=title
        self.description=story_line
        self.image=poster
        self.trailer=movie_trailer
    def play_trailer(self):
        webbrowser.open(self.trailer)
