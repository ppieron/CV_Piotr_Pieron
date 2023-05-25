import random

from sqlalchemy.exc import IntegrityError

from DB_Create import Base, Applicant
from session import session
from faker import Faker


def create_applicants(count=10):
    fake = Faker()
    return [
        Applicant(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            age=random.randint(25, 40),
            email=fake.email(),
            phone_number=random.randint(770_000_000, 999_999_999)
        )
        for _ in range(count)
    ]


def execute(count):
    Base.metadata.create_all()

    Applicants = create_applicants(count=count)
    for Applicant in Applicants:
        try:
            session.add(Applicant)
            session.commit()
        except IntegrityError:
            session.rollback()


def exceute_single_applicant(first_name, last_name, age, email, phone_number, comment):
    applicant = Applicant(
        first_name= first_name,
        last_name=last_name,
        age=age,
        email=email,
        phone_number=phone_number,
        comment=comment
    )
    session.add(applicant)
