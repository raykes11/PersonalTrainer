from trainer.moduls.base import Base
from typing import List
from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, Float, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable

class ExerciseMachine_db(Base):
    __tablename__ = 'exercise_machine'
    id = Column(Integer,primary_key=True, index=True)
    title = Column(String)
    specification = Column(String)
    max_weight = Column(Integer)
    min_weight = Column(Integer)
    add_weight = Column(String)
    add_weight_item = Column(String)
    list_weight = Column(String)
    group_muscles = Column(String)
    user_create = Column(String,nullable=False)
    user_list = relationship('UserMachine_db', back_populates='machine_db')
    __table_args__ = (
        UniqueConstraint('title', name='uq_machine_nickname'),  # Уникальность для поля `nickname`
    )

# print(CreateTable(ExerciseMachine_db.__table__), )

