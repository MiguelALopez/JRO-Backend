# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app.app import db



# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


# Define a User model
class Repository(Base):
    __tablename__ = 'repository'

    ori_url = db.Column(db.String(1000),  nullable=False)
    fork_url = db.Column(db.String(1000),  nullable=False)
    state = db.Column(db.String(128),  nullable=False, unique=True)
    owner = db.Column(db.String(128), db.ForeignKey('user.orcid'), nullable=False)

    def __init__(self, ori_url, fork_url, state, owner):

        self.ori_url = ori_url
        self.fork_url = fork_url
        self.state = state
        self.owner = owner

    def __repr__(self):
        return '<Repo %r>' % self.ori_url
