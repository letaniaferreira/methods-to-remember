def singleNumber(nums):

    numbers = {}
    for n in nums:
        if n not in numbers:
            numbers[n] = 1
        else:
            numbers[n] += 1
    
    values = []


    
    for k, v in numbers.items():
        values.append(v)
    smaller = min(values)
    
    for key in numbers.keys():
        if numbers[key] == smaller:
            return key


answer = singleNumber([4,1,2,1,2])
print(answer)