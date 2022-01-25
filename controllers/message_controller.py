from flask_login import current_user


def create_message(title, body, receiver_id):
    from models import Message
    user = current_user
    message = Message(title=title, body=body, sender_id=user_id)
    print()
