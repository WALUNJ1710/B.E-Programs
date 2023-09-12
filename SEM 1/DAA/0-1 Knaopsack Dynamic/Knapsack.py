def knapsack(values,weights,capacity):
    n = len(values)
    dp = [[0]*(capacity +1) for _ in range(n+1)]

    for i in range(1,n+1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]]+values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    max_value = dp[n][capacity]
    selected_items = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i -1]
    return max_value, selected_items

#Example usage:
#values = [60,100,120]
#weights = [10,20,30]
#capacity = 50
#max_value, selected_items = knapsack(values,weights,capacity)
#print("Maximum value:", max_value)
#print("Selected items:", selected_items)
n = int(input("Enter number of items: "))
values = []
weights = []

for i in range(n):
    value = int(input(f"Enter the value of item {i+1}: "))
    weight = int(input(f"Enter weight of item {i+1}: "))
    values.append(value)
    weights.append(weight)
    
print(f"Provided values are {values} and provided weights are {weights}")

capacity = int(input("Enter the capacity of the knapsack : "))

max_value, selected_items = knapsack(values, weights, capacity)
print("Maximum value: ", max_value)
print("Selected items: ", selected_items)
