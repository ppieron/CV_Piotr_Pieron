import Jobs
import Skills
from DB_Fill import execute, exceute_single_applicant
from DB_Create import Applicant
from session import session


def main():
    execute(5)
    exceute_single_applicant('Piotr', 'Pieron', 34, 'piotrek.pieron@gmail.com', 662112614, "That's our guy!")
    execute(4)
    print('>' * 8 + ' Curriculum Vitae ' + '<' * 8)
    session.query(Applicant)
    Applicant.show_applicant_data(Applicant)
    print('Work Experience:')
    job_factory = Jobs.JobFactory()
    jobs = ['EuroJobs', 'Glovo', 'Bacardi', 'GZ', 'Mondelez', 'Panasonic', 'PepsiCo']
    for job in jobs:
        print(job_factory.create_job(job).about())
    print('-' * 34 + '\nSkills:')
    skill_factory = Skills.SkillFactory()
    skills = ['English', 'French', 'Python', 'SQL', 'MSOffice', 'Presentation', 'Communication']
    for skill in skills:
        print(skill_factory.create_skill(skill).about())


if __name__ == "__main__":
    main()