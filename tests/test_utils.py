from utils import (get_posts_by_user,
                   get_posts_all,
                   get_comments_by_post_id,
                   search_for_posts,
                   get_post_by_pk)


def test_get_posts_all():
    """Тест загрузки всех постов"""
    posts = get_posts_all()
    assert isinstance(posts, list), "Должен возвращаться список"
    assert len(posts) > 0, "Список постов не должен быть пустым"

def test_get_posts_by_user_existing():
    """Тест для существующего пользователя"""
    user_post = get_posts_by_user("leo")
    assert len(user_post) == 2, "У пользователя leo должно быть 2 поста"
    assert user_post[0]['pk'] == 1, "Первый пост должен иметь pk=1"

def test_get_posts_by_user_non_existing():
    """Тест для несуществующего пользователя"""
    try:
        get_posts_by_user("Шрек")
        assert False, "Должна была возникнуть ошибка ValueError"
    except ValueError:
        assert True

def test_get_comments_by_post_id_existing():
    """Тест для существующего коммента"""

    comments = get_comments_by_post_id(1)
    assert len(comments) == 4, "У первого поста должно быть 4 коммента"
    assert comments[0]['pk'] == 1, "Первый коммент должен иметь pk=1"

def test_get_comments_by_post_non_existing():
    """Тест для несуществующего коммента"""
    try:
        get_comments_by_post_id(69)
        assert False, "Должна была возникнуть ошибка ValueError"
    except ValueError:
        assert True

def test_search_for_posts():
    """Тест загрузки постов по слову"""

    posts = search_for_posts("пирог")
    assert isinstance(posts, list), "Должен возвращаться список"
    assert posts[0].get("poster_name") == "leo", "Первый пост писал leo"


def test_get_post_by_pk():
    """Тест загрузки поста по номеру"""
    post = get_post_by_pk(1)
    assert isinstance(post, dict), "Должен возвращаться словарь"
    assert post.get('poster_name') == "leo", "Первый пост писал leo"


