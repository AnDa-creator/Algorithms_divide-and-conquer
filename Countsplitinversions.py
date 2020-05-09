import time
import random
def sort_and_countinv(data):
    data1 = data[:len(data) // 2]
    data2 = data[len(data) // 2:]
    final1 = data1
    final2 = data2
    if len(data1) > 2:
        final1, count1 = sort_and_countinv(data1)
    else:
        if len(data1) < 2:
            count1 = 0
        elif data1[1] < data1[0]:
            final1 = data1[::-1]
            count1 = 1
        else:
            count1 = 0
    if len(data2) > 2:
        final2, count2 = sort_and_countinv(data2)
    else:
        if len(data2) < 2:
            count2 = 0
        elif data2[1] < data2[0]:
            final2 = data2[::-1]
            count2 = 1
        else:
            count2 = 0
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
            splitinv = splitinv + len(data1) - i

    return final, splitinv


# def divide(data):
#     data1 = data[:len(data) // 2]
#     data2 = data[len(data) // 2:]
#     final1 = data1
#     final2 = data2
#
#     if len(data1) > 2:
#         final1 = divide(data1)
#     else:
#         if len(data1) < 2:
#             pass
#         elif data1[1] < data1[0]:
#             final1 = data1[::-1]
#         else:
#             pass
#
#     if len(data2) > 2:
#         final2 = divide(data2)
#     else:
#
#         if len(data2) < 2:
#             final2 = data2
#         elif data2[1] < data2[0]:
#             final2 = data2[::-1]
#         else:
#             final2 = data2
#
#     merged = merge(final1, final2)
#     return merged

#
# def merge(data1, data2):
#     i = 0
#     j = 0
#     final = []
#     for k in range(0, len(data2) * 2 + 1):
#         if i > len(data1) - 1 and j > len(data2) - 1:
#             break
#         elif i > len(data1) - 1:
#             final.append(data2[j])
#             j += 1
#             # print("Hi, 1st case")
#         elif j > len(data2) - 1:
#             final.append(data1[i])
#             i += 1
#             # print("Hi, 2nd case")
#         elif data1[i] < data2[j]:
#             final.append(data1[i])
#             i += 1
#             # print("hello")
#         else:
#             final.append(data2[j])
#             j += 1
#
#     return final

def getInvCount(arr, n):

    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] > arr[j]):
                inv_count += 1

    return inv_count


if __name__ == '__main__':
    myList=[]
    for i in range(0, 10 ** 5):
        random_num = random.randint(0, 10 ** 10)
        if random_num not in myList:
            myList.append(random_num)

    # with open("ToSort.txt", 'r') as numbers:
    #     for number in numbers:
    #         myList.append(int(number))
    print(len(myList))
    print(myList)
    timestart= time.time()
    sorted_array, count = sort_and_countinv(myList)
    print(sorted_array, count,time.time()-timestart, sep='\n')
    # new=getInvCount(myList, len(myList))
    # print(sorted_array, count, sep='\n')
    # print(new)
    # print(new==count)
