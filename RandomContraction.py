import random
import csv


def contract(data, verticeslist):
    final = []
    if len(verticeslist) == 2:
        # print("hello")
        final.append(verticeslist[0])
        final.append(verticeslist[1])

        return final, len(data[final[0]])

    index = random.choice(verticeslist)
    # print(index,"hello1")
    index2 = random.choice(data[index])
    # print(index2, "hello2")

    for each in data :
        if each == 0:
            continue
        for i in range(0, len(each)):
            if each[i] == index2:
                each[i] = index

    for num in data[index2]:
        if num != index and num != index2:
            data[index].append(num)

    data[index]= [x for x in data[index] if x != index]
    data[index]= [x for x in data[index] if x != index2]
    # print(sorted(data[index]))
    # print(len(data[index]))
    # print(index2)
    # if index2 in verticeslist:
    verticeslist.remove(index2)
    # print(verticeslist)
    final, length = contract(data, verticeslist)

    return final, length







if __name__ == '__main__':
    mincut = 10 ** 5
    iterar = 1
    while iterar != 10**5 :
        with open("RandomContraction.txt", 'r') as file :
            reader = csv.reader(file, delimiter='\t')
            adjacencylist = []
            for i in range(0,201):
                adjacencylist.append(0)

            for line in reader:
                index = int(line[0])
                adjacencylist[index]=[]
                for num in line:
                    if str(num) == '':
                        break
                    if int(num) != index:
                        adjacencylist[index].append(int(num))
            verticeslist = []
            for i in range (1,201):
                verticeslist.append(i)

            points = contract(adjacencylist, verticeslist)
            if points[1] < mincut :
                mincut = points[1]
                print("huh!", points[1], mincut)
            else :
                print("checked once for iteration {}".format(iterar))
        iterar += 1
    print("Final mincut is {} : found at iteration {}".format(mincut, iterar))
