Array = [1,3,4,5,7,2]
Found = False
number = int(input('what number do you want?'))

for position in range(len(Array)):
  if Array[position] == number:
    print('Position:',position+1)
    found = True
else:
  print('that number is not in the array')
