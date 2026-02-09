from Person import Person
from Staff import Staff
from Patient import Patient
from Department import Department
from Hospital import Hospital


if __name__ == "__main__":
    # Create a hospital
    hospital = Hospital("City Hospital", "123 Main St")

    # Create a department
    cardiology = Department("Cardiology")
    hospital.add_department(cardiology)

    # Create a patient
    patient1 = Patient("Alice", 30, "No known allergies")
    cardiology.add_patient(patient1)

    # Create a staff member
    doctor1 = Staff("Dr. Smith", 45, "Cardiologist")
    cardiology.add_staff(doctor1)

    # View patient and staff records
    print(patient1.view_record())
    print(doctor1.view_info())