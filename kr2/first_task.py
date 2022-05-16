import requests

url_users = 'https://jsonplaceholder.typicode.com/users'
url_posts = 'https://jsonplaceholder.typicode.com/posts'
url_comments = 'https://jsonplaceholder.typicode.com/comments'

users = requests.get(url_users).json()
posts = requests.get(url_posts).json()
comments = requests.get(url_comments).json()


def get_all_email(username: str) -> set:
    """Возвращает email комментаторов ко всем постам username"""
    email = set()
    for data in users:
        if data['username'] == username:
            user_id = data['id']
            for post in posts:
                if post['userId'] == user_id:
                    post_id = post['id']
                    for comment in comments:
                        if comment['postId'] == post_id:
                            email.add(comment['email'])
    return email

if __name__ == "__main__":
    print(get_all_email('Bret'))
    print(get_all_email('Antonette'))
    print(get_all_email('Samantha'))
    print(get_all_email('Karianne'))