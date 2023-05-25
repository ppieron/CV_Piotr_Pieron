class Job:
    company_name = ''
    position = ''
    period = ''

    def about(self):
        return '-' * 34 + "\n" \
                          f'\33[34mCompany:\33[0m {self.company_name}' \
                          f'\n\33[34mPosition:\33[0m {self.position}' \
                          f'\n\33[34mPeriod of time:\33[0m {self.period}'


class Eurojobs(Job):
    company_name = 'EuroJobs'
    position = 'Founder and GM'
    period = '07.2019 - 03.2023'


class Glovo(Job):
    company_name = 'Glovo'
    position = 'Marketing Manager'
    period = '05.2020 - 05.2021'


class Bacardi(Job):
    company_name = 'Bacardi Martini'
    position = 'Regional Brand Manager'
    period = '07.2016 - 06.2018'


class Gz(Job):
    company_name = 'Grupa Żywiec'
    position = 'Junior Brand Manager'
    period = '05.2015 - 06.2016'


class Mondelez(Job):
    company_name = 'Mondelez'
    position = 'Junior Brand Manager'
    period = '04.2014 - 04.2015'


class Panasonic(Job):
    company_name = 'Panasonic'
    position = 'Junior Product Manager'
    period = '08.2012 - 03.2014'


class Pepsico(Job):
    company_name = 'PepsiCo'
    position = 'Assistant Brand Manager'
    period = '10.2011 - 8.2012'


class JobFactory:
    def create_job(self, type):
        target_job = type.capitalize()
        return globals()[target_job]()