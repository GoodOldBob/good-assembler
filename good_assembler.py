import sys
import re

infile = sys.argv[1]
outfile = sys.argv[2]
toRead = open(infile, 'r')
toWrite = open(outfile, 'w')

for line in toRead:
    broken = line.strip().split()
    if broken[0] == "halt":
	toWrite.write("000000000     //halt\n")
    if len(broken) < 2 or broken[0] == "//":
        continue
    if broken[0] != "bne" and broken[0] != "blt" and broken[0] != "bevn" \
        and broken[0] != "halt":
        param1 = int(re.sub("[^0-9]", "", broken[1]))
        param2 = int(re.sub("[^0-9]", "", broken[2]))
        if broken[0] == "cmp":
	    toWrite.write("0001")
        elif broken[0] == "add":
	    toWrite.write("0010")
        elif broken[0] == "sbab":
	    toWrite.write("0011")
        elif broken[0] == "and":
	    toWrite.write("0100")
        elif broken[0] == "ld":
	    toWrite.write("0101")
        elif broken[0] == "st":
	    toWrite.write("0110")
        elif broken[0] == "mov":
	    toWrite.write("0111")
        elif broken[0] == "addi":
	    toWrite.write("1000")
        elif broken[0] == "shift":
	    toWrite.write("1001")
        elif broken[0] == "cmpi":
	    toWrite.write("1010")
	toWrite.write(((bin(param1))[2:]).zfill(3))
	toWrite.write(((bin(param2))[2:]).zfill(2))
        toWrite.write("     //"+broken[0]+" "+broken[1]+" "+broken[2]+"\n")
    elif broken[0] != "halt":
        if broken[0] == "blt":
	    toWrite.write("1011")
        elif broken[0] == "bevn":
	    toWrite.write("1100")
        elif broken[0] == "bne":
	    toWrite.write("1101")
	toWrite.write((bin(int(broken[1])+8)[2:]).zfill(5))
        toWrite.write("     //"+broken[0]+" "+broken[1]+"\n")
toWrite.close()
toRead.close()
