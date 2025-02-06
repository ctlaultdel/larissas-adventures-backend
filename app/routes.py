from flask import Blueprint, jsonify, request, abort, make_response

from app.models.Adventure import Adventure
from app.models.Blog import Blog
from app.models.Content import Content

adventures_bp = Blueprint("adventures", __name__, url_prefix="/adventures")
blog_bp = Blueprint("blog", __name__, url_prefix="/blogs")

# adventures
@adventures_bp.route("", methods=["GET"])
def get_adventures():
    adventures = Adventure.query.order_by(Adventure.id).all()
    response = []
    for adv in adventures:
        response.append(adv.to_dict())
    return jsonify(response)

# blog and contents
@blog_bp.route("", methods=["GET"])
def get_blog_content():
    id_ = int(request.headers.get('Adventure-ID'))
    blog = Blog.query.filter_by(adventure_id=id_).first()

    response = blog.to_dict()
    for content in blog.contents:
        response['content'].append(content.to_dict())
    return jsonify(response)