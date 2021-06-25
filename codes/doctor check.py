file = open("doctor's info.txt")
data = file.readlines()
file.close()
list = []
for i in range(len(data)):
    
    list.append([])
    for j in data[i].split(" "):
        list[i].append(j)


search = input("Specilization searchin for :")
doctor_search = []
for i in list:
    for j in i:
        if j == search:
            doctor_search.append(i)
            
for i in range(len(doctor_search)):
    print("Name:",doctor_search[i][0])
    print("Mobile:",doctor_search[i][1])
    print("Specilization:",doctor_search[i][2])
    print("Time",doctor_search[i][3])
    print("Cost",doctor_search[i][4])
    
            

        
        

        

