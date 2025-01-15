class HealthProfessional:
    daily_capacity = 7.5

    def __init__(self, assignment_number=None, surname=None, firstname=None, employer_id=None):
        if not assignment_number:
            raise ValueError("Assignment Number cannot be empty")           # raise an error if assignment_number is missing
        self.assignment_number = assignment_number
        self.surname = surname
        self.firstname = firstname
        self.employer_id = employer_id

    def __str__(self):
        return f'{self.firstname} {self.surname} works at {self.employer_id} for {self.daily_capacity} hours per day'


class Nurse(HealthProfessional):
    def __init__(self, assignment_number=None ,surname=None ,firstname=None ,
                 employer_id=None ,department=None ,specialism=None ,band=None , role=None):
        self.department = department
        self.specialism = specialism
        self.band = band
        self.role = role
        super().__init__(assignment_number,surname,firstname,employer_id)

class Doctor(HealthProfessional):
    def __init__(self, assignment_number=None ,surname=None ,firstname=None ,
                 employer_id=None , department=None , specialism=None , seniority=None ):
        self.department = department
        self.specialism = specialism
        self.seniority = seniority
        super().__init__(assignment_number,surname,firstname,employer_id)