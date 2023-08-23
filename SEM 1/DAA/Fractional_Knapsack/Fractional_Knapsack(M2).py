def fractional_knapsack(items, capacity):
    # Calculate the value-to-weight ratio for each item
    for item in items:
        item['ratio'] = item['value'] / item['weight']

    # Sort items by their value-to-weight ratio in descending order
    items.sort(key=lambda x: x['ratio'], reverse=True)

    total_value = 0
    knapsack = []

    for item in items:
        if capacity >= item['weight']:
            knapsack.append(item)
            total_value += item['value']
            capacity -= item['weight']
        else:
            fraction = capacity / item['weight']
            total_value += fraction * item['value']
            knapsack.append({'name': item['name'], 'weight': fraction * item['weight'], 'value': fraction * item['value']})
            break

    return knapsack, total_value

# Example items: {'name': 'item_name', 'weight': weight, 'value': value}
items = [{'name': 'item1', 'weight': 10, 'value': 60},
         {'name': 'item2', 'weight': 20, 'value': 100},
         {'name': 'item3', 'weight': 30, 'value': 120}]

capacity = 50
knapsack, total_value = fractional_knapsack(items, capacity)

print("Items in the knapsack:")
for item in knapsack:
    print(f"Item: {item['name']}, Weight: {item['weight']}, Value: {item['value']}")

print(f"Total value: {total_value}")
