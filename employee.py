
class Employee(Human):

    def _init_(self, name, age, gender, employee_id, position, salary):
        super()._init_(name, age, gender)
        self.employee_id = employee_id
        self.position = position
        self.salary = salary


    def get_data(self):
        print(f"Employee ID: {self.employee_id}\nName: {self.name}\nPosition: {self.position}\nSalary: {self.salary}")

    def setdepartment(self,dep):
        self.department=dep
        print(f'{self.name} work in {self.department} department now')