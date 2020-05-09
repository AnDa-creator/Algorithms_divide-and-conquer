import random
from Sorter import divide,merge
import time


def choosepivot(data, l, r):
    # index = random.randint(l, r)
    # index = r
    # index = l
    third_num = (l + r)//2
    pivotlist = [data[l],data[r],data[third_num]]
    pivotlist.sort()
    if pivotlist[1] == data[l]:
        return l
    elif pivotlist[1] == data[r]:
        return r
    else :
        return third_num
    # return index


def partition(data, l, r):
    pivot = data[l]
    i = l + 1
    count = 0
    for j in range(i, r + 1):
        count += 1
        if data[j] < pivot:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp
            i += 1
    temp = pivot
    data[l] = data[i - 1]
    data[i - 1] = temp
    return i - 1,count


def quicksort(data, l, r):
    count = 0
    count1 = 0
    count2 = 0
    if l >= r:
        return 0
    i = choosepivot(data, l, r)
    temp = data[i]
    data[i] = data[l]
    data[l] = temp
    j,count = partition(data, l, r)
    count1 = quicksort(data, l, j - 1)
    count2 = quicksort(data, j + 1, r)
    return count1 + count2 + count


if __name__ == '__main__':
    myList = []
    # for i in range(0, 10 ** 5):
    #     random_num = random.randint(0, 10 ** 5)
    #     if random_num not in myList:
    #         myList.append(random_num)
    with open("Toquicksort.txt", 'r') as numbers:
        for number in numbers:
            myList.append(int(number))
    myList2 = myList
    print(myList)
    time1 = time.time()
    num_count = quicksort(myList, 0, len(myList) - 1)
    time2 = time.time()
    print(myList)
    print("number of counts is {}".format(num_count))
    print("Time taken by Quicksort is {}".format(time2-time1))
    time3 = time.time()
    Merged_list = divide(myList2)
    time4 = time.time()
    print("Time taken for merged sort is {}".format(time4-time3))
    print("merged sort is {}".format(Merged_list))
    print(Merged_list==myList)
