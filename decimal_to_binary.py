# lists of power 2 numbers
list1 = [2 ** i for i in range(30)]
list2 = [2 ** i for i in range(30)]
list1.sort(reverse=True)
list2.sort(reverse=True)
indexs = []


# get a decimal number from user
decimal = int(input('Please enter a decimal number:  '))
num = decimal

# find decimal number position between power 2 numbers and replace it with 1 and subtract main number
for i in list1:
    if num >= i:
        indexs.append(list1.index(i))
        list2[list2.index(i)] = 1
        num = num - i
        continue

# replace numbers that doesnt change with 0
for i in range(len(list2)):
    if i not in indexs:
        list2[i] = 0

# convert number to string to display
bin = list2[list2.index(1)::]
bin = map(str, bin)
res = ''.join(bin)
print(f'The binary form of {decimal} is:\n>>> {res}')
