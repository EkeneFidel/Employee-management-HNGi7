import random
import string

class Employee:

  
   def get_employee_details():
      employees = []
      while True:
         ans = input("Add new employee? y/n ")
         if ans == 'y':
            name =  str.split(input("Enter your First name and Last name: "))
            while len(name) > 2 :
               name = str.split(input("Enter only your first and last names: "))
            firstname = name[0]
            lastname = name[1]
            email = str(input("Enter your email: "))

            passw = (Employee.password_generator( Employee, firstname,lastname))

            print("Suggested password: " + passw)

            reply = input ("Do you want to change password? y/n ")
            if reply == 'y':
               passw = input ("Input Password: ")
               while len(passw) < 7:
                  passw = input ("Input Password Equal Or Greater Than 7: ")
                  print("Password Confirmed")
                  message = ".....Your details.....\nFirstname: {} \nLastname: {} \nEmail address: {}"
                  print(message.format(firstname, lastname, email))

            elif reply == "n":
               print("Password Confirmed")
               message = ".....Your details.....\nFirstname: {} \nLastname: {} \nEmail address: {}"
               print(message.format(firstname, lastname, email))
                        

            id = 0
            if not employees:
               id = 1
               emp = {"firstname" : firstname, "lastname" : lastname, "email" : email, "password" : passw}
               employee = [f"{id}", emp]
               employees.append(employee)
            else:
               id = len(employees) + 1
               emp = {"firstname" : firstname, "lastname" : lastname, "email" : email, "password" : passw}
               employee = [f"{id}", emp]
               employees.append(employee)


         elif ans == 'n':
            if not employees:
               print("No employee has been added yet")
            else:
               print(".......EMPLOYEE DETAILS......")

               for i in employees:
                  print(i[0] + " " + i[1]["firstname"] + " " + i[1]["lastname"] + " " + i[1]["email"])
            exit()

      
      return employee
      
      

   def add_employee(self):
      ans = input("Add new employee? y/n ")

   def password_generator(self, firstname, lastname):
      length = 5
      a  = "".join(random.choice( string.ascii_lowercase) for i in range (length))
      password = firstname[0:2] + lastname[-2:] +  a
      return password

Employee.get_employee_details()
     


