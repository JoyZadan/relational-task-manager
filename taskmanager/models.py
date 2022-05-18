"""
imports db from the taskmanager package to define the database
"""
from taskmanager import db


# creates separate tables which will be represented by
# class-based models using SQLAlchemy's ORM
# first table will be for various categories
# it will use the declarative base SQLAlchemy's model
class Category(db.Model):
    """
    schema for the Category model
    """
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship("Task", backref="category",
                            cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


# second table will be for each task created
# this will also use the default db.Model
class Task(db.Model):
    """
    schema for the Task model
    """
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(
                   "category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )
