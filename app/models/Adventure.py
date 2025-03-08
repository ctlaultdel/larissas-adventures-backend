import base64
from app import db

class Adventure(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    img = db.Column(db.LargeBinary, nullable=False)
    alt_name = db.Column(db.String, default=''.join([char if char.isalpha() else '_' for char in name]))
    public = db.Column(db.Boolean, default='true')
    blog = db.relationship("Blog", back_populates="adventure")

    def to_dict(self):
        """
        Returns Adventure JSON serializable data
        """
        return {
            "id": self.id,
            "name": self.name,
            "url_name": self.url_name,
            "img": self.convert_base64(),
            "public": self.public,
        }
    
    def convert_base64(self):
        """
        Encodes binary img data into base64 string
        """

        return base64.b64encode(self.img).decode('utf-8')