import math

def message_encoder(s):
    # remove the spaces
    unspaced = s.replace(' ', '')
    # find the length of the string without spaces
    length_of_unspaced = len(unspaced)
    # get the grids and columns(square root of the length of string without spaces)
    cols = math.ceil(math.sqrt(length_of_unspaced))
    d_array = []
    # create a 2 d array and fill it with hashtags
    for i in range(cols):
        d_array.append([])
        for j in range(cols):
            d_array[-1].append("#")

    # replace the hashtags with the respective values of the string
    index = 0
    for i in range(cols):
        for j in range(cols):
            if index < length_of_unspaced:
                d_array[i][j] = unspaced[index]
            index += 1
    # print out the result after ensuring all the hastags have been replaced
    for j in range(cols):
        for i in range(cols):
            if d_array[i][j] != "#":
                print(d_array[i][j], end="")
        print(" ",end="")

    

s = "have a nice day"
a = message_encoder(s)
print(a)