from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from models import ConversationsBase


class ConversationsBase(DeclarativeBase):
    __tablename__ = "googlenews"

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

    cb = ConversationsBase()
    cb.title = results['title']
    cb.source = results['source']
    cb.time = results['time']
    cb.content_url = results['content_url']
    cb.content = results['content']

    success = False

    try:
        session.add(cb)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        # TODO: some indicator of success
        success = True
        session.close()

    return success
