class News:
    title: str = None
    subtitle: str = None
    image: str = None
    url: str = None
    date: str = None
    content: str = None

    def __init__(self, title: str, subtitle: str, image: str, url: str, date: str, content: str) -> None:
        self.title = title
        self.subtitle = subtitle
        self.image = image
        self.url = url
        self.date = date
        self.content = content
    