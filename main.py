def remove_duplicates(lst):
    unique_list = []
    for element in lst:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list


my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_list = remove_duplicates(my_list)
print(f"Список без повторяющихся чисел: {unique_list}")
def find_average(lst):
    average = sum(lst) / len(lst)
    return average
average_result = find_average(my_list)
print(f"Среднее значение списка: {average_result}")
