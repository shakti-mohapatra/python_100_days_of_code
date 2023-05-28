import random

names_string=input("Give me the names separated by comma : \n")
names = names_string.split(",")
num = len(names)
random_num = random.randint(0, num-1)   #cuz index starts from 0, not 1
person_who_pays = names[random_num]

print(f"{person_who_pays} is going to pay today!!")