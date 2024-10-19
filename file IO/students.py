import csv

# read a csv file

students = []
with open("file IO/students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)

 
for student in sorted(students, key=lambda student: student['name']):
    print(f"{student['name']} is in {student['home']}")


# write in csv files

name = input("what's your name? ")
home = input("where is your home? ")

with open ("file IO/students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home":home})