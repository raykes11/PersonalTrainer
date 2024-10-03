import asyncio
from asyncio import WindowsSelectorEventLoopPolicy

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine

from trainer.bot.api import POSTGRES

engine = create_async_engine(f"{POSTGRES}", echo=False,
                             pool_size=5)
asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())

metadate_obj = MetaData()
