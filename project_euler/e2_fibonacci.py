#Fibonacci, you need to sum all pares number of the sequence (4M)

def fibonacci(number):
     a = 1
     b = 2
     c = 0
     list_fibo = [1,2]
     while c < number:
          c = a + b
          a = b
          b = c
          list_fibo.append(c)
     return list_fibo

def pares(list_numbers):
     list_pares = []
     for number in list_numbers:
          if (number % 2) == 0:
               list_pares.append(number)
     return list_pares

def total_sum(list_pares):
     sum_total = 0
     for number in list_pares:
          sum_total += number
     return sum_total


print(total_sum(pares(fibonacci(4_000_000))))