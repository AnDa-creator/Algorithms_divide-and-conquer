import random
import time


def divide(data):
    data1 = data[:len(data) // 2]
    data2 = data[len(data) // 2:]
    final1 = data1
    final2 = data2

    if len(data1) > 2:
        final1 = divide(data1)
    else:
        if len(data1) < 2:
            pass
        elif data1[1] < data1[0]:
            final1 = data1[::-1]
        else:
            pass

    if len(data2) > 2:
        final2 = divide(data2)
    else:

        if len(data2) < 2:
            final2 = data2
        elif data2[1] < data2[0]:
            final2 = data2[::-1]
        else:
            final2 = data2

    merged = merge(final1, final2)
    return merged


def merge(data1, data2):
    i = 0
    j = 0
    final = []
    for k in range(0, len(data2) * 2 + 1):
        if i > len(data1) - 1 and j > len(data2) - 1:
            break
        elif i > len(data1) - 1:
            final.append(data2[j])
            j += 1
            # print("Hi, 1st case")
        elif j > len(data2) - 1:
            final.append(data1[i])
            i += 1
            # print("Hi, 2nd case")
        elif data1[i] < data2[j]:
            final.append(data1[i])
            i += 1
            # print("hello")
        else:
            final.append(data2[j])
            j += 1

    return final


def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def sort_and_countinv(data):
    data1 = data[:len(data) // 2]
    data2 = data[len(data) // 2:]
    final1 = data1
    final2 = data2
    if len(data1) > 2:
        final1, count1 = sort_and_countinv(data1)
    else:
        if len(data1) < 2:
            final1, count1 = data1, 0
        elif data1[1] < data1[0]:
            final1 = data1[::-1]
            count1 = 1
        else:
            final1, count1 = data1, 0

        if len(data2) > 2:
            final2, count2 = sort_and_countinv(data2)
        else:
            if len(data2) < 2:
                final2, count2 = data2, 0
            elif data2[1] < data2[0]:
                final2 = data2[::-1]
                count2 = 1
            else:
                final2, count2 = data2, 0

    Merged, count3 = merge_and_countsplitinv(final1, final2)
    return Merged, count1 + count2 + count3


def merge_and_countsplitinv(data1, data2):
    i = 0
    j = 0
    splitinv = 0
    final = []
    for k in range(0, len(data2) * 2 + 1):
        if i > len(data1) - 1 and j > len(data2) - 1:
            break
        elif i > len(data1) - 1:
            final.append(data2[j])
            j += 1
            # print("Hi, 1st case")
        elif j > len(data2) - 1:
            final.append(data1[i])
            i += 1
            # print("Hi, 2nd case")
        elif data1[i] < data2[j]:
            final.append(data1[i])
            i += 1
            # print("hello")
        else:
            final.append(data2[j])
            j += 1
            splitinv = splitinv + len(data1) - i + 1

    return final, splitinv


if __name__ == '__main__':
    my_list = []
    for i in range(0, 10 ** 5):
        my_list.append(random.randint(0, 10 ** 5))
    print(my_list)
    time1 = time.time()
    Merged_list = divide(my_list)
    time2 = time.time()


    print("Time taken for merged sort is {}".format(time2-time1))
    print("merged sort is {}".format(Merged_list))
    time4 = time.time()
    merged_list = insertionSort(my_list)
    time3 = time.time()
    print("Time taken for insertion sort is {}".format(time3-time4))


    print("Insertion sort is {}".format(merged_list))
    print(merged_list==Merged_list)
