from sqlalchemy.sql.ddl import CreateTable

from trainer.moduls.trainers_db import Trainer_db
from trainer.moduls.user_db import User_db


from trainer.moduls.base import Base
from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey,Float


class TrainersUser_db(Base):
    __tablename__ = 'trainers_user'
    id = Column(Integer,primary_key=True, index=True)
    trainer = Column(ForeignKey("trainers.nickname"), primary_key=True)
    user = Column(ForeignKey("users.nickname"), primary_key=True)


# print(CreateTable(TrainersUser_db.__table__), )
