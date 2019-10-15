def knapsack(money, price, iPrice=0, stack=[]):
    if money < 0:
        return
    if money == 0:
        print("Found", stack)
        return
    for i in range(iPrice, len(price)):
        stack.append(price[i])
        knapsack(money - price[i], price, i + 1, stack)
        stack.pop()


knapsack(20, [20, 10, 5, 5, 3, 2, 20, 10])
