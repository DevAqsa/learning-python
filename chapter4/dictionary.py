# dictionary in  python -- store data in key:pair value 
# dictionary are mutable and unordered and dont allow duplicate keys

# info = {
#     "name" : "aqsa",
#     "cgpa" : 3.1,
#     "learning" : "python",
#     "age" : 22,
#     "is_adult": True,
#     "subject":["pyhton", "javascript", "php"],
#     "topics": ("dictionary", "sets")
# }

# info["name"] = "aqsa mumtaz" #overwrite if we add the same key
# info["surname"] = "mumtaz"
# print(type(info))
# print(info)


# empty dictionary
# null_dict ={}

# print(null_dict)

# nesting in dictionary

# student ={
#     "name" : "aqsa",
#     "subjects" :{
#         "phy" : 89,
#         "math" : 90,
#         "chem": 80
#     }
# }

# print(student)
# print(student["subjects"])
# print(student["subjects"]["chem"])

# methods in dict

student ={
    "name" : "aqsa",
    "subjects" :{
        "phy" : 89,
        "math" : 90,
        "chem": 80
    }
}

# print(student.keys()) #only return the outer layer keys not the nested keys

# if we want the keys then we use the typecasting

# print(list(student.keys()))
# print(len(list(student.keys())))
# print(len(student))

# print(list(student.values()))

# print(student.items()) -- return all key pair values are tuples
# print(list(student.items()))

# print(student["name"]) # get the error
# print(student.get("name")) #get the none value not error so that this method working well

student.update({
    "city": "multan"
})

print(student)


