my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

# Your code here
def max_integer(numbers):
    first_element = numbers[0]
    for number in numbers:
        if number > first_element:
            first_element = number
    return first_element 

print(max_integer(my_list))