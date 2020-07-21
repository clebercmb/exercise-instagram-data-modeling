import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), primary_key=True)

class Follower(Base):
    __tablename__ = 'Follower'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    #id = Column(Integer, primary_key=True)

    user_from_id = Column(Integer, ForeignKey('User.id'), primary_key=True)
    

    user_to_id = Column(Integer, ForeignKey('User.id'), primary_key=True)

    b = relationship(User)
    a = relationship(User)
   


class Post(Base):
    __tablename__ = 'Post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('User.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

class Comments(Base):
    __tablename__ = 'Comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))

    post_id =  Column(Integer, ForeignKey('Post.id'))
    post = relationship(Post)

    author_id = Column(Integer, ForeignKey('User.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

class Media(Base):
    __tablename__ = 'Media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)

    type = Column(Integer)

    url = Column(String(250))


    post_id = Column(Integer, ForeignKey('Post.id'))
    post = relationship(Post)

    def to_dict(self):
        return {}



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')