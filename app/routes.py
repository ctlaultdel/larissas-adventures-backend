from flask import Blueprint, jsonify, request, abort, make_response

from app.models.Adventure import Adventure
from app.models.Blog import Blog
from app.models.Content import Content

adventures_bp = Blueprint("adventures", __name__, url_prefix="/adventures")
blog_bp = Blueprint("blog", __name__, url_prefix="/blogs")

# adventures
@adventures_bp.route("", methods=["GET"])
def get_adventures():
    name_query = request.args.get("name")

    if name_query:
        adventures = Adventure.query.filter_by(alt_name=name_query)
    else:
        adventures = Adventure.query.order_by(Adventure.id).all()

    response = []
    for adv in adventures:
        response.append(adv.to_dict())
    return jsonify(response)

# blog and contents
@blog_bp.route("", methods=["GET"])
def get_blog_content():
    name_query = request.args.get("name")
    
    if name_query:
        blogs = Blog.query.filter_by(alt_name=name_query)
    else:
        blogs = Blog.query.order_by(Blog.id).all()

    response = []
    for i, blog in enumerate(blogs):
        response.append(blog.to_dict())
        for content in blog.contents:
            response[i]['content'].append(content.to_dict())
    return jsonify(response)