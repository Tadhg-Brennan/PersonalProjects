stringinput = input("Please enter all names with a ', ' between them: \n")
array = stringinput.split(", ")
class meeting:
    def __init__(self, person1, person2):
        self.person1 = person1
        self.person2 = person2

count = 0
originalarray = []
for i in array:
    originalarray.append(array[count])
    count+=1

if count%2 == 1:
    count+=1
    originalarray.append("nobody")
    array.append("nobody")
    
firstround = []

for i in range(0,count,2):
    firstround.append(meeting(array[i], array[i+1]))

thisround = firstround
check = False

loopcount = 0
while check == False:

    loopcount+=1

    print("ROUND: " + str(loopcount))

    for i in range(int(count/2)):
        print(thisround[i].person1 + " meets " + thisround[i].person2)
    print()

    oldstoredpiece = array[1]
    array[1] = array[2]
    for i in range(2,count):
        if i%2 == 0:
            if i == count-2:
                array[i] = array[count-1]
            else:
                array[i] = array[i+2]
        elif i%2 == 1:
            newstoredpiece = array[i]
            array[i] = oldstoredpiece
            oldstoredpiece = newstoredpiece

    thisround = []
    for i in range(0,count,2):
        thisround.append(meeting(array[i], array[i+1]))

    check = True
    for i in range(count):
        if array[i] != originalarray[i]:
            check = False


    
