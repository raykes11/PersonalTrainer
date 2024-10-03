from trainer.moduls.base import Base
from sqlalchemy import Column, Integer, String, Date, Text, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship, Mapped,mapped_column
from sqlalchemy.schema import CreateTable


class Trainer_db(Base):
    __tablename__ = 'trainers'
    id = Column(Integer,primary_key=True, index=True)
    nickname = Column(String,primary_key=True)
    first_name = Column(String)
    about_self = Column(Text)
    user_trainer = relationship('User_db', back_populates='connect_trainer')
    __table_args__ = (
        UniqueConstraint('nickname', name='uq_trainer_nickname'),  # Уникальность для поля `nickname`
    )

# print(CreateTable(Trainer_db.__table__), )