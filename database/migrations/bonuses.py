from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from database.app import db


class Wallet(db.Model):
    __tablename__ = 'bonuses'

    id = Column(Integer, primary_key=True)
    daily = Column(DateTime)
    weekly = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='bonuses')
