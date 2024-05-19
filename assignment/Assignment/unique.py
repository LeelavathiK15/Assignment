def unique_values(arr):
    unique_set = set(arr)
    unique_list = list(unique_set)
    return unique_list

arr = list(map(int, input().split()))
print(unique_values(arr))