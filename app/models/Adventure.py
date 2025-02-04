import base64
from app import db

class Adventure(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    img = db.Column(db.LargeBinary, nullable=False)
    public = db.Column(db.Boolean, default='true')
    blog = db.relationship("Blog", back_populates="blog")

    def to_dict(self):
        """
        Returns Adventure JSON serializable data
        """
        return {
            "name": self.name,
            "img": self.convert_base64(),
            "blog_id": self.blog.id,
            "public": self.public,
        }
    
    def convert_base64(self):
        """
        Encodes binary img data into base64 string
        """

        return base64.b64encode(self.img).decode('utf-8')