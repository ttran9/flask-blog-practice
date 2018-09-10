from app import app, db, cli
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    # register certain items passed into the dictionary in the return.
    return {'db': db, 'User': User, 'Post': Post}
