import base64
from app import db
from flask import request

class Adventure(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    img = db.Column(db.LargeBinary, nullable=False)
    url = db.Column(db.Text, nullable=True)
    public = db.Column(db.Boolean, default='true')

    def to_dict(self):
        """
        Returns Adventure JSON serializable data
        """
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "img": self.convert_base64(),
            "public": self.public,
        }
    
    def convert_base64(self):
        """
        Encodes binary img data into base64 string
        """

        return base64.b64encode(self.img).decode('utf-8')