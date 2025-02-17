from typing import List,Optional
import csv
from secret_santa import Employee

class FileManager:
    'Read employee data from the CSV file'
    @staticmethod
    def read_csv(file_path: str) -> List[Employee]:
        employees = []
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                employee = Employee(row['Employee_Name'], row['Employee_EmailID'])
                employees.append(employee)
        return employees
        
    'Write final output to CSV File'
    @staticmethod
    def write_to_csv(output_file_path: str, assignments: List[dict]) -> None:
        with open(output_file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Employee_Name', 'Employee_EmailID', 'Secret_Child_Name', 'Secret_Child_EmailID'])
            writer.writeheader()
            for assignment in assignments:
                writer.writerow(assignment)
