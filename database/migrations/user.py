from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from database.app import db
from database.migrations import promo_code_users

STATUS_REGISTER = 'register'
STATUS_ACTIVE = 'active'
STATUS_BANNED = 'banned'

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    name = Column(String)
    lastname = Column(String)
    username = Column(String)
    email = Column(String)
    level = Column(Integer)
    balance_trx = Column(Float)
    balance_usd = Column(Float)
    role = Column(String)
    status = Column(String)
    language = Column(String)
    patron = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    first_referer_id = Column(Integer)
    second_referer_id = Column(Integer)
    third_referer_id = Column(Integer)

    bonus = relationship('Bonus', back_populates='user', uselist=False)
    achievements = relationship('Achievement', back_populates='user', uselist=False)
    lottery = relationship('Lottery', back_populates='user', uselist=False)
    wallet = relationship('Wallet', back_populates='user')
    payments = relationship('Payment', back_populates='user')
    say_hi = relationship('Say_hi', back_populates='user')
    promo_codes = relationship('PromoCode', secondary=promo_code_users, back_populates='users')
