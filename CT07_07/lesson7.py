

list1 = ["Apple", "Banana", "Cherry", "Durian"]
list2 = ["Cherry", "Durian", "Elderberry", "Figs"]
common = []

for fruit in list1:
    for fruit2 in list2:
        if fruit == fruit2:
            common.append(fruit)

print ("common")


