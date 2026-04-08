# Creat Student list
# crude = Create, Update, Read, Deleted
# Studentnamlist = id, name, sc1, sc2, sc3, sc4, sc5, total, everage, grade

import csv
import os

file_path ="Fixed/score_input.csv"

colum_header = ["id", "Name", "Score1", "Score2", "Score3", "Score4", "Score5", "Total", "Average", "Grade"]

studentlist = []

try:
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["id"] = int(row["id"])
            row["sc1"] = float(row["sc1"])
            row["sc2"] = float(row["sc2"])
            row["sc3"] = float(row["sc3"])
            row["sc4"] = float(row["sc4"])
            row["sc5"] = float(row["sc5"])
            row["total"] = float(row["total"])
            row["average"] = float(row["average"])
            # load data from file and send it into studentlist
            studentlist.append(row)
            
    print("the data reader and convert successfully..... \n\n")
        
except FileNotFoundError:
    print("we can not find the file...")
    with open(file_path, "w", newline="") as file:
        writer = csv.DictWriter(file,fieldnames=colum_header)
        writer.writeheader()
        
    print("New file is created")
  

print("\n Welcome to my system..........\n")
sid = int(input("input student id: "))
name = str(input("student name : "))
sc1 = float(input("inputscore1: "))
sc2 = float(input("inputscore2: "))
sc3 = float(input("inputscore3: "))
sc4 = float(input("inputscore4: "))
sc5 = float(input("inputscore5: "))
total = sc1 + sc2 + sc3 + sc4 + sc5
average = total / 5
grade = "A" if average >= 80 else "B" if average >=50 else "F"

studentlist.append({"id": sid, "Name": name, "Score1": sc1, "Score2": sc2, "Score3": sc3, "Score4": sc4, "Score5": sc5, "Total": total, "Average": average, "Grade": grade })

with open(file_path, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=colum_header)
    writer.writeheader()
    writer.writerows(studentlist)
    
print("\nData Saved successfully....!\n")

# Header of table on list
print(f"{'ID':<5} | {'Name':<15} | {'sc1':>5} | {'sc2':>5} | {'sc3':>5} | {'sc4':>5} | {'sc5':>5} | {'total':>10} | {'average':>10}")
         
print("-" * 80)

# for details in colum_header:
for std in studentlist:
    print(f"{std['id']:<5} | {std["Name"]:<15} | {std["Score1"]:<5} | {std["Score2"]:>5} | {std["Score3"]:>5} | {std["Score4"]:>5} | {std["Score5"]:>5} | {std["Total"]:>10} | {float(std["Average"]):>10.2f}")

print("\n---------------------")

    



#     for row in writer :
#         

# print("\n")

# #write sample data from list to file

# with open(file_path, "w", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=colum_header)

#     writer.writeheader()
#     writer.writerows(studetlist)
#     print("file saved successfully.")

# try:
#     with open("score_input-20260323.txt","w", newline="") as file:
#         # colum_header = ["id", "name", "sc1", "sc2", "sc3", "sc4", "sc5","total", "average" ]

#         writer = csv.DictWriter(file,)
#         writer.writeheader()
#         writer.writerrows(load_data)

#         for row in writer :
#             row["id"] = int(row["id"])
#             row["sc1"] = float(row["sc1"])
#             row["sc2"] = float(row["sc2"])
#             row["sc3"] = float(row["sc3"])
#             row["sc4"] = float(row["sc4"])
#             row["sc5"] = float(row["sc5"])
#             row["total"] = float(row["total"])
#             row["average"] = float(row["average"])
        
#         print("the data reader and convert successfully..... \n\n")




# total = sc1 + sc2 + sc3 + sc4 + sc5

# average = total / 5

# print("======== Print Score =======\n")
# print(f"student id: {id}")
# print(f"student name: {name}")
# print(f"score1: {sc1}")
# print(f"score2: {sc2}")
# print(f"score3: {sc3}")
# print(f"score4: {sc4}")
# print(f"score5: {sc5}")

# print("==============================")
# print(f"total: {total}")
# print(f"Average: {average}")



# # f = open("score_input_20260323.txt")

# f = open("Test 20260323/Score_input_20260323", "w")
# f = open("test_20260323/score_input_20260323", "w")
#  {id = int(input("input student id: "))},
#     {name = str(input("student name : "))},
#     {sc1 = float(input("inputscore1: "))},
#     {sc2 = float(input("inputscore2: "))},
#     {sc3 = float(input("inputscore3: "))},
#     {sc4 = float(input("inputscore4: "))},
#     {sc5 = float(input("inputscore5: "))}