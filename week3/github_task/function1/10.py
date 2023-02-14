def not_set(nums):
    new_list = []
    for i in nums:
        if i not in new_list:
            new_list.append(i)
    return new_list

nums = list(map(int,input().split()))
print(not_set(nums))
