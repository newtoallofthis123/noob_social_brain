from flask import Blueprint, Flask, request, jsonify
from dotenv import load_dotenv
import os

from web.db.connect import NoobSocialDB
from web.model.classify import classify_tags
load_dotenv()

app = Flask(__name__)

api = Blueprint('api', __name__, url_prefix='/v1/api')
db = NoobSocialDB(os.environ.get("DB_USER"), os.environ.get("DB_PASSWORD"))
assert(db.check_connection())

@api.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

@api.route('/tags', methods=['GET'])
def tags():
    tags = db.fetch_tags()
    return jsonify(tags)

@api.route('/give_tag', methods=['POST'])
def tag():
    if not request.is_json:
        return jsonify({'status': 'error', 'message': 'Request must be JSON'}), 400
    json = request.get_json()
    post_id = json['post_id'] 
    post = db.fetch_content_by_id(post_id)
    if post is None:
        return jsonify({'status': 'error', 'message': 'Post not found'}), 404
    tag_ids = db.get_tags_for_post(post_id)
    if tag_ids is not None:
        db_tags = db.fetch_tags()
        tags = []
        for tag_id in tag_ids:
            for db_tag in db_tags:
                if db_tag[0] == tag_id:
                    tags.append(db_tag)
        return jsonify({'status': 'ok', 'tags': tags})
    tags = classify_tags(post[1], db.fetch_tags())

    for tag in tags:
        db.add_tag(post[0], tag[0])

    return jsonify({'status': 'ok', 'tags': tags})


@api.route('/get_tags', methods=['GET'])
def get_tags():
    return jsonify(db.fetch_tags())

@api.route('/posts_of_tag', methods=['POST'])
def posts_of_tag():
    if not request.is_json:
        return jsonify({'status': 'error', 'message': 'Request must be JSON'}), 400
    json = request.get_json()
    tag_id = json['tag_id']
    posts = db.fetch_posts_of_tag(tag_id)
    return jsonify(posts)

app.register_blueprint(api)
