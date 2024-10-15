from sqlalchemy import Column, Integer, String, Text, UniqueConstraint
from sqlalchemy.orm import relationship

from trainer.moduls.base import Base
from trainer.moduls.user_db import User_db


class Trainer_db(Base):
    __tablename__ = 'trainers'
    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String, primary_key=True)
    first_name = Column(String)
    about_self = Column(Text)
    user_trainer = relationship('User_db', back_populates='connect_trainer')
    __table_args__ = (
        UniqueConstraint('nickname', name='uq_trainer_nickname'),  # Уникальность для поля `nickname`
    )
