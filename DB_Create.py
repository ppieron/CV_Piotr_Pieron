from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from session import engine, session

Base = declarative_base(bind=engine)


class Applicant(Base):
    __tablename__ = "Junior Data Engineer - shortlist"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    age = Column(Integer)
    email = Column(String(50), unique=True, nullable=False)
    phone_number = Column(Integer, unique=True)
    comment = Column(String(100))


    def show_applicant_data(self):
        applicant = session.query(Applicant).get(6)
        print('=' * 34)
        print(f'\33[31mName:\33[0m {applicant.first_name}'
              f'\n\33[31mSurname:\33[0m {applicant.last_name}'
              f'\n\33[31mAge:\33[0m {applicant.age}'
              f'\n\33[31me-mail:\33[0m {applicant.email}'
              f'\n\33[31mphone number:\33[0m {applicant.phone_number}'
              )
        print('=' * 34)


Base.metadata.create_all(engine)