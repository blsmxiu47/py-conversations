import logging

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
from dagster import op

# from models import ConversationsBase
import settings

Base = declarative_base()

class ConversationsBase(Base):
    __tablename__ = 'googlenews'

    id = Column(Integer)
    title = Column('title', String(128), primary_key=True)
    source = Column('source', String(128), primary_key=True)
    time = Column('time', DateTime(timezone=False), primary_key=True)
    content_url = Column('content_url', String(256))
    content = Column('content', Text())


CONNECTION_STRING = '{drivername}://{user}:{password}@{host}:{port}/{database}'.format(
    drivername='postgresql',
    user=settings.DB_USER,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database=settings.DB_NAME,
)


@op
def ingest_data(results):
    engine = create_engine(CONNECTION_STRING)

    Session = sessionmaker(bind=engine)

    session = Session()

    success = False

    for item in results:
        cb = ConversationsBase()
        cb.title = item['title']
        cb.source = item['source']
        cb.time = item['time']
        cb.content_url = item['content_url']
        cb.content = item['content']

        try:
            session.add(cb)
            session.commit()
        except IntegrityError as e:
            logging.warning(e)
        except:
            session.rollback()
            raise
        finally:
            # TODO: some indicator of success
            session.close()
    
    success = True

    return success
