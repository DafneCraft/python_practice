#Multples of 3 or 5
#First condition the number must multiples 3 or 5
#We need to storage of number that are multiples 3 or 5 in a list
#After that we need to sum all those numbers and get total sum

list_numbers = []
total_sum = 0

for number in range(1,1000):

     if (number % 3) == 0 or (number % 5) == 0:
          list_numbers.append(number)

for number in list_numbers:
     total_sum += number

print(list_numbers)
print(total_sum)