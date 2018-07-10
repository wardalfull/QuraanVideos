import webbrowser
class Myvideo():
    def  __init__(self,video_title,video_storyline,poster_image,video_youtube,video_release_date):
        self.title=video_title
        self.storyline=video_storyline
        self.poster_image_url=poster_image
        self.video_youtube_url=video_youtube
        self.release_date = video_release_date
    def show_video(self):
        webbrowser.open(self.video_youtube_url)



        

    
    
