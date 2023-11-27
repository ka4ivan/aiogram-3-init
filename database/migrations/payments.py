from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship

from database.app import db


class Wallet(db.Model):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    add_trx = Column(Float)
    del_trx = Column(Float)
    add_usd = Column(Float)
    address = Column(String)
    status = Column(String)
    created_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='payments')
