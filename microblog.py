from app import db, cli, create_app
from app.models import User, Post, Notification, Message, Task

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    # register certain items passed into the dictionary in the return.
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message,
            'Notification': Notification, 'Task': Task}
