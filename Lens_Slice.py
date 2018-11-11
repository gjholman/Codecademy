toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices   = [2, 6, 1, 3, 2, 7, 2]

pizzas = list(zip(prices, toppings)) 
num_pizzas = len(toppings) 

print('We sell %s different kinds of pizzas' % num_pizzas)

pizzas.sort()

cheapest_pizza = pizzas[0] 
priciest_pizzas = pizzas[-1] 
three_cheapest = pizzas[:3]

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
