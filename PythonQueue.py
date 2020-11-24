names = []


for i in range(10):
    acceptedName = input("Enter Name:")
    names.append(acceptedName)


for j in range(len(names)):
    print (names.pop(0))
