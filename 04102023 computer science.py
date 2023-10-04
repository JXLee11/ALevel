import random
rannum = ["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
rannum = random.sample(rannum, len(rannum))
print(rannum)
def insertionSort(array):
    for n in range(1, len(array)):
        temp = array[n]
        count = n - 1
        while count >= 0 and temp < array[count]:
            array[count + 1] = array[count]
            count = count - 1

        array[count + 1] = temp

insertionSort(rannum)
print(rannum)

