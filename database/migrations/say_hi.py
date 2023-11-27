from sqlalchemy import Column, Integer, ForeignKey, DateTime, Text, String, Boolean
from sqlalchemy.orm import relationship

from database.app import db


class Wallet(db.Model):
    __tablename__ = 'say_hi'

    id = Column(Integer, primary_key=True)
    photo = Column(Boolean)
    audio = Column(Boolean)
    status = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    message = Column(Text)
    created_at = Column(DateTime)

    user = relationship('User', back_populates='say_hi')
