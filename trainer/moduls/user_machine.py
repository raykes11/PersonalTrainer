from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from trainer.moduls.base import Base
from trainer.moduls.exercise_machine_db import ExerciseMachine_db
from trainer.moduls.user_db import User_db

class UserMachine_db(Base):
    __tablename__ = 'user_machine'
    id = Column(Integer, primary_key=True, index=True)
    machine = Column(String, ForeignKey("exercise_machine.title"), primary_key=True)
    user = Column(String, ForeignKey("users.nickname"), primary_key=True)
    user_db = relationship('User_db', back_populates='list_machine')
    machine_db = relationship('ExerciseMachine_db', back_populates='user_list')

# print(CreateTable(UserMachine_db.__table__), )
