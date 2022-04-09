
with open('Input.txt') as f:
    Lines = f.readlines()
    
lineArray = list()

def notPrimeChecker(bd):
    array = []
    for a in bd:
        flg = False
        if a==1:
            flg=True
        for b in range(2,a):
            if a%b == 0:
                flg = True
                break
        if flg == True:
            array.append(a) 
    return array

print("Input:","\n")

checkflag=True
flag=True

for line in Lines:
    print(line)
    if (line != line.lstrip()) and checkflag==True:
        flag=False

    checkflag=False
    line = line.lstrip()
    line = line.strip("\n")
    line=[int(s) for s in line.split() if s.isdigit()]
    lineArray.append(line)

print()
print("+++++++++++++++++++++++","\n")

total = []
for lines in lineArray:
    if len(lines)==1:
        total.append(max(lines))
        prevIndex=0
    else:
        sortedList=sorted(lines,reverse=True)
        while True:
            if len(sortedList)==0:
                break
            if (lines.index(max(sortedList))-prevIndex == 1):#+1 or 0 index
                if ((max(sortedList) in notPrimeChecker(lines))):#primeNot
                    total.append(max(sortedList))
                    prevIndex=lines.index(max(sortedList))
                    break
                else:
                    sortedList.remove(max(sortedList))
                    pass

            elif (lines.index(max(sortedList))-prevIndex == 0):

                if ((max(sortedList) in notPrimeChecker(lines))):
                    total.append(max(sortedList))
                    prevIndex=lines.index(max(sortedList))
                    break
                else:
                    sortedList.remove(max(sortedList))
                    pass

            elif ((lines.index(max(sortedList))-prevIndex == -1) and (flag==True)):

                if ((max(sortedList) in notPrimeChecker(lines))):
                    total.append(max(sortedList))
                    prevIndex=lines.index(max(sortedList))
                    break
                else:
                    sortedList.remove(max(sortedList))
                    pass

            else:
                sortedList.remove(max(sortedList))
                pass

print("Path:",total,"\n")

print("Output Result:",sum(total),"\n")
