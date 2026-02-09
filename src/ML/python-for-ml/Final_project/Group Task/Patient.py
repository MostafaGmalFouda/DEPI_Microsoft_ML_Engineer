from Person import Person
class Patient(Person):
    """Class for hospital patients, inheriting from Person.
     :name: patient's name
     :type name: str
     :age: patient's age
     :type age: int
     :medical_record: patient's medical record
     :type medical_record: str

    """
    def __init__(self, name:str, age: int, medical_record:str):
        """
        Initialize a Patient.
        :name: patient's name
        :age: patient's age
        :medical_record: patient's medical record
        
        """
        super().__init__(name, age)
        self.medical_record = medical_record

    def view_record(self)-> str:
        """View patient record.
        :return: patient's medical record
        :rtype: str
        """
        return f"Patient Record: {self.medical_record}"
