#this is the file where we move the different data files into our train, test and validate
#put all the imports up here

filename = input("Input file address like './voltage/sig1_voltage.out'    : ") 
myoutputfile = input("Which file to output to? example = 'horizTrainVoltage.out'   : ")
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
        outputfile.write(line)
    counter += 1
outputfile.close()
