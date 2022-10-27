dictionary = {}

with open("monsters_simple.txt", 'r') as fi:
    for line in fi:
        line=line.strip('\n')
        parts = line.rsplit(",")
        dictionary[parts[0]] = parts[1]
key=input ("what monster do you want: ").capitalize()

print(dictionary[key])