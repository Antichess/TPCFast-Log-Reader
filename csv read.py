import csv

rawdata = []
with open("name.csv","r") as file:
#put the log file name in the line 4, above this
    reader = csv.reader(file)
    
    for row in reader:
        rawdata.append(row)

userstats = []
for i in range(len(rawdata)-1):
    found = False
    append = []
    for x in userstats:
        if x[0] == rawdata[i+1][1]:
            if x[1] == (int(float(rawdata[i+1][2])) - int(float(rawdata[i][2]))):                
                found = True
                break
    if found is False:
        append = (rawdata[i+1][1],(int(float(rawdata[i+1][2])) - int(float(rawdata[i][2]))),1)
        userstats.append(append)
    else: #if found is true
        for j in range(len(userstats)):
            if (userstats[j][0] == rawdata[i+1][1]):
                if (userstats[j][1] == (int(float(rawdata[i+1][2])) - int(float(rawdata[i][2])))):
                     temp = list(userstats[j])
                     temp[2] = temp[2] + 1
                     userstats[j] = temp

print("Username|Speed|Counts")
print("---|---|---")
                        
unique_names = []
timemax = 0
for x in userstats:

    if x[0] not in unique_names:
        unique_names.append(x[0])


for y in unique_names:
    times = []
    for x in userstats:
        if y == x[0]:
            times.append(x[1])
        times.sort()


    for t in times:
        for x in userstats:
            if y == x[0] and t == x[1] and x[2] != 0:
                print(str(x[0]) + " | " + str(t) + "s | " + str(x[2]))
                break
            
            
        
        

