import base64
from app import db

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String, nullable = True)
    figure = db.Column(db.LargeBinary, nullable=True)
    caption = db.Column(db.String, nullable=True)
    blog_id = db.Column(db.Integer, db.ForeignKey("blog.id"), nullable=False)
    blog = db.relationship("Blog", back_populates="contents")

    def to_dict(self):
        """
        Returns dict of content data including binary img data into base64 str
        """
        return {
            "text": self.text,
            "figure": self.convert_base64(),
            "caption": self.caption,
        }
    
    def convert_base64(self):
        """
        Encodes binary img data into base64 string
        """

        return base64.b64encode(self.figure).decode('utf-8')
