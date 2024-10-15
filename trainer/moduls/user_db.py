from sqlalchemy import Column, Integer, String, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship

from trainer.moduls.base import Base
from trainer.moduls.user_machine import UserMachine_db
from trainer.moduls.trainers_db import Trainer_db


class User_db(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True, index=True)
    nickname = Column(String,primary_key=True)
    first_name = Column(String)
    age = Column(String)
    height = Column(String)
    weight = Column(String)
    history_weight = Column(String)
    history_calories = Column(String)
    average_calories = Column(String)
    date_last_training = Column(String)
    history_date = Column(String)
    machine = Column(String)
    history_machine = Column(String)
    sleep_time = Column(String)
    # list_sleep_time = Column(String)
    set_exercise = Column(String)
    last_set_exercise = Column(String)
    password = Column(String)
    status = Column(String)
    trainer = Column(String,ForeignKey("trainers.nickname"),nullable=True)
    connect_trainer = relationship('Trainer_db', back_populates='user_trainer')
    list_machine =  relationship('UserMachine_db', back_populates='user_db')
    __table_args__ = (
        UniqueConstraint('nickname', name='uq_user_nickname'),  # Уникальность для поля `nickname`
    )


    def __str__(self):
        return self.nickname



