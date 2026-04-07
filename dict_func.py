# Write your code here!
def employee_print(employee_info):
    name = employee_info.pop("Name", "N/A")
    salary = employee_info.pop("Salary", "N/A")
    role = employee_info.pop("Role", "N/A")
    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print(f"Role: {role}")
    if employee_info:
        for key, value in employee_info.items():
            print(f"{key}: {value}")
    else:
        print("No other info!")
    employee_info["Name"] = name
    employee_info["Salary"] = salary
    employee_info["Role"] = role