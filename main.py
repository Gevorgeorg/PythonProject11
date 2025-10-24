from flask import Flask, request, render_template
import logging
from utils import (get_posts_all,
                   get_post_by_pk,
                   get_posts_by_user,
                   get_comments_by_post_id,
                   search_for_posts)

ALLOWED_EXTENSIONS: set = {'png', 'jpg', 'jpeg'}

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)


@app.route('/', methods=["GET"])
def main_tape() -> str:
    """Выводит главную страницу со всеми постами"""

    posts: list = get_posts_all()
    return render_template('index.html', posts=posts)


@app.route('/post/<int:post_id>/', methods=["GET"])
def post_page(post_id: int) -> str:
    """Выводит конкретный пост"""

    post: dict = get_post_by_pk(post_id)
    comments = get_comments_by_post_id(post_id)
    return render_template('post.html', post=post, comments=comments)


@app.route('/search/', methods=["GET"])
def search_page():
    """Обработка поискового запроса"""

    search_query = request.args.get('s', '').strip()

    posts = search_for_posts(search_query)

    return render_template('search.html', search_query=search_query, posts=posts)


@app.route('/users/<username>', methods=["GET"])
def search_user(username):
    """Поиск по имени"""
    posts = get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts)


app.run(host='0.0.0.0', port=5000, debug=True)
