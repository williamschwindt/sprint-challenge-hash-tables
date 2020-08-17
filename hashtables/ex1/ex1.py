weight_dict = {}

def get_indices_of_item_weights(weights, length, limit):
    global weight_dict
    result = []

    for i in range(0, len(weights) - 1):
        weight_dict[weights[i]] = i

    for weight in weight_dict:
        if limit - weight in weight_dict:
            result = [weight_dict[weight], weight_dict[limit - weight]]

    weight_dict = {}

    if len(result) < 2:
        return None
    elif result[0] > result[1]:
        return (result[0], result[1])
    else: 
        return (result[1], result[0])
    

print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))
