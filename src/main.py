from secret_santa import SecretSantaAssigner, Employee
from file_manager import FileManager
import csv
import os 

if __name__ == "__main__":
    input_file_path = 'data/employees.csv'
    output_file_path = 'data/secret_santa_assignments.csv'
    
    employees = FileManager.read_csv(input_file_path)

    secretSanta = SecretSantaAssigner()
    SantaPairing = secretSanta.assign_secret_children(employees)

    FileManager.write_to_csv(output_file_path,SantaPairing)
    