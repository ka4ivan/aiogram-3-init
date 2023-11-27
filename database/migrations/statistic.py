from sqlalchemy import Column, Integer, Float

from database.app import db


class Wallet(db.Model):
    __tablename__ = 'statistics'

    id = Column(Integer, primary_key=True)
    all_accounts = Column(Integer)
    daily_accounts = Column(Integer)
    active_accounts = Column(Integer)
    paid_trx = Column(Float)
