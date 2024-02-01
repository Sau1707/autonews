import yaml
import hashlib


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
    
    def __str__(self) -> str:
        return f"News(title={self.title}, subtitle={self.subtitle}, image={self.image}, url={self.url}, date={self.date}, content={self.content})"

    def get_metadata(self) -> dict:
        return {
            'title': self.title,
            'subtitle': self.subtitle,
            'image': self.image,
            'url': self.url,
            'date': self.date,
        }
    
    def id(self) -> str:
        """Return an unique identifier for the news, using hash of all the content"""
        return hashlib.sha256(str(self).encode('utf-8')).hexdigest()[:8]

    def save(self, path: str = None) -> None:
        """Save the news in a file, using the id as filename"""
        if path is None:
            path = f"news/{self.id()}.md"
        yaml_metadata = yaml.dump(self.get_metadata(), default_flow_style=False)
        markdown_body = self.content
        with open(path, 'w', encoding='utf-8') as f:
            complete_document = f"---\n{yaml_metadata}---\n{markdown_body}"
            f.write(complete_document)
