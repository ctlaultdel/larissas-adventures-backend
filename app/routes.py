from flask import Blueprint, jsonify, request, abort, make_response

from app.models.Adventure import Adventure
from app.models.Blog import Blog
from app.models.Content import Content

adventures_bp = Blueprint("adventures", __name__, url_prefix="/adventures")
blog_bp = Blueprint("blog", __name__, url_prefix="/blogs")

# adventures
@adventures_bp.route("", methods=["GET"])
def get_adventures():
    adventures = Adventure.query.all()
    response = []
    for adv in adventures:
        response.append(adv.to_dict())
    return jsonify(response)

# blog and contents
@blog_bp.route("", methods=["POST"])
def get_blog_content():
    # access blog id from header
    # TODO: add id validation checker
    id_ = request.headers.get('Adventure-ID')
    blog = Blog.query.filter_by(adventure_id=id_).first()

    response = blog.to_dict()
    for content in blog.contents:
        response.content.append(content.to_dict)
    return jsonify(response)

# validate model ids
# def validate_id(model, id):
#     try:
#         id = int(id)
#     except:
#         abort(make_response({"message": "Invalid ID"}), 400)

#     record = model.query.get(id)
#     if not record:
#         abort(make_response({"message": "Active Record ID not found"}, 404))
#     return record