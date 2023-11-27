from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from database.app import db


class Wallet(db.Model):
    __tablename__ = 'achievements'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    daily_bonus = Column(Integer, default='0')
    c_daily_bonus = Column(Integer, default='0')
    week_bonus = Column(Integer, default='0')
    c_week_bonus = Column(Integer, default='0')
    pay_trx = Column(Integer, default='0')
    c_pay_trx = Column(Integer, default='0')
    pay_trx_th = Column(Integer, default='0')
    c_pay_trx_th = Column(Integer, default='0')
    game_dice = Column(Integer, default='0')
    c_game_dice = Column(Integer, default='0')
    game_mine = Column(Integer, default='0')
    c_game_mine = Column(Integer, default='0')
    game_fifty = Column(Integer, default='0')
    c_game_fifty = Column(Integer, default='0')
    game_case = Column(Integer, default='0')
    c_game_case = Column(Integer, default='0')
    game_slot = Column(Integer, default='0')
    c_game_slot = Column(Integer, default='0')
    game_num = Column(Integer, default='0')
    c_game_num = Column(Integer, default='0')
    game_num_win_hun = Column(Integer, default='0')
    c_game_num_win_hun = Column(Integer, default='0')
    win_lot = Column(Integer, default='0')
    c_win_lot = Column(Integer, default='0')
    c_f_ref = Column(Integer, default='0')
    c_s_ref = Column(Integer, default='0')
    c_a_ref = Column(Integer, default='0')

    user = relationship('User', back_populates='achievements')
