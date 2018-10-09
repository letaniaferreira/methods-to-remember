def designerPdfViewer(h, word):
    import string
    max_index = 0
    letters = list(string.ascii_lowercase)
    for letter in word:
        lst_index = letters.index(letter)
        index_val = h[lst_index]
        if index_val > max_index:
            max_index = index_val
            
    return max_index * len(word)
    
designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7], 'zaba')