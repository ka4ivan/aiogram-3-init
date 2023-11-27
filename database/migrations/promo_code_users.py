from sqlalchemy import Column, Integer, ForeignKey

from database.app import db


class Wallet(db.Model):
    __tablename__ = 'promo_code_users'

    id = Column(Integer, primary_key=True)

    Column('promo_code_id', Integer, ForeignKey('promo_codes.id')),
    Column('user_id', Integer, ForeignKey('users.id'))
