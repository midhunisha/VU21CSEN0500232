import os
import json
from datetime import datetime

# File to store patient data
DATA_FILE = 'patient_data.json'

# Load existing patient data from file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save patient data to file
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Add a new report or update an existing one
def add_patient_report(patient_id, report):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_entry = {"date": date, "report": report}

    if patient_id in patient_data:
        patient_data[patient_id].append(report_entry)
        print(f"Added new report for Patient ID: {patient_id}")
    else:
        patient_data[patient_id] = [report_entry]
        print(f"Created new record and added report for Patient ID: {patient_id}")

# Retrieve reports for a specific patient
def get_patient_report(patient_id):
    if patient_id in patient_data:
        print(f"\nReports for Patient ID: {patient_id}")
        for idx, entry in enumerate(patient_data[patient_id], 1):
            print(f"Report {idx} - Date: {entry['date']}\n{entry['report']}\n")
    else:
        print(f"No reports found for Patient ID: {patient_id}")

# Retrieve all patient IDs
def get_all_patient_ids():
    if patient_data:
        print("\nAll Patient IDs:")
        for patient_id in patient_data.keys():
            print(f"- {patient_id}")
    else:
        print("No patient records found.")

# Delete a specific report for a patient
def delete_report(patient_id, report_index):
    if patient_id in patient_data:
        if 0 < report_index <= len(patient_data[patient_id]):
            deleted_report = patient_data[patient_id].pop(report_index - 1)
            print(f"Deleted report from {deleted_report['date']}.")
            if not patient_data[patient_id]:  # If no reports left, delete patient ID
                del patient_data[patient_id]
                print(f"Deleted Patient ID: {patient_id} as there are no more reports.")
        else:
            print("Invalid report number.")
    else:
        print(f"No reports found for Patient ID: {patient_id}")

# Delete an entire patient record
def delete_patient(patient_id):
    if patient_id in patient_data:
        del patient_data[patient_id]
        print(f"Deleted all reports for Patient ID: {patient_id}")
    else:
        print(f"No reports found for Patient ID: {patient_id}")

# Main menu interface
def main_menu():
    print("\nAutomatic Health Monitoring System")
    print("1. Add/Update Patient Report")
    print("2. Retrieve Patient Report")
    print("3. Retrieve All Patient IDs")
    print("4. Delete a Specific Report")
    print("5. Delete Entire Patient Record")
    print("6. Exit")
    return input("Enter your choice (1/2/3/4/5/6): ")

def main():
    global patient_data
    patient_data = load_data()

    while True:
        choice = main_menu()

        if choice == '1':
            patient_id = input("Enter Patient ID: ").strip()
            if not patient_id:
                print("Patient ID cannot be empty.")
                continue
            report = input("Enter Diagnosis Report: ").strip()
            if not report:
                print("Report cannot be empty.")
                continue
            add_patient_report(patient_id, report)

        elif choice == '2':
            patient_id = input("Enter Patient ID: ").strip()
            if not patient_id:
                print("Patient ID cannot be empty.")
                continue
            get_patient_report(patient_id)

        elif choice == '3':
            get_all_patient_ids()

        elif choice == '4':
            patient_id = input("Enter Patient ID: ").strip()
            if not patient_id:
                print("Patient ID cannot be empty.")
                continue
            get_patient_report(patient_id)
            report_index = int(input("Enter the report number to delete: ").strip())
            delete_report(patient_id, report_index)

        elif choice == '5':
            patient_id = input("Enter Patient ID to delete: ").strip()
            if not patient_id:
                print("Patient ID cannot be empty.")
                continue
            delete_patient(patient_id)

        elif choice == '6':
            print("Saving data and exiting the system.")
            save_data(patient_data)
            break

        else:
            print("Invalid choice, please enter 1, 2, 3, 4, 5, or 6.")

if __name__ == "__main__":
    main()