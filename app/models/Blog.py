from app import db
from datetime import datetime

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    publication_date = db.Column(db.DateTime, default=datetime.now())
    adventure = db.relationship("Adventure", back_populates="blog")
    adventure_id = db.Column(db.Integer, db.ForeignKey("adventure.id"))
    contents = db.relationship("Content", back_populates="blog")

    def to_dict(self):
        """
        Returns dict of blog data including contents
        """
        return {
            "title": self.title,
            "publication_date": self.publication_date.strftime("%B %d, %Y"),
            "content": [],
        }