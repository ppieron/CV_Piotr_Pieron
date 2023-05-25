class Skill:
    name = ''
    level = ''
    category = ''

    def about(self):
        return '-' * 34 + "\n" \
                          f'\33[35mSkill name:\33[0m {self.name}' \
                          f'\n\33[35mLevel:\33[0m {self.level}' \
                          f'\n\33[35mCategory:\33[0m {self.category}'


class English(Skill):
    name = 'English'
    level = 'Fluent'
    category = 'Foreign Languages'


class French(Skill):
    name = 'French'
    level = 'Basic'
    category = 'Foreign Languages'


class Python(Skill):
    name = 'Python'
    level = 'Intermediate'
    category = 'Computer'


class Sql(Skill):
    name = 'SQL'
    level = 'Intermediate'
    category = 'Computer'


class Msoffice(Skill):
    name = 'MSOffice'
    level = 'Advanced'
    category = 'Computer'


class Presentation(Skill):
    name = 'Presentation'
    level = 'Expert'
    category = 'Soft'


class Communication(Skill):
    name = 'Communication'
    level = 'Expert'
    category = 'Soft'


class SkillFactory:
    def create_skill(self, type):
        target_skill = type.capitalize()
        return globals()[target_skill]()