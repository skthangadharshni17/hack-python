def get_divisors(n):
   return [x for x in range(1, n+1) if n % x == 0]


def divisors_of_list(numbers):
   return {num: get_divisors(num) for num in numbers}


numbers = [10, 15, 21]
divisors = divisors_of_list(numbers)
print(divisors)