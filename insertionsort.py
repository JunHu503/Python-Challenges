def insertionSort(list):
  for index in range(1, len(list)):
    currentvalue = list[index]
    position = index
    print(list)

    while position>0 and list[position-1] > currentvalue:
      list[position] = list[position-1]
      position = position - 1

    list[position] = currentvalue

list = [50, 49, 130, 1, 8, 26, 38, 100, 9]
insertionSort(list)
print(list)