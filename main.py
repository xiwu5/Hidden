def hidden(matrix, n):
    # handle input validation

    
    #row = len(matrix)

    # initialize the return string


    
    # char = ''
    # index = 0
    # for row in matrix:
    #     for letter in row: 
    #         if index % n == 0: 
    #             char += letter
    #         index += 1
    # return char

    char = matrix[0][0]
    index = 0
    for row in matrix:
        for letter in row: 
            # char += letter # addon first letter
            # # addon index + n letter if index is not out of bound
            while index + n < len(row):
                print("current index", index)
                char += row[index + n]
                index += n
        print(char)

    return char

    

matrix_1 = (
    ('u','e','r','e', ' ', 'e'),
    #0.       2.      4
    ('d', 'z', 'o', 'b', 'i', 'v'),
    #0.        2.         4
    ('n',),
    #0

    ('w', 'g', 'q', ' ', '5', 'g', 'w'),
    # 0.        2.       4.         6
    ('r',),
    ('y', 'e'),
    ('u', 'a', 'u', 't')
)
assert hidden(matrix_1, 2) == 'ur doing great'
assert hidden(matrix_1, 3) == 'uedbnqgya'
assert hidden(matrix_1, 525600) == 'u'
assert hidden(matrix_1, 1) == 'uere edzobivnwgq 5gwryeuaut'

matrix_2 = (
    ('💜',),
)
assert hidden(matrix_2, 17) == '💜'
assert hidden(matrix_2, 1) == '💜'

print("All tests passed! Discuss time and space complexity if time remains!")

