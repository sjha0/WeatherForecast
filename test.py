Fruits=["Apple","Banana","Cherry","Mango","Orange"]
print("Fruits list",Fruits)
print("First fruit in the list",Fruits[0])
print("Last fruit in the list",Fruits[-1])
print("First two fruits in the list",Fruits[:2])
print("Last two fruits in the list",Fruits[-2:])
Fruits[1]="Blueberry"
print("Fruits list after changing second fruit",Fruits)
Fruits.append("Pineapple")
print("Fruits list after adding Pineapple",Fruits)
Fruits.insert(2,"Grapes")
print("Fruits list after adding Grapes",Fruits)
Fruits.remove("Pineapple")
print("Fruits list after removing Pineapple",Fruits)
Fruits.remove("Grapes")
print("Fruits list after removing Grapes",Fruits)
del Fruits[1]
print("Fruits list after deleting second fruit",Fruits)
for fruit in Fruits:
    print(fruit)



    numbers=[1,2,3,4,5]
    print("Length of the list",len(numbers))