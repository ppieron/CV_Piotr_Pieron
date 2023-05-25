from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

password = input('Please input your MySQL Password: ')

"""Selecting the target location of a table is essential for the program to work properly"""

dbname = input('Please input the target DB name/location: ')
if dbname == '':
    dbname = 'vacancies'  # for own testing purposes

engine = create_engine(f"mysql+pymysql://root:{password}@localhost:3306/{dbname}")
Session = sessionmaker(bind=engine)
session = Session()
