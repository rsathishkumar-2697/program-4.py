multipiles = [1,2,3,4,5,6,7,8,9]
num_list = [1,2,8,9,12,46,76,82,15,20,30]
result_dict = {}
for div in multipiles:
    count = 0
    for num in num_list:
        if num % div == 0:
            count += 1
            result_dict[str(div)] = count
print(result_dict)