import json
from cryptography.fernet import Fernet
import os

class DataDumpTool:
    @staticmethod
    def logo():
        return """
  ╔═╗ ╔═╗ ╔═╗
  ║═╣ ╠╦╝ ╠═╣
  ╚═╝ ╩╚═ ╩ ╩
        """

    def __init__(self):
        self.data = []
        self.file_path = ""
        self.password = None

    def load_data_from_file(self):
        # ... (rest of the code)

    def save_data_to_file(self):
        # ... (rest of the code)

    def add_record(self):
        # ... (rest of the code)

    def display_records(self):
        # ... (rest of the code)

    def search_record(self):
        # ... (rest of the code)

    def set_file_path(self):
        # ... (rest of the code)

    def set_password(self):
        # ... (rest of the code)

    @staticmethod
    def get_valid_input(prompt, data_type, validation_func=None):
        # ... (rest of the code)

    @staticmethod
    def is_valid_email(email):
        # ... (rest of the code)

    def run(self):
        while True:
            print(self.logo())  # Display the logo
            print("Menu:")
            print("1. Add record")
            print("2. Display records")
            print("3. Search records")
            print("4. Save data to file")
            print("5. Load data from file")
            print("6. Set data file path")
            print("7. Set password for data encryption")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_record()
            elif choice == "2":
                self.display_records()
            elif choice == "3":
                self.search_record()
            elif choice == "4":
                self.save_data_to_file()
            elif choice == "5":
                self.load_data_from_file()
            elif choice == "6":
                self.set_file_path()
            elif choice == "7":
                self.set_password()
            elif choice == "8":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    tool = DataDumpTool()
    tool.run()
