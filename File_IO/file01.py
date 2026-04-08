
# f = open("File_IO/Test01.txt", "w")

products = ["apple", "banana", "orange", "mango"]

# write something into file with mode "w"
with open("File_IO/Test01.txt", "w") as file:
    for x in products:
        # file.write(f"{x} : Hello, How are you today ?\n")
        file.write(f"{x} \n")
    

with open("File_IO/Test01.txt", "a") as file:
    file.write("coconat\n")
    
with open("File_IO/Test01.txt", "r") as file:
    text_file = file.read()
    # text_file = file.readline()
    print("============ Read From file =============")
    print(text_file)