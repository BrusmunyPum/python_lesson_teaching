
test_dic = {
    "id" : "e2023ff",
    "name" : "meme",
    "age" : 21    
}


# print(test_dic.keys())
# print(test_dic.values())

# for key, value in test_dic.items():
#     print(f"Key : {key} --> {value}")

test_dic.update({"status" : "Single"})

# test_dic.pop("age")

# test_dic.popitem()

# del test_dic["name"]

test_dic["name"] = "Halo"

# test2 = test_dic.copy()

# test2 = dict(test_dic)

# print(test_dic)
# print(test2)

# for i in range(1,10):
#     for j in range(1,i):
#         print(j)


child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

test3 = {
    "chile1" : child1,
    "chile2" : child2,
    "chile3" : child3
}

# print(test3["staff1"])

# for key, value in test3.items():
#     print(f"{key} : {value}")

# test3["chile1"].update({"name" : "Emili"})
# print(test3["chile1"])

print(test3["chile2"]["name"])