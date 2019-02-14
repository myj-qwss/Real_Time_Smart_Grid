#this is the file where we move the different data files into our train, test and validate
#put all the imports up here

filename = input("Input file address like './voltage/sig1_voltage.out'    : ") 
myoutputfile = input("Which file to output to? example = 'trainVoltage.out'   : ")
pmunumber =    input("Which PMU?                     ")
# the file is just a normal csv.
# ../IData/voltage/sig1_voltage.out
# './example/test.txt'

partialfile = open(filename, 'r')

lines = partialfile.readlines()

partialfile.close()

count = len(lines)

mymin = 0
mymax = count*.8
counter = 0
outputfile = open(myoutputfile, 'a')
for line in lines:
    if (mymin <= counter <= mymax):
        outputfile.write()
        outputfile.write(line[46:])
    counter += 1
outputfile.close()

#Old code

#print(len(lines))

#normal = 0
#temporal = 0
#constraint = 0
#total = 0

#print(lines[0][-2])
#for line in lines:
 #   total +=1
  #  char = line[-2]
   # if (char == "T"):
    #    temporal +=1
    #elif  (char == "C"):
     #   constraint += 1
    #else:
     #   normal +=1

#totalcheck = normal + temporal + constraint

#if (totalcheck != total):
 #   print("There is an error with the for loop, total not matching sum of three categories.")
 #   print([totalcheck, total])

#print("normal number is: {} \ntemporal number is: {}\nconstraint number is: {}\n".format(normal, temporal, constraint))