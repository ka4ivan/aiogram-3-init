from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database.app import db


class Wallet(db.Model):
    __tablename__ = 'lottery'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='lottery')
