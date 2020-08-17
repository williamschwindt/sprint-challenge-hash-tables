number_dict = {}

def has_negatives(a):
    global number_dict
    result = []

    for num in a:
        #if the opposite of the number alrady exists add to result
        if num - (num*2) in number_dict:
            result.append(abs(num))
        elif num not in number_dict:
            number_dict[num] = num
        elif num in number_dict:
            continue
        
    number_dict = {}
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
    print(has_negatives([1,2,3,-4]))
