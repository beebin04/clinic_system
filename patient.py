from .patient_record import PatientRecord
class Patient():


    def __init__(self, phn=None, n=None, b=None, p=None, e=None, a=None):
        self.phn = phn
        self.name = n
        self.birth_date = b
        self.phone = p
        self.email = e
        self.address = a
        self.patient_record = PatientRecord()
    def __repr__(self):
        return "Patient(%d, %s, %s, %s, %s, %s)" % (self.phn, self.name, self.birth_date, self.phone, self.email, self.address)
    def __eq__(self, other):
        if other == None:
            return False
        if self.phn != other.phn:
            return False
        return True