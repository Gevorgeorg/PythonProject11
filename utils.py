from pathlib import Path
import json


def get_posts_all():
    """Загружает данные из файла и возвращает обычный list"""

    current_dir = Path(__file__).parent
    file_path = current_dir / 'data' / 'posts.json'


    print(f"Ищу файл по пути: {file_path}")
    print(f"Файл существует: {file_path.exists()}")

    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_user(user_name):
    """возвращает посты определенного пользователя"""

    right_posts: list = []
    user_exists = False

    for post in get_posts_all():
        if post.get('poster_name') == user_name:
            right_posts.append(post)
            user_exists = True
    if not user_exists:
        raise ValueError("Пользователь  не найден")
    return right_posts


def get_comments_by_post_id(post_id):
    """возвращает комментарии определенного поста"""

    current_dir = Path(__file__).parent
    file_path = current_dir / 'data' / 'comments.json'
    with open(file_path, 'r', encoding='utf-8') as file:
        comments = json.load(file)
    right_comments: list = []
    post_exists = False

    for comment in comments:
        if comment.get('post_id') == post_id:
            right_comments.append(comment)
            post_exists = True
    if not post_exists:
        raise ValueError("Пост  не найден")
    return right_comments




def search_for_posts(query):
    """возвращает список постов по ключевому слову"""

    right_posts: list = []
    for post in get_posts_all():
        if query.lower() in post.get('content').lower():
            right_posts.append(post)
    return right_posts

def get_post_by_pk(pk):
    """возвращает один пост по его идентификатору"""

    for post in get_posts_all():
        if pk is post.get('pk'):
            return post


