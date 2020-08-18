def get_indices_of_item_weights(weights, length, limit):
    weight_dict = {}
    result = []

    for i in range(0, len(weights)):
        remander = limit - weights[i]
        if remander in weight_dict:
            x = weight_dict[remander]
            result = (i, x)
        else:
            weight_dict[weights[i]] = i

    print(weight_dict)

    if len(result) < 2:
        return None
    elif i > x:
        return (i, x)
    else: 
        return (x, i)
    

# print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))
print(get_indices_of_item_weights([4,4], 2, 8))
