from dataclasses import dataclass

@dataclass
class Contact:
    email: str

@dataclass
class Manager:
    contact: Contact

@dataclass
class Department:
    manager: Manager

@dataclass
class Employee:
    department: Department

class ApprovalReminder:
    """Only responsible for delivering an approval reminder."""
    def notify(self, employee, sender):
        sender.send(employee.department.manager.contact.email, "Please approve")
