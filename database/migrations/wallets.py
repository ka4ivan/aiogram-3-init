from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.app import db


class Wallet(db.Model):
    __tablename__ = 'wallets'

    id = Column(Integer, primary_key=True)
    address = Column(String)
    type = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='wallets')