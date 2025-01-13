class Employee:
    def __init__(self, employee_id, employee_name, *args):
        self.id = employee_id
        self.name = employee_name

    def get_info(self):
        return self.__dict__


class Manager(Employee):
    def __init__(self, employee_id, employee_name, department, *args):
        super().__init__(employee_id, employee_name, *args)
        self.department = department

    def manage_project(self):
        return f"{self.name} managment"


class Technician(Employee):
    def __init__(self, employee_id, employee_name, specialization, *args):
        super().__init__(employee_id, employee_name, *args)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"{self.name} maintenance"


class TechManager(Manager, Technician):
    def __init__(self, employee_id, employee_name, department, specialization, employee_list, *args):
        super().__init__(employee_id, employee_name, department, specialization, *args)
        self.employee_list = employee_list

    def add_employee(self, employee):
        self.employee_list.append(employee)

    def get_team_info(self):
        return [employee.get_info() for employee in self.employee_list]


if __name__ == '__main__':
    tech_manager = TechManager(0, "name techM", "name department", "name spec", [])

    print(tech_manager.perform_maintenance())
    print(tech_manager.get_info())
    print(tech_manager.manage_project())

    tech_manager.add_employee(
        Employee(employee_id=1, employee_name="name employee")
    )
    tech_manager.add_employee(
        Manager(employee_id=2, employee_name="name manager", department="name department")
    )
    print(tech_manager.get_team_info())
