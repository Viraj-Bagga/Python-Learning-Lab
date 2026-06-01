name = input("What is your name : ")
age = int(input("What is you age : "))
expected_salary = float(input("What is you r expected salary : "))

months_alive = age * 12
monthly_salary = expected_salary / 12

print(f"Your name is {name}, you have been alive for roughly {months_alive} months, and you expect to make {monthly_salary: .2f} a month.")
