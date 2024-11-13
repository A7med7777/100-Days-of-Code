class Post:
    def __init__(self, post):
        self.id = post["id"]
        self.body = post["body"]
        self.title = post["title"]
        self.subtitle = post["subtitle"]
