from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

## end configuration code

class Restaurant(Base) :
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)

class MenuItem(Base) :
    __tablename__ = 'menu_item'

    # mapper
    restaurant = relationship(Restaurant)

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    course = Column(String(20))
    description = Column(String(8))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))


class Employee(Base) :
    __tablename__ = 'employee'

    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)


class Address(Base) :
    __tablename__ = 'address'

    id = Column(Integer,primary_key = True)
    street = Column(String(80), nullable = False)
    zip = Column(String(5))

    # mapper
    employee = relationship(Employee)

    employee_id = Column(Integer, ForeignKey('employee.id'))
## end of file

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
