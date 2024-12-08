StudentDetails = [["" for j in range(2)] for i in range(30)] #ARRAY[0:29][0:1] OF STRING

def LaterBirthday(CurrentBirthday, ComparingBirthday):
    if int(ComparingBirthday[0:4]) > int(CurrentBirthday[0:4]):
        return True
    elif int(ComparingBirthday[0:4]) == int(CurrentBirthday[0:4]) and int(ComparingBirthday[5:7]) > int(CurrentBirthday[5:7]):
        return True
    elif int(ComparingBirthday[0:4]) == int(CurrentBirthday[0:4]) and int(ComparingBirthday[5:7]) == int(CurrentBirthday[5:7]) and int(ComparingBirthday[8:10]) > int(CurrentBirthday[8:10]):
        return True
    return False


def InsertionSort(array):
    for i in range(1, len(array)):
        position = i - 1
        currentvalue = array[i] #date
        date = array[i][1]
        if date == '':
            continue
        while position >= 0 and LaterBirthday(date, array[position][1]) == True: #move condition
            array[position+1] = array[position]
            position = position - 1
        array[position+1] = currentvalue
    return array


def BinarySearch(array, target):
    Found = False
    low = 0
    high = len(array)-1
    while array[high][0] == '':
        high = high - 1

    while low <= high:
        mid = (high+low)//2
        if array[mid][1] == target:
            print(array[mid][0])
            Found = True
            break
        elif LaterBirthday(target, array[mid][1]) == True:
            high = mid - 1
        else:
            low = mid + 1
    if Found == False:
        print("Student not found in array")


count = 0 #INTEGER
try:
    with open('Class.txt') as file:
        for line in file:
            line = line.strip()
            split = line.split(", ")
            name = split[0]
            birthday = split[1]
            if int(birthday[0:4]) >= 2007:
                StudentDetails[count][0] = name
                StudentDetails[count][1] = birthday
                count = count + 1
except OSError:
    print("Sorry, could not find the file")


InsertionSort(StudentDetails)
BinarySearch(StudentDetails, "2007-05-30")
BinarySearch(StudentDetails, "2007-12-09")
