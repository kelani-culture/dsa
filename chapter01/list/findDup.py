def contains_duplicate(num):
    seen = set()
    
    for i in num:
        if i in seen:
            return True
        seen.add(i)
    
    return False
nums = [1,2,3]
print(contains_duplicate(nums))