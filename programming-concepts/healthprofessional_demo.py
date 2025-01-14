import demo_packages.oop_healthprofessional as ohp

doctor_peppa = ohp.Doctor(1234567,"Pig","Peppa","A1A1A","Emergency","A&E","Consultant")

print(doctor_peppa)
print(doctor_peppa.assignment_number)
print(" ") # leave a gap in the terminal output

nurse_duggee = ohp.Nurse(7654321,"Dog","Duggee","Z9Z9Z","Paediatrics","Haematology","8a","Advanced Nurse Practitioner")

print(nurse_duggee)
print(nurse_duggee.specialism)
print(" ")

# try updating someone's daily_capacity to a number of hours other than 7.5