from typing import List
import random


class Employee:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

class SecretSantaAssigner:
    
   def assign_secret_children(self, employees: List[dict]) -> List[dict]:
        secret_santa_pairings = list(dict())  # Initialize an empty list to store the secret santa pairings
        available_employees = list(set(employees))  # Remove any duplicate employees

        'We will first shuffle the list of employees we have'
        group1 = available_employees.copy()
        group2 = available_employees.copy()
        while len(group1) > 0:

            random.shuffle(group1)
            selected_employee = group1[0]  # Select an employee from group 1

            if selected_employee in group2:
                group2.remove(selected_employee)  # Remove the selected employee from group 2
                secret_child = random.choice(group2)  # Select a secret child from group 2
                group2.append(selected_employee)  # Add the selected employee back to group 2
            else:
                secret_child = random.choice(group2)  # Select a secret child from group 2
            group1.remove(selected_employee)  # Remove the selected employee from group 1
            group2.remove(secret_child)  # Remove the selected secret child from group 2
            
            secret_santa_pairings.append({
                "Employee_Name": selected_employee.name,
                "Employee_EmailID": selected_employee.email,
                "Secret_Child_Name": secret_child.name,
                "Secret_Child_EmailID": secret_child.email
            })
        
        return secret_santa_pairings
            

    