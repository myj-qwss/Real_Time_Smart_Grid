#this is the file where we will analyze the different data files
#put all the imports up here

filename = input("Input file address like 'condensedCurrent.out' : ") 
# the file is just a normal csv.
# ../IData/voltage/sig1_voltage.out
# './example/test.txt'

analyzefile = open(filename, 'r')

lines = analyzefile.readlines()

#print(len(lines))

normal = 0
temporal = 0
constraint = 0
total = 0

#print(lines[0][-2])
for line in lines:
    total +=1
    char = line[-2]
    if (char == "T"):
        temporal +=1
    elif  (char == "C"):
        constraint += 1
    else:
        normal +=1

totalcheck = normal + temporal + constraint

if (totalcheck != total):
    print("There is an error with the for loop, total not matching sum of three categories.")
    print([totalcheck, total])

print("normal number is: {} \ntemporal number is: {}\nconstraint number is: {}\n".format(normal, temporal, constraint))

analyzefile.close()

outputfile = open('dataOverview.txt', 'a')
outputfile.write("\n\n----------------------------------------------------\nFile under analysis: "),
outputfile.write(filename)
outputfile.write("\nRaw Data: \ntotal: {}\nnormal: {}\nnormal %: {}\ntemporal: {}\ntemporal %: {}\nconstraint: {}\nconstraint %: {}".format(total, normal,normal/total, temporal, temporal/total, constraint, constraint/total))
outputfile.close()

