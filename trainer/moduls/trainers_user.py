from sqlalchemy import Column, Integer, ForeignKey

from trainer.moduls.base import Base


class TrainersUser_db(Base):
    __tablename__ = 'trainers_user'
    id = Column(Integer, primary_key=True, index=True)
    trainer = Column(ForeignKey("trainers.nickname"), primary_key=True)
    user = Column(ForeignKey("users.nickname"), primary_key=True)
