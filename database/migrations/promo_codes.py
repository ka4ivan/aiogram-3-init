from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.app import db
from database.migrations import promo_code_users


class Wallet(db.Model):
    __tablename__ = 'promo_codes'

    id = Column(Integer, primary_key=True)
    code = Column(String)
    used_count = Column(Integer)

    users = relationship('User', secondary=promo_code_users, back_populates='promo_codes')

