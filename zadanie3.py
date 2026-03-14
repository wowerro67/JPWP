prices = [10, 20, 30.5, 15]
total = 0

for price in prices:
    total += price
    
print(total) # 75.5

from functools import reduce

prices = [10, 20, 30.5, 15]

# Użycie reduce i wyrażenia lambda do "zredukowania" listy do jednej wartości
total = reduce(lambda current_sum, price: current_sum + price, prices, 0)

print(total) # 75.5