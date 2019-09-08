def plusMinus(arr):
    size = len(arr)
    positive = negative = zero = 0
    for num in arr:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zero += 1
    print(str.format('{0:.6f}', positive / size))
    print(str.format('{0:.6f}', negative / size))
    print(str.format('{0:.6f}', zero / size))