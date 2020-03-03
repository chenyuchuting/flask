from sqlalchemy import create_engine, Column, Integer, \
    Float, Boolean, DECIMAL, Enum, Date, DateTime, Time, \
    Text, String, func, and_, or_, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'test'
USERNAME = 'root'
PASSWORD = '123'

DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8'.\
    format(username=USERNAME,
        password=PASSWORD,
        host=HOSTNAME,
        port=PORT,
        db=DATABASE)

engine = create_engine(DB_URI)
# declarative_base()是一个工厂函数，它为声明性类定义构造基类
Base = declarative_base(engine)
# Session的主要目的是建立与数据库的会话，它维护你加载和关联的所有数据库对象。
# sessionmaker方法创建了一个Session工厂
session = sessionmaker(engine)()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(10), nullable=False)


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    # uid = Column(Integer, ForeignKey('user.id', ondelete="RESTRICT"))
    # uid = Column(Integer, ForeignKey('user.id', ondelete="NO ACTION"))
    # uid = Column(Integer, ForeignKey('user.id', ondelete="CASCADE"))
    uid = Column(Integer, ForeignKey('user.id', ondelete="SET NULL"))


Base.metadata.drop_all()
Base.metadata.create_all()

user = User(username="chain1")
session.add(user)
session.commit()

article = Article(title="python", content="big data", uid=1)
session.add(article)
session.commit()