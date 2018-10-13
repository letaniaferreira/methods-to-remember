def formingMagicSquare(s):
    single= []
    repeated = []
    missing = []
    final = 0
    index = 0
    while index < 3:
        for n in s[index]:
            if n not in single:
                single.append(n)
            else:
                repeated.append(n)
        index += 1
    for num in range(1, 10):
        if num not in single:
            missing.append(num)
    size = len(missing)
    idx = 0
    while idx < size:
        for n in repeated:
            val = n - missing[idx]
            if val < 0:
                val = val * -1
            final += val
            idx += 1
    
    return final
    
formingMagicSquare([[4, 8, 2], [4, 5, 7], [6, 1, 6]])