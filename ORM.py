from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

postgrees_password = "38gjgeuftd"  # input('YOUR POSTGREE PASSWORD, PLEASE')
engine = create_engine(f'postgresql+psycopg2://postgres:{postgrees_password}@localhost:5432/ORM', echo=True,
                       future=True)

DeclarativeBase = declarative_base()


class Publisher(DeclarativeBase):
    __tablename__ = 'publisher'

    id = Column(Integer, primary_key=True)
    name = Column('name', String)

    def __repr__(self):
        return "".format(self.code)


class Book(DeclarativeBase):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column('title', String)
    id_publisher = Column(Integer, ForeignKey("Publisher.id"))

    def __repr__(self):
        return "".format(self.code)


class Shop(DeclarativeBase):
    __tablename__ = 'shop'

    id = Column(Integer, primary_key=True)
    name = Column('name', String)

    def __repr__(self):
        return "".format(self.code)


class Stock(DeclarativeBase):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
    id_book = Column(Integer, ForeignKey("Book.id"))
    id_shop = Column(Integer, ForeignKey("Shop.id"))
    count = Column('count', Integer)

    def __repr__(self):
        return "".format(self.code)


class Sale(DeclarativeBase):
    __tablename__ = 'sale'

    id = Column(Integer, primary_key=True)
    price = Column('price', Integer)
    date_sale = Column('date_sale', DateTime)
    id_stock= Column(Integer, ForeignKey("Stock.id"))
    count = Column('count', Integer)

    def __repr__(self):
        return "".format(self.code)


DeclarativeBase.metadata.create_all(engine)

def main():
    Session = sessionmaker(bind=engine)
    session = Session()
    input_publisher = input("Input publisher or it's id: ")
    if input_publisher.isdigit():
        print(session.query(Publisher).filter(Publisher.id == int(input_publisher)))
    else:
        print(session.query(Publisher).filter(Publisher.name == int(input_publisher)))
    session.commit()


if __name__ == "__main__":
    main()
