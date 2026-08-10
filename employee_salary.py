class Employee:
    def __init__(self, name, salary):
        self.name= name
        self.salary= salary

    def showdetail(self):
        print(f"name of the employee is {self.name} and salary is {self.salary}")

employees = []

n = int(input("Enter total number of employees: "))

for i in range(n):
    print(f"\n--- Enter details for Employee {i + 1} ---")
    name = input("Enter name: ")
    salary = float(input("Enter salary: "))

    emp = Employee(name, salary)
    employees.append(emp)

out= input("Do You want to see records of employees? (yes/no): ")
if out.lower() == "yes":
    print("\n=== All Employee Records ===")
    for emp in employees:
        emp.showdetail()
else:
    print("thanks")
